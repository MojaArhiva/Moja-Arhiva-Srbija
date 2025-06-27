import streamlit as st
import os

st.set_page_config(page_title="Moja Arhiva", page_icon="📁", layout="centered")

# Affichage du logo
st.image("assets/logo.png", width=150)

st.title("📂 Moja Arhiva")
st.markdown("Dobrodošli! Ovde možete sačuvati i organizovati sve vaše važne dokumente.")

# Menu latéral mis à jour avec nouvelle catégorie
menu = [
    "📁 Lična dokumenta",
    "🪪 Lična karta i pasoš",
    "🏡 Nekretnine i stanovanje",
    "🚗 Vozila",
    "📚 Obrazovanje",
    "🏥 Zdravstveni dokumenti",
    "👨‍👩‍👧‍👦 Porodični dokumenti"
]
choice = st.sidebar.selectbox("Izaberite kategoriju", menu)

# Dictionnaire des dossiers associés
category_folders = {
    "📁 Lična dokumenta": "personal_docs",
    "🪪 Lična karta i pasoš": "id_passport_docs",
    "🏡 Nekretnine i stanovanje": "housing_docs",
    "🚗 Vozila": "vehicle_docs",
    "📚 Obrazovanje": "education_docs",
    "🏥 Zdravstveni dokumenti": "health_docs",
    "👨‍👩‍👧‍👦 Porodični dokumenti": "family_docs"
}
selected_folder = category_folders[choice]
os.makedirs(selected_folder, exist_ok=True)

# Formulaire d’upload
st.subheader(f"📎 Dodajte dokument za: {choice}")
uploaded_file = st.file_uploader("Izaberite fajl za otpremanje", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    file_path = os.path.join(selected_folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ Dokument '{uploaded_file.name}' je sačuvan u kategoriji '{choice}'.")

# Liste des documents par catégorie
st.subheader(f"📄 Dokumenti za kategoriju: {choice}")
files = os.listdir(selected_folder)
if files:
    for file in files:
        st.markdown(f"📌 {file}")
else:
    st.markdown("📭 Još uvek nema učitanih dokumenata.")
