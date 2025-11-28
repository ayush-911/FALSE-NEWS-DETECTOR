## CODE I USED 
import streamlit as st
import joblib

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

# ----------------------------
# CUSTOM CSS (FULL + FIXED)
# ----------------------------
st.markdown("""
<style>

    /* ------------------------------
       ANIMATED BACKGROUND
    ------------------------------ */
    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(135deg, #ff914d, #b44dff, #ff5ec4, #ff914d);
        background-size: 400% 400%;
        animation: gradientMove 12s ease infinite;
        color: white !important;
    }

    /* ------------------------------
       TOP RED BAR
    ------------------------------ */
    .top-bar {
        width: 100%;
        padding: 15px 0;
        background-color: red;
        text-align: center;
        font-size: 20px;
        font-weight: 600;
        color: white;
    }

    /* ------------------------------
       TITLE CONTAINER (NO COLLISION)
    ------------------------------ */
    .main-title-container {
        margin-top: 80px !important;  /* FIXES collision */
        position: relative;
        display: flex;
        justify-content: center;
    }

    /* ------------------------------
       SCANNING LINE
    ------------------------------ */
    @keyframes scanline {
        0% { top: 0%; opacity: 0.2; }
        50% { opacity: 1; }
        100% { top: 100%; opacity: 0.2; }
    }

    .scanline {
        position: absolute;
        left: 0;
        width: 100%;
        height: 4px;
        background: rgba(0,255,180,0.8);
        box-shadow: 0 0 10px #00ffcc;
        animation: scanline 3s linear infinite;
        margin-top: 30px;  /* prevents overlap */
    }

    /* ------------------------------
       PURPLE GLITCH EFFECT
    ------------------------------ */
    @keyframes glitchPurple {
        0% { 
            clip-path: inset(0 0 0 0);
            text-shadow: 0 0 12px #c77dff;
        }
        25% { 
            clip-path: inset(5px 0 25px 0); 
            transform: skew(1deg);
            text-shadow: 0 0 22px #d157ff;
        }
        50% { 
            clip-path: inset(12px 0 8px 0); 
            transform: skew(-1deg);
            text-shadow: 0 0 30px #f28dff;
        }
        75% { 
            clip-path: inset(3px 0 30px 0); 
            transform: skew(0.8deg);
            text-shadow: 0 0 18px #c77dff;
        }
        100% { 
            clip-path: inset(0 0 0 0);
            text-shadow: 0 0 12px #c77dff;
        }
    }

    /* ------------------------------
       FUTURISTIC BOXY TITLE PANEL
    ------------------------------ */
    .main-title {
        padding: 22px 40px;
        border: 4px solid #00ffcc;
        border-radius: 12px;

        background: rgba(0,255,180,0.10);
        backdrop-filter: blur(4px);

        text-align: center;
        color: white;
        font-size: 48px;
        font-weight: 900;

        text-shadow:
            0 0 12px #00ffcc,
            0 0 25px #00ffcc,
            0 0 40px #00ffcc;

        animation:
            neonBreath 3s ease-in-out infinite,
            glitchPurple 1.8s infinite;
    }

    @keyframes neonBreath {
        0% {
            box-shadow: 0 0 15px #00ff9d, 0 0 25px #00ff9d, inset 0 0 10px #00ff9d;
        }
        50% {
            box-shadow: 0 0 35px #00ff9d, 0 0 60px #00ff9d, inset 0 0 25px #00ff9d;
        }
        100% {
            box-shadow: 0 0 15px #00ff9d, 0 0 25px #00ff9d, inset 0 0 10px #00ff9d;
        }
    }

    /* ------------------------------
       BLUE GLOW LABEL
    ------------------------------ */
    label {
        color: white !important;
        font-size: 22px !important;
        font-weight: 700 !important;
        text-shadow:
            0 0 15px #66ccff,
            0 0 25px #66ccff,
            0 0 40px #66ccff;
    }

    /* ------------------------------
       FLOATING CAR-STYLE INPUT BOX
    ------------------------------ */
    @keyframes floatBox {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    textarea {
        border-radius: 18px !important;
        border: 4px solid #d5d5d5 !important;
        padding: 15px !important;

        background: linear-gradient(145deg, #fff27a, #ffe864) !important;
        color: white !important;
        font-weight: 600 !important;

        text-shadow: 0 0 10px red;

        box-shadow:
            0 15px 35px rgba(0,0,0,0.6),
            inset 0 0 12px rgba(255,255,255,0.8),
            inset 0 0 22px rgba(255,255,255,0.5),
            0 0 35px #00eaff,
            0 0 65px #00eaff,
            0 0 110px #00eaff;

        animation: floatBox 4s ease-in-out infinite;
    }

    ::placeholder {
        color: white !important;
        opacity: 1 !important;
    }

    /* ------------------------------
       BUTTON
    ------------------------------ */
    .stButton button {
        background-color: black !important;
        color: white !important;
        padding: 10px 22px;
        border-radius: 10px;
        font-size: 18px;
        border: 1px solid white !important;
    }

</style>
""", unsafe_allow_html=True)

