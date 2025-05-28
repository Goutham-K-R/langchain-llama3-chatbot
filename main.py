from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ['Langchain_API_KEY']=os.getenv("Langchain_API_KEY")


# prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Answer the user's questions clearly."),
    ("user", "Question: {question}"),
])

st.title("Langchain Chatbot with Ollama")
input_text = st.text_input("💬 Enter your question:")

llm =Ollama(model="llama3")
out_parser = StrOutputParser()
chain = prompt | llm | out_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))