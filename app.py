import streamlit as st

st.set_page_config(page_title="Showcase - Lionel Sultan",
                   page_icon="🚀", layout="wide")

st.sidebar.image("assets/photo.png", width=150)
st.sidebar.title("Menu")
tab1, tab2, tab3, tab4 = st.tabs(
    ["🏠 Accueil", "🛠 Compétences", "📂 Projets", "📩 Contact"])

with tab1:
    st.header("🚀 Bienvenue sur mon Showcase")
    st.write("Découvrez mon parcours et mes réalisations.")

with tab2:
    st.header("🛠 Compétences")
    st.write("Liste détaillée de mes compétences techniques et managériales.")

with tab3:
    st.header("📂 Projets")
    st.write("Présentation de mes projets marquants et études de cas.")

with tab4:
    st.header("📩 Contact")
    st.write("Retrouvez-moi sur LinkedIn, GitHub ou contactez-moi par e-mail.")
