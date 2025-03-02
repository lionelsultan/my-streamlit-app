import streamlit as st

st.set_page_config(
    page_title="Site personnel - Lionel Sultan",
    page_icon="🚀",
    layout="wide"
)

st.sidebar.image("assets/photo.png", width=150)
st.sidebar.markdown("### Navigation")
st.sidebar.info("Utilisez le menu en haut à gauche pour naviguer entre les pages.")
st.title("Bienvenue sur mon Showcase")
st.write("""
Cette application présente mes compétences, mes projets et mes informations de contact de manière interactive.  
Utilisez le menu de navigation pour explorer le contenu.
""")
