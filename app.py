"""
Einstein-Rosen Bridge Explorer

Main Streamlit application.
"""

import streamlit as st


st.set_page_config(

    page_title="Einstein-Rosen Bridge Explorer",

    page_icon="🌌",

    layout="wide"

)



st.title(
    "🌌 Einstein-Rosen Bridge Explorer"
)


st.markdown(
"""
## Interactive General Relativity Laboratory

Explore:

- Einstein-Rosen bridges
- Morris-Thorne wormholes
- Black holes
- Event horizons
- Gravitational lensing
- Geodesics
- Spacetime curvature

Use the sidebar pages to begin.
"""
)



col1,col2,col3=st.columns(3)


with col1:

    st.metric(

        "Models",

        "10+"

    )


with col2:

    st.metric(

        "3D Engine",

        "PyVista"

    )


with col3:

    st.metric(

        "Physics",

        "General Relativity"

    )



st.info(
"""
Navigate through the pages:

1. Einstein-Rosen Bridge
2. Morris-Thorne Wormhole
3. Embedding Diagrams
4. 3D Explorer
5. Geodesics
6. Event Horizon
7. Gravitational Lensing

"""
)
