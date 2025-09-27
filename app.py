# AI Data Analysis Web App using Streamlit, LangChain, and Google Generative AI (Gemini)

import streamlit as st
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("AI Data Analysis Assistant (Gemini)")

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

df = None

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    st.write("First 5 rows of the uploaded file:")
    st.write(df.head())

    st.write("Ask a question about your data:")

    question = st.text_input("Enter your question")

    api_key = st.text_input("Enter your Google Generative AI API Key", type="password")

    if question and api_key:
        def create_agent(df, api_key):
            llm = ChatGoogleGenerativeAI(google_api_key=api_key, model="gemini-1.5-flash", temperature=0)
            agent = create_pandas_dataframe_agent(llm, df, verbose=True)
            return agent

        agent = create_agent(df, api_key)

        with st.spinner("Analyzing..."):
            try:
                answer = agent.run(question)
                st.write("Answer:")
                st.write(answer)
            except Exception as e:
                st.error(f"Error: {e}")