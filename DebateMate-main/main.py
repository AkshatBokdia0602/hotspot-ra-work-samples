import streamlit as st
import google.generativeai as genai

if "messages" not in st.session_state:
    st.session_state["messages"] = []
messages = st.session_state["messages"]


def set_google_api_key(api_key):
    st.session_state["GOOGLE_API_KEY"] = api_key


def sidebar():
    with st.sidebar:
        st.subheader("About")
        st.markdown("""Welcome to DebateMate 💬, your AI-powered debate partner! Enhance your debating skills with
        tailored experiences, whether you're a beginner or advanced. Choose your complexity level and topic, and
        engage in dynamic, thought-provoking discussions. Perfect for students and debate enthusiasts, DebateMate 💬
        helps you master the art of argumentation and critical thinking. Get ready to excel in debates and make your
        voice heard with DebateMate 💬!""")
        st.write("")
        st.write("")
        api_key_input = st.text_input("Enter your Gemini API Key",
            type = "password",
            placeholder = "Paste your Gemini API key here (sk-...)",
            help = "You can get your API key from https://aistudio.google.com/app/u/1/apikey.",
            value = st.session_state.get("OPENAI_API_KEY", ""))

        st.markdown("<h1 style='font-style: italic; color: #A9A9A9;'>Settings</h1>", unsafe_allow_html = True)
        st.write("")
        selected_level = st.sidebar.radio("Select the level of complexity", ["Beginner", "Intermediate", "Advanced"])
        selected_topic = st.sidebar.text_input("Enter your debate topic")

        st.subheader("HOW TO USE: ")
        st.markdown("<p style = 'cursor: default;'>1. Enter your Gemini's API KEY."
                    "<br>2. Choose level of complexity that your AI partner will showcase."
                    "<br>3. Enter your debate topic/question."
                    "<br>4. Start debating with your personalised AI Debate Partner.", unsafe_allow_html = True)

        return api_key_input, selected_level, selected_topic


def generate_debate_prompt(level, topic):
    if level == "Beginner":
        return f"""Assume you are a debate partner for a beginner student. Your goal is to engage in a friendly debate
        on the topic '{topic}'. Start with simple, clear arguments and counterarguments, and provide supportive
        explanations. Ensure your language is easy to understand and avoid using complex terminology. Try to answer as
        if you are a human and keep it short and concise."""

    elif level == "Intermediate":
        return f"""Assume you are a debate partner for an intermediate student. Your goal is to engage in a debate on the topic
        '{topic}'. Provide more detailed arguments and counterarguments with moderate complexity. Use some technical
        terms and encourage critical thinking. Try to answer as if you are a human and keep it short and concise."""

    elif level == "Advanced":
        return f"""Assume you are a debate partner for an advanced student. Your goal is to engage in a sophisticated debate
        on the topic '{topic}'. Provide complex, nuanced arguments and counterarguments, using advanced terminology and
        encouraging deep analysis. Challenge the student's critical thinking skills. Try to answer as if you are a human
        and keep it short and concise."""


def get_response(messages):
    model = genai.GenerativeModel('gemini-1.5-pro')
    res = model.generate_content(messages)
    return res


def check(message):
    model = genai.GenerativeModel('gemini-1.5-pro')
    res = model.generate_content(f"""Evaluate the content to identify any harmful language, inappropriate words,
    or content that violates rules or guidelines. Provide a binary response:
    True if the content is harmful or contains inappropriate words.
    False if the content is acceptable and does not contain harmful or inappropriate elements.
    Content: {message}""")
    return res


def main():
    st.set_page_config(page_title = "DebateMate・Streamlit", page_icon = "💬")
    api_key_input, selected_level, selected_topic  = sidebar()
    genai.configure(api_key = api_key_input)
    st.markdown("<h1 style='margin-bottom:-3%;'> <span style='color:#21A6FF;'>Debate</span><span style='color:#00F555;'> Mate</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style = 'padding-bottom: 2%'>✨  AI-Powered Interactive Debate Partner</p>", unsafe_allow_html = True)

    if messages:
        for item in messages:
            role, parts = item.values()
            if role == "user":
                st.chat_message("user").markdown(parts[0].split("......")[0])
            elif role == "model":
                st.chat_message("assistant").markdown(parts[0])

    chat_message = st.chat_input("Message DebateMate")
    res = None

    if selected_topic == "" and chat_message is not None:
        st.error("Kindly ENTER your debate topic first!")

    else:
        debate_prompt = generate_debate_prompt(selected_level, selected_topic)

        if chat_message:
            st.chat_message("user").markdown(chat_message)
            res_area = st.chat_message("assistant").markdown("...")

            response = check(chat_message)
            if response.candidates[0].finish_reason.value == 3 or response.text == "True":
                st.error("Your words violate the rules that have been set. Please TRY AGAIN!")

            else:
                messages.append({"role": "user", "parts": [chat_message + "......" + debate_prompt]},)

                res = get_response(messages)

                if res is not None:
                    res_text = ""
                    for chunk in res:
                        if chunk.candidates:
                            res_text += chunk.text
                    res_area.markdown(res_text)

                    messages.append({"role": "model", "parts": [res_text]})

if __name__ == "__main__":
    main()