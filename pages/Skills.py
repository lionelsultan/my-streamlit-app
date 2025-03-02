import streamlit as st
import plotly.express as px
import pandas as pd

st.title("🔧 Compétences")

st.markdown("### Mes compétences techniques et managériales")
st.write("""
- **Agilité & SAFe RTE**
- **Gestion de produit**
- **Automatisation (Python, Jira)**
- **SQL & Business Intelligence (Power BI)**
- **Cybersécurité (ISO 27001)**
- **Cloud (GCP, AWS)**
- **SEO & IA**
- **Leadership & coaching**
""")

# Exemple de graphique interactif avec Plotly
data = pd.DataFrame({
    "Compétence": ["Python", "Agilité", "Cloud", "IA", "SEO"],
    "Niveau (%)": [90, 85, 80, 75, 70]
})
fig = px.bar(data, x="Compétence", y="Niveau (%)", color="Compétence", text="Niveau (%)")
st.plotly_chart(fig, use_container_width=True)
