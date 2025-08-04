# SmartWP-Content-Enhancer

An AI-powered WordPress plugin that integrates with OpenAI to help users rewrite, summarize, and improve content directly in the WordPress editor.

## 🔧 Features

- ✍️ Rewrite selected text  
- 🧠 Summarize content blocks  
- 🖼️ Auto-generate alt text for images  
- 💬 Tone conversion (e.g., formal ↔ casual)  
- 📊 Usage metrics with token tracking  

## 🧱 Tech Stack

- **Frontend:** WordPress JS / Gutenberg block  
- **Backend:** Python (FastAPI)  
- **AI Engine:** OpenAI GPT API  
- **Optional:** Docker, Firebase for logging  

## 📁 Folder Structure
```
/frontend # WordPress JS or Gutenberg block
/backend # FastAPI server calling OpenAI
/utils # Prompt templates and helpers
/logs # Optional: token usage + logs
README.md # You're here
```

## 🚀 Getting Started

1. Clone the repo  
2. Start backend with `uvicorn backend.main:app --reload`  
3. Connect WordPress frontend via REST API  
4. Add your OpenAI API key to `.env`  
5. Test rewrite and summarization tools  

## 🧪 Demo

![Demo GIF](demo.gif)

## 📋 License

MIT
