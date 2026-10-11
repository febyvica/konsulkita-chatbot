"""
Rekomendasi aktivitas self-care berdasarkan mood user.
"""

RECOMMENDATIONS = {
    "stres": [
        "🧘 Coba 4-7-8 breathing: tarik napas 4 detik, tahan 7 detik, buang 8 detik",
        "🎧 Dengerin lo-fi playlist di Spotify atau YouTube",
        "📓 Tulis 3 hal yang bikin kamu bersyukur hari ini",
        "🚶 Jalan santai 10 menit tanpa HP",
    ],
    "sedih": [
        "🚶 Jalan kaki 15 menit di luar rumah, hirup udara segar",
        "🎬 Nonton film comfort favoritmu",
        "☎️ Telepon sahabat yang bikin kamu nyaman",
        "🍫 Makan camilan favorit (secukupnya)",
    ],
    "cemas": [
        "🌬️ Grounding 5-4-3-2-1: sebut 5 benda yang kamu lihat, 4 yang bisa disentuh, 3 yang didengar, 2 yang dicium, 1 yang dirasa",
        "🧩 Puzzle atau game ringan untuk alihkan fokus",
        "🛁 Mandi air hangat",
        "✍️ Tulis kekhawatiranmu di kertas, lalu robek",
    ],
    "capek": [
        "😴 Tidur 7-9 jam, hindari gadget 1 jam sebelum tidur",
        "🍵 Minum teh chamomile atau air hangat",
        "📵 Digital detox 2 jam",
        "🎵 Dengerin musik instrumental sambil rebahan",
    ],
    "marah": [
        "🏃 Olahraga ringan: lari, push-up, atau lompat tali",
        "💨 Tarik napas dalam 10x, buang perlahan",
        "📝 Tulis apa yang bikin marah, tanpa filter",
        "🚪 Jauhkan diri dulu dari sumber masalah",
    ],
    "senang": [
        "📸 Abadikan momen ini — foto atau tulis di jurnal",
        "💌 Kabari teman/orang tersayang tentang hal baikmu",
        "🎯 Manfaatkan mood bagus untuk hal produktif",
    ],
}


def get_recommendation(mood: str):
    """Return list rekomendasi sesuai mood."""
    if not mood:
        return ["💙 Istirahat cukup, minum air, dan lakukan hal kecil yang kamu suka."]

    mood_lower = mood.lower()
    for key in RECOMMENDATIONS:
        if key in mood_lower:
            return RECOMMENDATIONS[key]

    return ["💙 Istirahat cukup, minum air, dan lakukan hal kecil yang kamu suka."]