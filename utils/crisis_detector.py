"""
Deteksi kata kunci krisis pada pesan user.
Jika terdeteksi, tampilkan hotline darurat.
"""

CRISIS_KEYWORDS = [
    "bunuh diri", "mengakhiri hidup", "self harm", "nyakitin diri",
    "pengen mati", "gak mau hidup", "cutting", "overdosis",
    "injury", "menyakiti diri", "akhiri hidup", "ingin mati",
    "pengen bunuh diri", "mau mati"
]


def detect_crisis(text: str) -> bool:
    """Return True jika pesan mengandung kata kunci krisis."""
    if not text:
        return False
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in CRISIS_KEYWORDS)


CRISIS_RESPONSE = """
🚨 **Aku peduli banget sama kamu.** Yang kamu rasain berat, tapi kamu gak sendiri.

**Tolong hubungi segera:**
- 📞 **Hotline Kemenkes: 119 ext 8**
- 📞 **LSM Jangan Bunuh Diri: 021-9696 9293**
- 🌐 **Into The Light Indonesia:** [bit.ly/intothelight](https://bit.ly/intothelight)

**Langkah darurat:**
1. Jangan sendirian — cari orang terdekat yang kamu percaya
2. Cerita ke orang dewasa (ortu, guru BK, kakak, atau teman dekat)
3. Kalau perlu, hubungi layanan darurat **112**

Kamu berharga. Perasaan ini akan lewat. ❤️
"""