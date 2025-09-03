import streamlit as st
import os
from PIL import Image
from io import BytesIO
import tensorflow as tf
import numpy as np
import cv2 as cv

if 'is_valid_employee' not in st.session_state:
    st.session_state.is_valid_employee = ""

if 'employee_name' not in st.session_state:
    st.session_state.employee_name = ""

model = tf.keras.models.load_model('sign_data/my_model.h5')

# Replace this dictionary with your employee database of the format - Name : Filepath to one of the Name's original signature image
img_database = {
    'Alice' : "sign_data/train/001/001_01.PNG",
    'Bob' : "sign_data/train/002/002_01.PNG",
    'Carol' : "sign_data/train/003/003_01.PNG",
    'Denver' : "sign_data/train/004/004_01.PNG",
    'Ellie' : "sign_data/train/006/006_01.PNG",
    'Ferb' : "sign_data/train/009/009_01.PNG",
    'Ginny' : "sign_data/train/012/012_01.PNG",
    'Henry' : "sign_data/train/013/013_01.PNG",
    'Ian' : "sign_data/train/014/014_01.PNG",
    'Jacob' : "sign_data/train/015/015_01.PNG"
}

def sidebar():
    with st.sidebar:
        st.markdown("<h1 style='font-style: italic; color: #519691;'>Hey <span style = 'color: #6B564C;'> There!</span></h1>", unsafe_allow_html=True)
        st.write("")

        st.subheader("ABOUT:")
        st.markdown("""Welcome to AuthenSign🔐, where cutting-edge technology meets seamless signature verification! Simplify your authentication 
                    process with our advanced system, ensuring reliability and setting a new standard in verification excellence.""")
        st.write("")
        st.write("")


def verify_employee_id(employee_id):

    # Replace this dictionary with your employee database of the format - EmployeeId : Name
    employee_database = {
        '001': 'Alice',
        '002': 'Bob',
        '003': 'Carol',
        '004': 'Denver',
        '005': 'Ellie',
        '006': 'Ferb',
        '007': 'Ginny',
        '008': 'Henry',
        '009': 'Ian',
        '010': 'Jacob'
    }

    if employee_id in employee_database:
        return True, employee_database[employee_id]
    else:
        return False, None


def preprocess(img):
    img = cv.resize(img, (128, 128, ))
    img = cv.Canny(img, 20, 200)
    img = img / 255.
    img = np.expand_dims(img, axis = -1)
    return img
    

def verify_signature(employee, signature_image):
    pil_image = Image.open(BytesIO(signature_image.read()))
    uploaded_img = cv.cvtColor(np.array(pil_image), cv.COLOR_RGB2BGR)
    database_img = cv.imread(img_database[employee])
    img1 = preprocess(uploaded_img)
    img1 = np.expand_dims(img1, axis = 0)
    img2 = preprocess(database_img)
    img2 = np.expand_dims(img2, axis = 0)

    y_prob = model.predict([img1, img2])
    y_pred = (y_prob > 0.2).astype(int)
    print(y_prob)
    if y_pred == 0:
        st.success("Signature verification successful!")
    else:
        st.error("Signature verification failed. Try again!")

    
def main():
    st.set_page_config(page_title = "AuthenSign・Streamlit", page_icon = "🔐")
    sidebar()
    st.markdown(
        """
        <style>
        .stApp {
            align-items: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<h1 style='margin-bottom:-3%;'> <span style='color:#EB6A0E;'>Authen</span><span style='color:#96613B;'> Sign</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style = 'padding-bottom: 2%'>🔐 Cutting-edge signature verification made seamless</p>", unsafe_allow_html = True)
    st.write("Please enter your Employee ID and upload your signature image for verification.")

    container = st.container(border = True)
    container.markdown("<h2 style='text-align: center; color: white;'>LOGIN</h2>", unsafe_allow_html=True)

    employee_id = container.text_input("Enter Employee ID:")

    verify = st.button("Verify", key = "button1")

    if "verify_state" not in st.session_state:
        st.session_state.verify_state = False

    if verify or st.session_state.verify_state:
        st.session_state.verify_state = True

        is_valid_employee, employee_name = verify_employee_id(employee_id)

        if is_valid_employee:
            st.success(f"Employee ID {employee_id} is valid. Welcome, {employee_name}!")

            uploaded_file = st.file_uploader("Upload signature image", type = ['jpeg', 'png', 'jpg', 'webp'], 
                                            help = "SVG Documents aren't supported yet!")

            if uploaded_file is not None:
                st.write("Image uploaded successfully!")
                st.empty()
                st.markdown("---")

                if st.button("Verify Signature"):
                    with st.spinner("Verifying Signature... This may take a while ⏳"):
                        verify_signature(employee_name, uploaded_file)
        else:
            st.error(f"Invalid Employee ID: {employee_id}. Please try again.")


if __name__ == "__main__":
    main()