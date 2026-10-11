import streamlit as st
import os
from dotenv import load_dotenv
from utils.llm_handler import init_model, build_history
from utils.crisis_detector import detect_crisis, CRISIS_RESPONSE
from utils.recommendations import get_recommendation

load_dotenv()

st.set_page_config(page_title="KonsulKita 💙", page_icon="💙", layout="centered")

st.title("💙 KonsulKita")
st.caption("Teman curhat AI untuk remaja. Bukan pengganti psikolog profesional.")

# --- Sidebar: Config & Memory ---
with st.sidebar:
    st.header("⚙️ Pengaturan")
    user_name = st.text_input("Nama kamu", value="Teman")
    mood = st.selectbox("Mood hari ini", ["😊 Senang", "😐 Biasa", "😔 Sedih", "😰 Cemas", "😩 Capek", "😡 Marah"])
    
    st.divider()
    st.subheader("💡 Rekomendasi untukmu")
    for rec in get_recommendation(mood):
        st.write(f"- {rec}")
    
    st.divider()
    if st.button("🗑️ Reset Percakapan"):
        st.session_state.messages = []
        st.rerun()
    
    st.caption("🚨 Darurat? Hubungi **119 ext 8**")

# --- Init API ---
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY belum diset di file .env")
    st.stop()

model = init_model(api_key)

# --- Init session ---
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": f"Hai {user_name}! 👋 Aku KonsulKita. Gimana perasaan kamu hari ini? Cerita aja, aku dengerin kok."
    }]

# --- Render history ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="💙" if msg["role"]=="assistant" else "🙂"):
        st.markdown(msg["content"])

# --- Input ---
if prompt := st.chat_input("Cerita apa aja di sini..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🙂"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="💙"):
        # Deteksi krisis dulu
        if detect_crisis(prompt):
            response = CRISIS_RESPONSE
            st.markdown(response)
        else:
            with st.spinner("Aku dengerin..."):
                try:
                    history = build_history(st.session_state.messages[:-1])
                    chat = model.start_chat(history=history)
                    result = chat.send_message(prompt)
                    response = result.text
                except Exception as e:
                    response = f"Aduh, ada error: {e}. Coba lagi ya 🙏"
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})