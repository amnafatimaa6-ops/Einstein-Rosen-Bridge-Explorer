"""
2_Einstein_Rosen_Bridge.py

Interactive Einstein-Rosen Bridge page.
"""

import streamlit as st
import numpy as np

from utils.plotting import create_bridge
from utils.metrics import schwarzschild_radius



st.set_page_config(

    page_title="Einstein-Rosen Bridge",

    page_icon="🌌",

    layout="wide"

)



st.title(
    "🌌 Einstein-Rosen Bridge"
)


st.write(
"""
Explore the geometry of the Einstein-Rosen Bridge.

The bridge is generated mathematically using a
3D embedding surface, not a static image.
"""
)



############################################################
# SIDEBAR PARAMETERS
############################################################

st.sidebar.header(
    "Bridge Parameters"
)


throat_radius = st.sidebar.slider(

    "Throat Radius",

    min_value=0.5,

    max_value=10.0,

    value=2.0,

    step=0.5

)



length = st.sidebar.slider(

    "Bridge Length",

    min_value=5,

    max_value=30,

    value=10

)



resolution = st.sidebar.slider(

    "Mesh Resolution",

    min_value=50,

    max_value=300,

    value=150

)



############################################################
# MASS CALCULATOR
############################################################

mass = st.sidebar.number_input(

    "Black Hole Mass (Solar Masses)",

    min_value=0.1,

    value=1.0

)



rs = schwarzschild_radius(

    mass

)



st.sidebar.metric(

    "Schwarzschild Radius (m)",

    f"{rs:.3e}"

)



############################################################
# CREATE 3D BRIDGE
############################################################


fig = create_bridge(

    throat_radius=throat_radius,

    length=length,

    resolution=resolution,

    mass=mass

)



st.plotly_chart(

    fig,

    use_container_width=True

)



############################################################
# PHYSICS INFORMATION
############################################################


col1,col2,col3 = st.columns(3)


with col1:

    st.metric(

        "Throat Radius",

        f"{throat_radius}"

    )


with col2:

    st.metric(

        "Grid Resolution",

        resolution

    )


with col3:

    st.metric(

        "Model",

        "Einstein-Rosen"

    )



st.subheader(
    "Physics Notes"
)


st.markdown(
"""
### Einstein-Rosen Bridge

The Einstein-Rosen bridge comes from the maximally extended
Schwarzschild solution of General Relativity.

It represents a mathematical connection between two
regions of spacetime.

Important:

- It is a theoretical solution.
- It is not a traversable wormhole.
- The throat collapses too quickly for passage.

The visualization above shows the spatial embedding geometry.
"""
)
