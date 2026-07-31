import streamlit as st

st.set_page_config(
    page_title="Einstein-Rosen Bridge Explorer",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌌 Einstein-Rosen Bridge Explorer")

st.markdown("""
Welcome to the **Einstein-Rosen Bridge Explorer**.

This application allows you to:

- 🌌 Explore Einstein-Rosen Bridges
- 🌀 Compare Morris-Thorne Wormholes
- 📈 View Embedding Diagrams
- 🛰 Fly Around in 3D
- 📐 Study the Mathematics
- ⚖ Compare Different Wormhole Geometries

Use the sidebar to navigate.
""")

st.info("Select a page from the sidebar.")
