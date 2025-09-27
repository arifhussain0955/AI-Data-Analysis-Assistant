📊 AI Data Analysis Assistant with Gemini 1.5 Flash
✨ Overview
This project is a powerful, interactive web application that transforms natural language questions into data insights. Built with Streamlit, it allows users to upload a CSV or Excel file and query their data using simple English. The core intelligence is powered by Google's Gemini 1.5 Flash model, orchestrated through LangChain's specialized pandas-dataframe-agent, enabling the AI to write and execute Python code to analyze the data.

This application simplifies data analysis, making it accessible to users without a coding background.

🚀 Features
File Flexibility: Supports uploading both CSV and Excel (.xlsx) files.

Gemini 1.5 Flash Intelligence: Leverages the high performance and reasoning capabilities of the gemini-1.5-flash model.

LangChain Pandas Agent: Uses the create_pandas_dataframe_agent to enable the LLM to write, run, and debug Python/Pandas code against your DataFrame.

Secure API Key Handling: Accepts the Gemini API Key securely via a Streamlit password input field.

Interactive UI: A clean, user-friendly interface built with Streamlit for quick file uploads and query submissions.

Real-Time Analysis: Provides immediate answers and insights into your data.

⚙️ Technologies Used
Technology	Purpose
Python 3.9+	Core programming language.
Streamlit	Building the interactive web user interface.
LangChain	Orchestrating the AI agent logic.
langchain-google-genai	Connector for the Gemini API.
gemini-1.5-flash	The underlying Large Language Model (LLM).
Pandas	Data manipulation and storage (DataFrame).

Export to Sheets
🛠️ Getting Started
Follow these steps to set up and run the AI Data Analysis Assistant locally.

Prerequisites
Python 3.9 or higher.

A Gemini API Key. You can obtain one from Google AI Studio.

Installation
Clone the repository:

Bash

git clone https://github.com/[YOUR_USERNAME]/ai-data-analysis-assistant.git
cd ai-data-analysis-assistant
Save app.py: Ensure the provided Python code is saved as app.py in the root of your project directory.

Create and activate a virtual environment (recommended):

Bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required Python packages:

Bash

pip install streamlit pandas openpyxl langchain-google-genai langchain-experimental
Running the Application
Start the Streamlit app:

Bash

streamlit run app.py
The application will automatically open in your web browser, typically at http://localhost:8501.

💡 How to Use
Upload Your Data: Click "Choose a file" and upload either a CSV or Excel (.xlsx) file. The app will display the first 5 rows to confirm.

Enter API Key: Paste your Google Generative AI API Key into the secure text input field.

Ask a Question: Enter any question about your data. The Gemini agent is capable of complex operations, including aggregation, filtering, and visualization (though Streamlit will only display the textual result of the code executed by the agent).

Query Examples:

"What is the total revenue for the top 3 selling products?"

"Plot a histogram of the 'Age' column."

"Show the average 'Price' for each unique value in the 'Category' column."
