import streamlit as st
import os
import base64

st.image('assets/logo.png', width=150)

st.title("📲 Moja Arhiva - Upravljanje dokumentima")

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

folder_mapping = {
    menu_item: menu_item.replace(" ", "_").replace("📁", "").replace("🏡", "").replace("🚗", "").replace("📚", "")
                         .replace("🏥", "").replace("👨‍👩‍👧‍👦", "").replace("🛂", "").strip()
    for menu_item in menu
}

selected_folder = os.path.join("uploaded_docs", folder_mapping[choice])
os.makedirs(selected_folder, exist_ok=True)

st.subheader("📤 Dodajte dokument")
uploaded_file = st.file_uploader("Izaberite dokument", type=["pdf", "png", "jpg", "jpeg"])
if uploaded_file is not None:
    with open(os.path.join(selected_folder, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ Dokument '{uploaded_file.name}' je uspešno sačuvan.")

files = os.listdir(selected_folder)
if files:
    st.subheader("📚 Vaši dokumenti")
    for file in files:
        st.write(f"- {file}")

    st.subheader("🔍 Pregled dokumenta")
    selected_doc = st.selectbox("Izaberite dokument za pregled", files)
    doc_path = os.path.join(selected_folder, selected_doc)

    if selected_doc.endswith((".png", ".jpg", ".jpeg")):
        st.image(doc_path, caption=selected_doc, use_column_width=True)
    elif selected_doc.endswith(".pdf"):
        with open(doc_path, "rb") as f:
            base64_pdf = base64.b64encode(f.re_
