from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# prompt temp

prompt=ChatPromptTemplate.from_messages(
  [
    ("system","You are helpful assistant. Please response to the user queries"),
    ("human","Question:{question}")

  ]
)
# Streamlit framework

st.title('Chatbot Using Ollama ')
input_text=st.text_input("What's in your mind ??")

# Ollama LLAma2  llm's

llm=OllamaLLM(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

# Handle input
if input_text:
    st.write(chain.invoke({'question': input_text}))