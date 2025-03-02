import streamlit as st

st.title("📩 Contact")

st.markdown("""
Si vous souhaitez en savoir plus sur mon parcours ou collaborer sur des projets innovants, n’hésitez pas à me contacter.

**Email** : [votre.email@example.com](mailto:votre.email@example.com)  
**LinkedIn** : [linkedin.com/in/votreprofil](https://www.linkedin.com/in/votreprofil)  
**GitHub** : [github.com/votreprofil](https://github.com/votreprofil)
""")

st.markdown("### Envoyez-moi un message")
with st.form("contact_form"):
    name = st.text_input("Votre nom")
    email = st.text_input("Votre email")
    message = st.text_area("Votre message")
    submitted = st.form_submit_button("Envoyer")
    if submitted:
        st.success("Merci pour votre message, je vous répondrai dans les meilleurs délais.")
