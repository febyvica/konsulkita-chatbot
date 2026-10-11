# 💙 KonsulKita - AI Mental Health Companion untuk Remaja

Chatbot berbasis LLM (Google Gemini 1.5 Flash) yang menemani remaja Indonesia 
(13-19 tahun) untuk bercerita tentang kondisi emosional mereka dengan pendekatan 
**empatik, non-judgmental, dan santai**.

> ⚠️ **Disclaimer:** Bot ini BUKAN pengganti psikolog/psikiater. Untuk kondisi 
> berat, segera hubungi profesional di **119 ext 8**.

---

## ✨ Fitur Utama

- 💬 **Natural conversation** dengan bahasa santai remaja (aku-kamu, bahasa gaul ringan)
- 🧠 **Memory percakapan** — bot ingat konteks chat dalam satu sesi
- 🚨 **Crisis detection** — deteksi kata kunci self-harm, auto-tampilkan hotline darurat
- 🎯 **Rekomendasi aktivitas** berdasarkan mood yang dipilih user
- 🎨 **UI clean** dengan Streamlit + custom CSS
- 🔒 **Aman** — API key disimpan di `.env`, tidak di-commit

---

## 🛠️ Tech Stack

| Komponen | Teknologi |
|----------|-----------|
| LLM | Google Gemini 1.5 Flash |
| Framework UI | Streamlit |
| Bahasa | Python 3.10+ |
| Config | python-dotenv |

---

## 🚀 Cara Menjalankan

### 1. Clone repository
```bash
git clone https://github.com/febyvica/konsulkita-chatbot.git
cd konsulkita-chatbot