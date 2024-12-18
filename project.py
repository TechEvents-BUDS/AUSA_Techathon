import streamlit as st
from openai import OpenAI
import google.generativeai as genai
import textwrap
import os


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# configuring API key
genai.configure(api_key=GEMINI_API_KEY)
# initializing text_doc as None
text_doc = None

# Initializing session variables
if 'text' not in st.session_state:
    st.session_state['text'] = False

# returns final prompt for health-related guidance
def make_prompt(symptom_details):
    escaped = symptom_details.replace("'", "").replace('"', "").replace("\n", " ")
    prompt = textwrap.dedent("""You are a helpful and informative health assistant. Based on the following symptoms and details, provide personalized advice on potential sicknesses and how to manage them.
    
    SYMPTOMS AND DETAILS: '{symptom_details}'

    ADVICE:
    """).format(symptom_details=escaped)

    return prompt

# Streamlit elements for health assistant
st.subheader('AI-Powered Personalized Health Assistant', divider='rainbow')

# Enable text input for symptoms
st.session_state['text'] = True

# Code for text input to describe symptoms
if st.session_state['text']:
    text_input = st.text_area("Describe your symptoms and health concerns:")
    if text_input:
        text_doc = text_input

# Code to generate health advice
if st.button("Get Health Advice"):
    if text_doc is not None:
        with st.spinner("Analyzing symptoms..."):
            try:
                prompt = make_prompt(text_doc)
                # using Gemini model for personalized health advice
                model = genai.GenerativeModel('gemini-pro')
                # generate response for the final prompt
                response = model.generate_content(prompt)
            except Exception as e:
                st.error(f"An error occurred. {e}")
                
        with st.expander("See Health Advice"):
            # display the response contents
            st.write(response.text)

        # button to download health advice
        st.download_button('Download Health Advice', response.text)

    else:
        st.error("Please provide your symptoms.")