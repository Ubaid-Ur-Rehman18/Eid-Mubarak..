import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load 3D Eid animation
lottie_eid = load_lottieurl("https://lottie.host/2de47cf7-9c65-4078-a3e4-321af94fbd49/HZV6wXhEuU.json")

st.set_page_config(page_title="Eid Mubarak", page_icon="🌙", layout="centered")

st.title("✨ Eid-ul-Fitr Mubarak! ✨")

st.write("**May Allah bless you with happiness, health, and success!**")

st_lottie(lottie_eid, height=300)

st.subheader("🌙 Beautiful Dua for Eid")

# Dropdown for translation selection
translation_option = st.selectbox("Select Language:", ["Urdu", "English"])

urdu_dua = "اللّهُمَّ أَهِلَّهُ عَلَيْنَا بِالأَمْنِ وَالإِيمَانِ وَالسَّلَامَةِ وَالإِسْلَامِ"
english_dua = "O Allah, bring this crescent upon us with safety, faith, and Islam."

if translation_option == "Urdu":
    st.write(f"**Dua (Urdu):** {urdu_dua}")
elif translation_option == "English":
    st.write(f"**Dua (English):** {english_dua}")

st.markdown("---")
st.write("© All Rights Reserved | Ubaid-ur-Rehman")
