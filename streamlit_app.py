import streamlit as st

# Set judul aplikasi
st.title("Mini Game Kimia")

# Simpan status aplikasi dengan session_state
if "step" not in st.session_state:
    st.session_state.step = "start"
if "topik" not in st.session_state:
    st.session_state.topik = ""

# Fungsi untuk reset ke awal
def reset():
    st.session_state.step = "start"
    st.session_state.topik = ""

# Tampilan awal: tombol Start
if st.session_state.step == "start":
    if st.button("Start"):
        st.session_state.step = "pilih_topik"

# Langkah kedua: pilih topik organik/anorganik
elif st.session_state.step == "pilih_topik":
    st.write("Pilih topik:")
    col1, col2 = st.columns(2)
