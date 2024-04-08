import streamlit as st
from llm_model import prompt, load_LLM

## Functions
def get_input_text():
    input_text = st.text_area(label="Your Email", placeholder = "Write your email here...", key="email_input")
    return input_text

def email_example():
    print ("example shown")
    st.session_state.email_input = "Hey Dave, I am starts work at yours monday. lmk if that works thanks, Paul"


#### --------------
#### Streamlit Start
#### --------------
st.set_page_config(page_title="Globalize Email", page_icon=":shark:")
st.header("Globalize Text")

## 1st Portion of Web
col1, col2 = st.columns(2)

with col1: 
    st.markdown("Often professionals would like to improve their emails, but don't have the skills to do so. This tool will help you improve your emails by converting your emails into a more professional format. This tool is powered by [LangChain](https://www.langchain.com) and [OpenAI](https://openai.com)")

with col2: 
    st.image(image = 'Grammarly.png', width=500, caption='Example of Grammarly Value Proposition')

st.markdown("## Enter Your Email to Convert")

## 2nd Portion of Web (User Inputs)
col1, col2 = st.columns(2)
with col1:
    option_tone = st.selectbox("Which tone would you like your email to have?", 
                               ('Formal', 'Informal'))

with col2:
    option_dialect = st.selectbox('Which English Dialect would you like?', 
                                  ('American English', 'British English', 'Australian English'))

user_email_input = get_input_text()

if len(user_email_input.split(" ")) > 700:
    st.write("Please enter a shorter email. The maximum length is 700 words.")
    st.stop()

st.button("*See An Example*", type='secondary', help="Click to see an example of the email you will be converting.", on_click=email_example)

st.markdown("## Your Converted Email:")

if user_email_input:
    llm = load_LLM()
    prompt_with_email = prompt.format(tone=option_tone, dialect=option_dialect, email=user_email_input)
    
    formatted_email = llm(prompt_with_email)

    st.write(formatted_email)
