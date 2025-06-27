import streamlit as st
from PIL import Image

st.set_page_config(page_title='Moja Arhiva', layout='centered')

st.image('assets/logo.png', width=150)
st.title("Moja Arhiva 🇷🇸")
st.subheader("Digitalna arhiva vaših ličnih dokumenata")

menu = ["📁 Lična dokumenta", "🏡 Nekretnine i stanovanje", "🚗 Vozila", "📚 Obrazovanje", "🏥 Zdravstveni dokumenti", "👨‍👩‍👧‍👦 Porodični dokumenti"]
choice = st.sidebar.selectbox("Izaberite kategoriju", menu)

if choice == "📁 Lična dokumenta":
    st.header("Lična dokumenta")
    st.markdown("- Lična karta\n- Pasoš\n- Vozačka dozvola\n- Izvod iz matične knjige rođenih")
elif choice == "🏡 Nekretnine i stanovanje":
    st.header("Nekretnine i stanovanje")
    st.markdown("- Ugovor o kupoprodaji\n- Ugovor o zakupu\n- Rešenje o porezu\n- Račun za struju")
elif choice == "🚗 Vozila":
    st.header("Vozila")
    st.markdown("- Saobraćajna dozvola\n- Polisa osiguranja\n- Tehnički pregled")
elif choice == "📚 Obrazovanje":
    st.header("Obrazovanje")
    st.markdown("- Diploma\n- Sertifikat jezika\n- Studentska kartica\n- Potvrda o pohađanju kursa")
elif choice == "🏥 Zdravstveni dokumenti":
    st.header("Zdravstveni dokumenti")
    st.markdown("- Zdravstvena knjižica\n- Potvrda o vakcinaciji\n- Recept za lekove\n- Specijalistički izveštaji")
elif choice == "👨‍👩‍👧‍👦 Porodični dokumenti":
    st.header("Porodični dokumenti")
    st.markdown("- Izvod iz matične knjige rođenih\n- Izvod iz matične knjige venčanih\n- Izvod iz matične knjige umrlih")
