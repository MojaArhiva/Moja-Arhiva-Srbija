# Affichage en aperçu si le fichier est image ou PDF
st.subheader("🔍 Pregled dokumenta")

if files:
    selected_doc = st.selectbox("Izaberite dokument za pregled", files)

    doc_path = os.path.join(selected_folder, selected_doc)

    if selected_doc.endswith((".png", ".jpg", ".jpeg")):
        st.image(doc_path, caption=selected_doc, use_column_width=True)
    elif selected_doc.endswith(".pdf"):
        with open(doc_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
            st.download_button(label="📥 Preuzmi PDF", data=PDFbyte, file_name=selected_doc, mime='application/pdf')
            st.markdown(f"📝 **Naziv fajla** : {selected_doc}")
            st.markdown("⚠️ Direktan pregled PDF fajla u browser-u nije još podržan.")
    else:
        st.warning("⚠️ Pregled ovog tipa dokumenta nije podržan.")
