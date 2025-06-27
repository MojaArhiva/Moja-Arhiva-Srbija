import streamlit as st
import os

st.set_page_config(page_title="Moja Arhiva", page_icon="📁", layout="centered")

# Affichage du logo
st.image("assets/logo.png", width=150)

st.title("📂 Moja Arhiva")
st.markdown("Dobrodošli! Ovde možete sačuvati i organizovati sve vaše važne dokumente.")

# Création du dossier d'upload
os.makedirs("uploaded_docs", exist_ok=True)

# Formulaire d'upload
st.subheader("📎 Dodajte novi dokument")
uploaded_file = st.file_uploader("Izaberite fajl za otpremanje (PDF, JPEG, PNG...)", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    file_path = os.path.join("uploaded_docs", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ Dokument '{uploaded_file.name}' je uspešno sačuvan.")

# Liste des fichiers déjà uploadés
st.subheader("📄 Vaši dokumenti")
files = os.listdir("uploaded_docs")
if files:
    for file in files:
        st.markdown(f"📌 {file}")
else:
    st.markdown("Nema učitanih dokumenata još uvek.")
