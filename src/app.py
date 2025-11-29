import streamlit as st
import joblib

st.set_page_config(page_title="Fake News Detector — Cosmic", page_icon="🚀", layout="wide")

model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ------------------------------
# PURE SAFE CSS (NO F-STRINGS, NO ERRORS)
# ------------------------------
st.markdown("""
<style>

html, body, .stApp {
    height: 100%;
    overflow: hidden !important;
    background:
        radial-gradient(900px 500px at 10% 10%, rgba(120,80,200,0.18), transparent 55%),
        radial-gradient(900px 500px at 90% 80%, rgba(20,200,255,0.16), transparent 55%),
        linear-gradient(180deg, #05021a 0%, #071234 40%, #050818 100%) !important;
    font-family: 'Segoe UI', system-ui, sans-serif;
}

/* Remove top padding */
.main > div { padding-top: 0 !important; }

/* ----------------- Nebula clouds ----------------- */
.nebula {
    position: fixed;
    width: 1000px;
    height: 600px;
    left: -200px;
    top: -100px;
    background: radial-gradient(circle, rgba(140,80,210,0.25), transparent 70%);
    filter: blur(80px);
    opacity: 0.6;
    animation: nebulaMove 20s ease-in-out infinite alternate;
    z-index: 1;
}
.nebula2 {
    position: fixed;
    width: 900px;
    height: 600px;
    right: -250px;
    top: 150px;
    background: radial-gradient(circle, rgba(20,200,255,0.2), transparent 70%);
    filter: blur(80px);
    opacity: 0.5;
    animation: nebulaMove 26s ease-in-out infinite alternate;
    z-index: 1;
}

@keyframes nebulaMove {
    0%   { transform: translate(0px,0px); }
    100% { transform: translate(40px,-25px); }
}

/* ----------------- Stars ----------------- */
.star {
    position: fixed;
    width: 3px;
    height: 3px;
    background: white;
    border-radius: 50%;
    box-shadow: 0 0 6px white;
    animation: twinkle 4s infinite ease-in-out;
    z-index: 2;
}
@keyframes twinkle {
    0%   { opacity: 0.5; transform: scale(0.8); }
    50%  { opacity: 1;   transform: scale(1.4); }
    100% { opacity: 0.5; transform: scale(0.8); }
}

/* Place many stars around screen */
.star.s1  { top:5vh;  left:10vw; }
.star.s2  { top:18vh; left:30vw; }
.star.s3  { top:12vh; left:60vw; }
.star.s4  { top:22vh; left:80vw; }
.star.s5  { top:45vh; left:15vw; }
.star.s6  { top:40vh; left:55vw; }
.star.s7  { top:72vh; left:25vw; }
.star.s8  { top:68vh; left:70vw; }

/* ----------------- Shooting stars ----------------- */
.shoot {
    position: fixed;
    width: 3px;
    height: 120px;
    background: linear-gradient(90deg, white, transparent);
    transform: rotate(-25deg);
    opacity: 0;
    animation: shootMove 4s linear infinite;
    z-index: 3;
}
.shoot.sA { top:10vh; left:-10vw; }
.shoot.sB { top:50vh; left:-20vw; animation-delay:2s; }

@keyframes shootMove {
    0%   { opacity:0; transform:translate(0,0) rotate(-25deg); }
    10%  { opacity:1; }
    40%  { opacity:1; transform:translate(40vw,20vh) rotate(-25deg); }
    100% { opacity:0; transform:translate(80vw,40vh) rotate(-25deg); }
}

/* ----------------- Spaceships ----------------- */
.ship {
    position: fixed;
    font-size: 90px;
    opacity: 0.95;
    animation: shipMove 18s ease-in-out infinite;
    z-index: 4;
}
.ship.s1 { top:20vh; left:-10vw; }
.ship.s2 { top:55vh; left:-15vw; animation-duration:22s; }
.ship.s3 { top:35vh; left:-12vw; animation-duration:20s; }

@keyframes shipMove {
    0%   { transform: translate(0vw,0vh) rotate(0deg); }
    25%  { transform: translate(30vw,-5vh) rotate(-8deg); }
    50%  { transform: translate(60vw,5vh) rotate(6deg); }
    75%  { transform: translate(80vw,-4vh) rotate(-5deg); }
    100% { transform: translate(110vw,0vh) rotate(0deg); }
}

/* ----------------- UI Foreground ----------------- */
.ui { position: relative; z-index: 10; }

.ayush-bar {
    background: red;
    color: white;
    padding: 14px;
    font-size: 20px;
    text-align: center;
    border-radius: 10px;
    margin-top: 15px;
    box-shadow: 0 5px 20px rgba(255,0,0,0.5);
}

.main-title {
    font-size: 65px;
    font-weight: bold;
    text-align: center;
    color: white;
    text-shadow:
        0 0 10px #00eaff,
        0 0 20px #00eaff,
        0 0 40px #00eaff;
}

/* Cloud textbox */
textarea {
    background: rgba(255,255,255,0.95) !important;
    color: black !important;
    border-radius: 45px !important;
    padding: 25px !important;
    font-size: 18px !important;
    border: none !important;
    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
}

</style>

<!-- Nebulas -->
<div class="nebula"></div>
<div class="nebula2"></div>

<!-- Stars -->
<div class="star s1"></div>
<div class="star s2"></div>
<div class="star s3"></div>
<div class="star s4"></div>
<div class="star s5"></div>
<div class="star s6"></div>
<div class="star s7"></div>
<div class="star s8"></div>

<!-- Shooting Stars -->
<div class="shoot sA"></div>
<div class="shoot sB"></div>

<!-- Spaceships -->
<div class="ship s1">🚀</div>
<div class="ship s2">🛸</div>
<div class="ship s3">🛰️</div>

""", unsafe_allow_html=True)

# ------------------------------
# UI CONTENT
# ------------------------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown("<div class='ui'>", unsafe_allow_html=True)

    st.markdown("<div class='ayush-bar'>Made by Ayush Kumar Trivedi ❤ — Made with Love</div>", unsafe_allow_html=True)
    st.markdown("<div class='main-title'>🌌 False News Detector — Cosmic</div>", unsafe_allow_html=True)

    user_input = st.text_area("Enter News Text:", height=200)

    if st.button("Check News"):
        if user_input.strip() == "":
            st.warning("Please enter some text!")
        else:
            X = vectorizer.transform([user_input])
            pred = model.predict(X)[0]

            if pred == 1:
                st.error("❌ Fake News Detected!")
            else:
                st.success("✔ Real News!")

    st.markdown("</div>", unsafe_allow_html=True)
