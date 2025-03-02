import streamlit as st
import streamlit.components.v1 as components

st.title("📂 Projets")

st.markdown("### Mes Projets Clés")
st.write("""
**Développement d’une application ARKit**  
- Création d’une application immersive sur MacBook Pro M4 Max.
""")

st.markdown("### Vidéo de présentation")
# Intégration d'une vidéo YouTube (remplacez le lien par celui de votre vidéo)
components.iframe("https://www.youtube.com/embed/XYZ123", height=315)
