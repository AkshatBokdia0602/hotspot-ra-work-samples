import cv2
import time
import numpy as np
import json
from controlkeys import right_pressed,left_pressed,up_pressed,down_pressed,space_pressed
from controlkeys import KeyOn, KeyOff
import tensorflow as tf
from keras.models import model_from_json
from tensorflow.keras.preprocessing import image

left_key_pressed = left_pressed
right_key_pressed = right_pressed
up_key_pressed = up_pressed
down_key_pressed = down_pressed
space_key_pressed = space_pressed

f = open('my_model_arch.json')
json_string = json.load(f)
model = model_from_json(json_string)
model.load_weights('my_model_weights.h5')

def prepare_image(img):
    img_array_expanded_dims = np.expand_dims(img, axis = 0)
    return tf.keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)


video = cv2.VideoCapture(0)


while True:
    ret,image = video.read()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable=False
    image.flags.writeable=True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    cv2.imshow("Frame",image)
    k = cv2.waitKey(1)
    
    if k == ord('q'):
        break
    
    image_new = cv2.resize(image, (150, 150))
    preprocessed_image = prepare_image(image_new)

    predictions = model.predict(preprocessed_image)

    value = np.argmax(predictions)
    prob = predictions[0][value] * 100
    
    if value == 0:
        pass

    elif value == 1 and prob > 99.99:
        print('space')
        KeyOn(space_key_pressed)
        KeyOff(space_key_pressed)

    elif value == 2 and prob > 99.99:
        print('down')
        KeyOn(down_key_pressed)
        KeyOff(down_key_pressed)

    elif value == 3 and prob > 99.99:
        print('up')
        KeyOn(up_key_pressed)
        KeyOff(up_key_pressed)

    time.sleep(2.0)
    
video.release()
cv2.destroyAllWindows()