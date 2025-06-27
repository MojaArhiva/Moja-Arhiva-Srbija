import streamlit as st
import os
import base64

# Logo
st.set_page_config(page_title="Moja Arhiva", layout="centered")
st.image("assets/logo.png", width=150)
st.title("📲 Moja Arhiva – Digitalna dokumentacija")

# Menu
menu = [
    "📁 Lična dokumenta",
    "🏡 Nekretnine i stanovanje",
    "🚗 Vozila",
    "📚 Obrazovanje",
    "🏥 Zdravstveni dokumenti",
    "👨‍👩‍👧‍👦 Porodični dokumenti",
    "🛂 Lična karta i pasoš"
]
choice = st.sidebar.selectbox("Izaberite kategoriju", menu)

# Normalisation du nom de dossier
folder_name = choice.split(" ", 1)[-1]
folder_path = os.path.join("uploaded_docs", folder_name)
os.makedirs(folder_path, exist_ok=True)

# Upload de document
st.subheader(f"📤 Dodajte dokument u: {choice}")
uploaded_file = st.file_uploader("Izaberite dokument (PDF, PNG, JPG)", type=["pdf", "png", "jpg", "jpeg"])
if uploaded_file is not None:
    save_path = os.path.join(folder_path, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ Dokument uspešno sačuvan: {uploaded_file.name}")

# Liste des fichiers enregistrés
files = os.listdir(folder_path)
if files:
    st.subheader("📂 Vaši sačuvani dokumenti")
    selected_doc = st.selectbox("Izaberite dokument za pregled", files)
    doc_path = os.path.join(folder_path, selected_doc)

    # Aperçu selon le type
    st.subheader("🔍 Pregled dokumenta")
    if selected_doc.endswith((".png", ".jpg", ".jpeg")):
        st.image(doc_path, caption=selected_doc, use_column_width=True)

    elif selected_doc.endswith(".pdf"):
        with open(doc_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Pregled ovog tipa dokumenta nije podržan.")
else:
    st.info("📭 Još uvek nema dokumenata u ovoj kategoriji.")
