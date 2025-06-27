import streamlit as st
import base64

st.set_page_config(page_title="Moja Arhiva", page_icon="📁")
st.image("assets/logo.png", width=150)
st.title("📁 Moja Arhiva – Digitalni arhiv")

def afficher_apercu_et_telechargement(uploaded_file):
    if uploaded_file is not None:
        pdf_bytes = uploaded_file.read()
        try:
            base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
            st.download_button("⬇️ Preuzmi dokument", data=pdf_bytes, file_name=uploaded_file.name, mime="application/pdf")
        except Exception as e:
            st.error("Greška pri prikazu dokumenta: " + str(e))

# Menu
menu = [
    "📁 Lična dokumenta",
    "🏡 Nekretnine i stanovanje",
    "🚗 Vozila",
    "📚 Obrazovanje",
    "🏥 Zdravstveni dokumenti",
    "👨‍👩‍👧‍👦 Porodični dokumenti"
]
choice = st.sidebar.selectbox("📂 Izaberite kategoriju", menu)

if choice == "📁 Lična dokumenta":
    st.subheader("📁 Lična dokumenta")
    st.markdown("- 📇 Lična karta\n- 🛂 Pasoš\n- 🧾 Izvod iz matične knjige rođenih\n- 🚘 Vozačka dozvola")
    uploaded_file = st.file_uploader("📤 Učitaj PDF dokument", type=["pdf"])
    afficher_apercu_et_telechargement(uploaded_file)

elif choice == "🏡 Nekretnine i stanovanje":
    st.subheader("🏡 Nekretnine i stanovanje")
    st.markdown("- 🏠 Ugovor o kupoprodaji\n- 🗝️ Ugovor o zakupu\n- 💰 Rešenje o porezu\n- ⚡ Račun za struju")
    uploaded_file = st.file_uploader("📤 Učitaj PDF dokument", type=["pdf"])
    afficher_apercu_et_telechargement(uploaded_file)

elif choice == "🚗 Vozila":
    st.subheader("🚗 Vozila")
    st.markdown("- 🚘 Saobraćajna dozvola\n- 📑 Polisa osiguranja\n- 🧾 Potvrda o registraciji")
    uploaded_file = st.file_uploader("📤 Učitaj PDF dokument", type=["pdf"])
    afficher_apercu_et_telechargement(uploaded_file)

elif choice == "📚 Obrazovanje":
    st.subheader("📚 Obrazovanje")
    st.markdown("- 🎓 Diploma\n- 📜 Sertifikat jezika\n- 🧾 Potvrda o pohađanju kursa\n- 🪪 Studentska kartica")
    uploaded_file = st.file_uploader("📤 Učitaj PDF dokument", type=["pdf"])
    afficher_apercu_et_telechargement(uploaded_file)

elif choice == "🏥 Zdravstveni dokumenti":
    st.subheader("🏥 Zdravstveni dokumenti")
    st.markdown("- 💳 Zdravstvena knjižica\n- 💉 Potvrda o vakcinaciji\n- 🏥 Otpusna lista\n- 💊 Recept\n- 📄 Specijalistički izveštaj")
    uploaded_file = st.file_uploader("📤 Učitaj PDF dokument", type=["pdf"])
    afficher_apercu_et_telechargement(uploaded_file)

elif choice == "👨‍👩‍👧‍👦 Porodični dokumenti":
    st.subheader("👨‍👩‍👧‍👦 Porodični dokumenti")
    st.markdown("- 🍼 Izvod iz matične knjige rođenih\n- 💍 Izvod iz knjige venčanih\n- ⚰️ Izvod iz knjige umrlih")
    uploaded_file = st.file_uploader("📤 Učitaj PDF dokument", type=["pdf"])
    afficher_apercu_et_telechargement(uploaded_file)
