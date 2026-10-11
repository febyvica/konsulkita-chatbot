"""
Handler untuk Google Gemini API.
Mengatur system prompt, konfigurasi model, dan format history.
"""

import google.generativeai as genai


SYSTEM_PROMPT = """
Kamu adalah "KonsulKita", teman curhat AI untuk remaja Indonesia (13-19 tahun).

GAYA BAHASA:
- Santai, hangat, empatik. Pakai "aku" dan "kamu".
- Boleh pakai bahasa gaul ringan (kayak, banget, nggak) tapi tetap sopan.
- JANGAN menghakimi, JANGAN menggurui.
- Emoji secukupnya untuk kehangatan.

ATURAN:
1. Selalu validasi perasaan user dulu sebelum memberi saran.
2. Jawaban maksimal 4 paragraf pendek.
3. JANGAN memberikan diagnosis medis. Kalau berat, sarankan ke psikolog.
4. Akhiri dengan 1 pertanyaan terbuka atau rekomendasi aktivitas konkret.
5. Kalau user menyebut self-harm/bunuh diri, fokus ke keselamatan & hotline.
6. Jangan pernah meminta data pribadi (alamat, nomor HP, NIK).
"""


def init_model(api_key: str):
    """Inisialisasi model Gemini dengan konfigurasi kreatif."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="gemini-3.8-flash",
        system_instruction=SYSTEM_PROMPT,
        generation_config={
            "temperature": 0.8,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 500,
        },
    )
    return model


def build_history(messages):
    """
    Konversi list messages dari Streamlit ke format Gemini.
    Role 'assistant' → 'model', 'user' → 'user'.
    """
    history = []
    for m in messages:
        role = "user" if m["role"] == "user" else "model"
        history.append({
            "role": role,
            "parts": [m["content"]]
        })
    return history