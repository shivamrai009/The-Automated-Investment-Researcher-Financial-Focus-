# 📈 AI Investment Researcher

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-orange)
![Groq](https://img.shields.io/badge/AI-Groq%20(Llama3)-blueviolet)
![License](https://img.shields.io/badge/License-MIT-green)

An autonomous **AI Agent** that acts as your personal financial analyst. This tool performs end-to-end investment research by fetching real-time stock data, scraping the latest financial news, and generating a professional "Buy, Sell, or Hold" recommendation using the **Llama 3** model (via Groq).

---

## 🚀 Features

* **Real-Time Data:** Fetches live stock prices using `yfinance`.
* **Market Sentiment:** Scrapes the latest news articles using `DuckDuckGo Search` to understand market trends.
* **Intelligent Reasoning:** Uses **LangGraph** and **Llama 3** to synthesize data and provide logical investment advice.
* **Interactive Dashboard:** Built with **Streamlit** for a clean, responsive UI.
* **Visual Charts:** Displays 1-year price history charts automatically.

---

## 🛠️ Tech Stack

* **LLM Engine:** Groq (Llama-3.3-70b-versatile) - *Fast & Free Inference*
* **Orchestration:** LangChain & LangGraph
* **Data Sources:** Yahoo Finance (Prices) & DuckDuckGo (News)
* **Frontend:** Streamlit
* **Language:** Python

---

## 📂 Project Structure

```text
├── src/
│   ├── agent.py       # Defines the AI Agent and LangGraph logic
│   ├── tools.py       # Custom tools for Stock Price & News Search
│   └── app.py         # Streamlit User Interface
├── requirements.txt   # Project dependencies
├── .env               # API Keys (Not pushed to GitHub)
└── README.md          # Project Documentation
