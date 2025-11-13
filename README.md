# 🗨️ Knowledge-Based Chatbot (Docker + Streamlit + LangChain)

This is a **RAG-based chatbot** built using **Streamlit**, **LangChain**, and **Google Gemini**.  
It reads and understands PDF documents to answer user queries accurately.

---

## 🚀 Features
- 💬 Chat interface using Streamlit  
- 📚 Retrieval-Augmented Generation (RAG) pipeline  
- 🧠 Uses FastEmbed for local embeddings  
- ⚡ Gemini LLM for smart and contextual answers  
- 🐳 Docker support for easy deployment  

---

## 🏗️ Tech Stack
- Python 3.12  
- Streamlit  
- LangChain  
- ChromaDB  
- FastEmbed  
- Google Gemini API  
- Docker  

---

## 📂 Project Structure

chatbot-docker/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .env
├── HistoryofGoldElsevier2ndedition.pdf
└── README.md


## 🧰 Setup Instructions

### 1️⃣ Clone or Download the Repo

If using Git:
```bash
git clone https://github.com/<your-username>/chatbot-docker.git
cd chatbot-docker
````

If not, just upload your project folder manually to GitHub.

---

### 2️⃣ Add Your Google API Key

Create a `.env` file inside the project:

```
GOOGLE_API_KEY=your_api_key_here
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Chatbot

```bash
streamlit run app.py
```

Then open your browser at **[http://localhost:8501]**

---

## 🐳 Run with Docker

### Build the Image

```bash
docker build -t chatbot-docker .
```

### Run the Container

```bash
docker run -p 8501:8501 chatbot-docker
```

---

## ✨ Author

**Nithiyasree R**
Built with using Python and LangChain.
