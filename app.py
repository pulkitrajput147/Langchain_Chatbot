# Importing Necessary Libraries
import os
import openai
from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st

# Loading the environment variable
load_dotenv()

# Function to load openai model and get response
def get_response(question):
    llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"),model_name="gpt-3.5-turbo-instruct",temperature=0.6)
    response=llm(question)
    return response


# Initializing the Streamlit
st.set_page_config(page_title="Q&A Chatbot")
st.header("Langchain Application")
input=st.text_input("Input :",key="input")
response=get_response(input)
submit=st.button("Submit")
    # if ask button is clicked
if submit:
    st.subheader("Result : ")
    st.write(response)

