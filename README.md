# 🏗️ Construction Progress Estimator (Vision + LLM)

This project is a web-based tool that estimates construction progress by comparing 2D architectural renderings with real-site construction images. It uses Vision-Language Models (like LLaVA) and LLMs (like LLaMA-4 via Groq) to provide structured progress insights.

---

## 🚀 Features

- Upload floor plans and real construction photos
- Estimate completion percentage using AI
- Structured analysis of completed vs pending components
- Streamlit UI + FastAPI backend
- Asynchronous and modular design

---

## 🖼️ How It Works

1. Upload two images: a rendered design and a real construction photo
2. Backend encodes and sends them to Groq API (LLaMA-4)
3. The model returns a formatted analysis like:

```
Progress Completed: 70%

Completed Work:
- Foundation and wall structures
- First floor slab poured

Pending Work:
- Roofing and window installation
- External plaster and paint
```

4. Streamlit displays the result

---

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **AI Model**: Groq LLaMA-4 Maverick
- **Encoding**: Base64, dotenv
- **HTTP Client**: httpx (async)

---

## 📦 Installation

```bash
git clone https://github.com/your-username/construction-progress-estimator
cd construction-progress-estimator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Run the App

### 1. Start the FastAPI backend

```bash
uvicorn backend.main:app --reload
```

### 2. Start the Streamlit frontend

```bash
streamlit run frontend/app.py
```

---

## 📄 License

This project is licensed under the MIT License.
