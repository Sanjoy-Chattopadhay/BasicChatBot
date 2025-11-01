# 🤖 AI Assistant Hub

A powerful, multi-featured AI chatbot built with LangChain, OpenAI GPT-4o, and Streamlit. This project showcases three distinct AI capabilities: conversational chat with memory, research paper summarization, and automated report generation.

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.51.0-red.svg)
![LangChain](https://img.shields.io/badge/langchain-0.3.7-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Features

### 💬 Conversational AI
- **Context-aware conversations** with full chat history retention
- Real-time responses powered by GPT-4o
- Clean, intuitive chat interface with user and assistant avatars
- Session state management for persistent conversations

### 📚 Research Paper Summarizer
- Summarize popular AI research papers on demand
- **Customizable output styles:**
  - Beginner-Friendly
  - Technical
  - Code-Oriented
  - Mathematical
- **Adjustable summary lengths:** Short, Medium, or Long
- Includes mathematical equations and practical analogies
- Download summaries as text files

### 📄 Advanced Report Generator
- Generate comprehensive reports on any topic using AI chaining
- **Two-step process:**
  1. Creates detailed, multi-paragraph reports
  2. Automatically generates 5-line executive summaries
- Real-time progress tracking
- Side-by-side display of summary and full report
- Download both summary and full report

## 🚀 Live Demo

**[View Live App](https://basic-chatbot.streamlit.app/)** 

## 📸 Screenshots

### Conversational Chat Interface
Beautiful gradient UI with persistent chat history and real-time responses.

### Research Summarizer
Customizable research paper summaries with style and length options.

### Report Generator
Automated report creation with executive summaries using LangChain prompt chaining.

## 🛠️ Tech Stack

- **Frontend:** Streamlit 1.51.0
- **AI Framework:** LangChain 0.3.7
- **LLM:** OpenAI GPT-4o (via langchain-openai 0.2.9)
- **Language:** Python 3.13
- **Dependencies:** python-dotenv, openai, httpx

## 📦 Installation

### Prerequisites
- Python 3.9 or higher (3.13 recommended)
- OpenAI API key
- Git

### Local Setup

1. **Clone the repository**
git clone https://github.com/Sanjoy-Chattopadhay/BasicChatBot.git
cd BasicChatBot

2. **Create virtual environment**
Windows
python -m venv venv
venv\Scripts\activate


3. **Install dependencies**
pip install -r requirements.txt


4. **Set up environment variables**

Create a `.env` file in the root directory:
OPENAI_API_KEY=your_openai_api_key_here


**⚠️ Security Note:** Never commit your `.env` file to version control. It's already included in `.gitignore`.

5. **Run the application**

streamlit run app.py

The app will open in your browser at `http://localhost:8501`


