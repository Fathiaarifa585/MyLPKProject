import streamlit as st

st.set_page_config(page_title="Game Edukasi Uji Reaksi Kimia", layout="centered")

st.title("🧪 Game Edukasi: Uji Reaksi Kimia Anorganik dan Organik")
st.write("Selamat datang! Yuk uji pemahamanmu tentang uji reaksi kimia anorganik dan organik.")

# Pertanyaan dan Jawaban
questions = [
    {
        "question": "1. Apa hasil uji nyala dari ion Natrium (Na⁺)?",
        "options": ["Merah bata", "Kuning terang", "Hijau zamrud", "Ungu"],
        "answer": "Kuning terang"
    },
    {
        "question": "2. Zat organik dengan gugus -OH menunjukkan hasil positif pada uji...",
        "options": ["Tollens", "Fehling", "Benedict", "Naftol"],
        "answer": "Naftol"
    },
    {
        "question": "3. Ion Cu²⁺ jika direaksikan dengan larutan NaOH akan membentuk endapan berwarna...",
        "options": ["Putih", "Hijau", "Biru", "Merah"],
        "answer": "Biru"
    },
    {
        "question": "4. Uji Tollens digunakan untuk mengidentifikasi senyawa...",
        "options": ["Alkohol", "Aldehida", "Asam karboksilat", "Amina"],
        "answer": "Aldehida"
    }
]

# Skor
score = 0
user_answers = []

# Menampilkan pertanyaan
for i, q in enumerate(questions):
    st.subheader(q["question"])
    choice = st.radio(f"Jawaban Anda (Soal {i+1})", q["options"], key=i)
    user_answers.append(choice)
    if choice == q["answer"]:
        score += 1

# Tombol Submit
if st.button("Lihat Skor"):
    st.success(f"Skor Anda: {score} dari {len(questions)}")

    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            st.markdown(f"✅ *{q['question']}* - Benar")
        else:
            st.markdown(f"❌ *{q['question']}* - Salah. Jawaban benar: *{q['answer']}*")
