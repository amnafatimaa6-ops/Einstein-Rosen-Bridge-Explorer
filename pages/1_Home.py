import streamlit as st

st.set_page_config(
    page_title="Einstein-Rosen Bridge Explorer",
    page_icon="🌌",
    layout="wide"
)

st.title("🌌 Einstein-Rosen Bridge Explorer")

st.markdown("""
# Interactive General Relativity Laboratory

Welcome to the **Einstein-Rosen Bridge Explorer**.

This project is an interactive computational physics application
for exploring wormholes and black hole geometries.

Everything displayed inside this application is generated
mathematically in real time using Python.

No images.

No videos.

Everything is computed live.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("🌌 Einstein-Rosen Bridge")

    st.write("""
- Interactive 3D Surface

- Rotate

- Zoom

- Slice

- Camera Control

- Variable Mass

- Event Horizon

- Wireframe Mode
""")

with col2:

    st.subheader("🌀 Morris-Thorne Wormhole")

    st.write("""
- Traversable Wormhole

- Adjustable Throat Radius

- Redshift Function

- Shape Function

- Comparison Mode

- 3D Interactive Rendering
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Physics Models",
        "2"
    )

with col2:

    st.metric(
        "Interactive Pages",
        "10+"
    )

with col3:

    st.metric(
        "3D Simulations",
        "Live"
    )

st.divider()

st.header("Available Modules")

modules = [

    "🌌 Einstein-Rosen Bridge",

    "🌀 Morris-Thorne Wormhole",

    "📈 Embedding Diagrams",

    "🛰️ 3D Explorer",

    "📐 Mathematics",

    "🌠 Gravitational Lensing",

    "🪐 Geodesic Simulator",

    "⚖ Wormhole Comparison",

    "🧮 Physics Calculator"

]

for module in modules:
    st.success(module)

st.divider()

st.header("Controls")

st.markdown("""
Every visualization supports:

- Mouse Rotation
- Zoom
- Pan
- Hover Information
- Camera Controls
- Live Parameter Updates
- Real-Time Rendering
""")

st.divider()

st.info("""
Use the navigation menu on the left to begin exploring.
""")
