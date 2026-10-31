# Financial Data Extractor using LLMs

A simple application that extracts key financial metrics from news articles and earnings reports using LangChain, Groq, and Streamlit.

## About the Project

Built this as a weekend learning project to explore how Large Language Models (LLMs) can transform unstructured financial text into structured data.

The application takes a financial paragraph, extracts relevant metrics using an LLM, and presents the results in a table.

## Features

* Extracts Revenue, EPS, Net Income, Operating Income, Free Cash Flow, and Gross Margin.
* Compares actual figures with analyst estimates when available.
* Displays missing values as "Not reported".
* Supports light and dark themes.
* Simple and interactive Streamlit interface.

## Tech Stack

Python | LangChain | Groq (GPT OSS 120B) | Streamlit | Pandas

## How It Works

```text
Financial Paragraph
        ↓
LangChain Prompt
        ↓
Groq LLM (GPT OSS 120B)
        ↓
JSON Output Parser
        ↓
Pandas DataFrame
        ↓
Streamlit Results
```

## Run Locally

1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/financial-data-extractor-llm.git
cd financial-data-extractor-llm
```

2. Install dependencies**

```bash
pip install -r requirements.txt
```

3. Configure your API key**

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

4. Run the application**

```bash
streamlit run app.py
```

## Live Demo

**Streamlit App:** Add your deployed application URL here.

## Key Learnings

This project helped me understand LLM integration with LangChain, prompt engineering for structured extraction, JSON parsing, and deploying AI applications using Streamlit.

## Limitations

This is a learning project. Extracted values depend on the supplied text and LLM accuracy. The application does not independently verify financial information.

## Feedback

Suggestions and feedback are welcome!