# ----------------------------
# TOP BAR
# ----------------------------
st.markdown('<div class="top-bar">Made by Ayush Kumar Trivedi</div>', unsafe_allow_html=True)

# ----------------------------
# TITLE + SCANLINE
# ----------------------------
st.markdown("""
<div class="main-title-container">
    <div class="main-title">Fake News Detector</div>
    <div class="scanline"></div>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# LOAD MODEL
# ----------------------------
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ----------------------------
# INPUT
# ----------------------------
news = st.text_area("Enter the news text below:", height=200)

# ----------------------------
# PREDICTION
# ----------------------------
if st.button("Check"):
    if news.strip() == "":
        st.error("Please enter some text!")
    else:
        X = vectorizer.transform([news])
        prediction = model.predict(X)[0]

        if prediction == 1:
            st.error("🚨 This news is **FAKE**!")
        else:
            st.success("✔ This news is **REAL**!")

---

## 🚀 Project Overview

The **Fake News Detector** is a machine learning project that uses **TF-IDF Vectorization** and a trained **ML classification model** to determine whether a piece of news is real or fake.

Built using:
- **Python**
- **Scikit-learn**
- **Streamlit**
- **Natural Language Processing (NLP)**

This project is lightweight, fast, and perfect for learning ML, NLP, and deploying simple AI apps.

---

## 🧠 How It Works

1. User enters a news text/article  
2. Text is vectorized using **TF-IDF**  
3. A trained ML model predicts:  
   - ✅ **REAL**  
   - ❌ **FAKE**  
4. Result is displayed beautifully on the Streamlit interface.

---

## 📂 Project Structure

```
📦 FAKE-NEWS-DETECTOR
├── app.py                     # Streamlit Web App
├── model/
│   ├── fake_news_model.pkl    # Trained Classification Model
│   ├── vectorizer.pkl         # TF-IDF Vectorizer
├── REQUIREMENTS/
│   └── REQUIREMENTS.txt       # Required Dependencies
└── src/
    ├── fake_news_model.pkl    # Backup model
    └── vectorizer.pkl         # Backup vectorizer
```

---

## ▶️ Running the Project Locally

### **1️⃣ Install dependencies**
```bash
pip install -r REQUIREMENTS/REQUIREMENTS.txt
```

### **2️⃣ Run the Streamlit app**
```bash
streamlit run app.py
```

The app will open in your browser automatically.

---

## 🛠 Tech Stack

| Area | Tools Used |
|------|------------|
| **Language** | Python |
| **Web Framework** | Streamlit |
| **ML Toolkit** | Scikit-learn |
| **Vectorization** | TF-IDF |
| **Model** | Logistic Regression / Naive Bayes |

---

## 🧪 Model Training (Optional)

If you're retraining:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
```

Train → Save → Load inside **app.py**

---

## 🌐 Future Improvements
- Add dataset downloader  
- Add confidence score meter  
- Add better UI with animations  
- Deploy using Streamlit Cloud  
- Add option to upload text files / PDFs  
- Add sentiment-based analysis  

---

## 👤 Author

**Ayush Kumar Trivedi**  
Machine Learning & AI Enthusiast  
GitHub: https://github.com/ayush-s-91

---

<p align="center">⭐ If you like this project, consider giving it a star on GitHub!</p>
