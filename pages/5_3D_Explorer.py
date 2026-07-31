"""
5_3D_Explorer.py

Interactive 3D Einstein-Rosen Bridge Explorer

Features:
- PyVista 3D rendering
- Wormhole geometry
- Event horizon
- Stars
- Camera controls
- Slicing
"""


import streamlit as st
import numpy as np
import pyvista as pv

from stpyvista import stpyvista


from utils.wormholes import (
    einstein_rosen_bridge
)

from utils.event_horizon import (
    create_event_horizon
)

from utils.stars import (
    generate_stars
)

from utils.slicing import (
    slice_mesh
)

from utils.metrics import (
    throat_metrics
)



############################################################
# STREAMLIT SETTINGS
############################################################

st.set_page_config(

    page_title="3D Wormhole Explorer",

    page_icon="🌌",

    layout="wide"

)



############################################################
# PYVISTA CLOUD SETTINGS
############################################################

pv.OFF_SCREEN = True


try:

    pv.global_theme.allow_empty_mesh = True

except Exception:

    pass



############################################################
# TITLE
############################################################

st.title(
    "🚀 Interactive 3D Wormhole Explorer"
)


st.write(
"""
Explore an Einstein-Rosen Bridge in true 3D.

Rotate  
Zoom  
Pan  
Inspect  

Modify parameters live.
"""
)



############################################################
# SIDEBAR CONTROLS
############################################################

st.sidebar.header(
    "Simulation Controls"
)



throat_radius = st.sidebar.slider(

    "Wormhole throat radius",

    1.0,

    10.0,

    3.0

)



bridge_length = st.sidebar.slider(

    "Bridge length",

    5.0,

    30.0,

    15.0

)



resolution = st.sidebar.slider(

    "Resolution",

    50,

    300,

    150

)



show_horizon = st.sidebar.checkbox(

    "Show Event Horizon",

    True

)



show_stars = st.sidebar.checkbox(

    "Show Star Field",

    True

)



slice_enabled = st.sidebar.checkbox(

    "Enable Slice",

    False

)



slice_position = st.sidebar.slider(

    "Slice position",

    -10.0,

    10.0,

    0.0

)



############################################################
# CREATE PLOTTER
############################################################

plotter = pv.Plotter(

    window_size=[900,700],

    off_screen=True

)



############################################################
# GENERATE WORMHOLE
############################################################


wormhole = einstein_rosen_bridge(

    throat_radius=throat_radius,

    length=bridge_length,

    resolution=resolution

)



plotter.add_mesh(

    wormhole,

    color="cyan",

    smooth_shading=True,

    opacity=0.85,

    name="wormhole"

)



############################################################
# SLICE CONTROL
############################################################


if slice_enabled:

    sliced = slice_mesh(

        wormhole,

        position=slice_position

    )


    plotter.add_mesh(

        sliced,

        color="yellow",

        name="slice"

    )








############################################################
# EVENT HORIZON
############################################################

if show_horizon:

    horizon = create_event_horizon(

        radius=throat_radius * 0.5,

        resolution=100

    )


    plotter.add_mesh(

        horizon,

        color="black",

        opacity=0.9,

        name="event_horizon"

    )



############################################################
# STAR FIELD
############################################################

if show_stars:

    stars = generate_stars(

        count=1500,

        radius=100

    )


    plotter.add_points(

        stars,

        color="white",

        point_size=2,

        name="stars"

    )



############################################################
# LIGHTING
############################################################

plotter.add_light(

    pv.Light(

        position=(20,20,20),

        focal_point=(0,0,0),

        intensity=1.5

    )

)



############################################################
# CAMERA SETUP
############################################################

plotter.camera_position = [

    (30,30,20),   # camera location

    (0,0,0),      # focus point

    (0,0,1)       # up direction

]



# Streamlit Cloud compatible projection

try:

    plotter.enable_parallel_projection(False)

except Exception:

    pass



############################################################
# AXES
############################################################

plotter.show_axes()



############################################################
# BACKGROUND
############################################################

plotter.set_background(

    "black"

)



############################################################
# DISPLAY
############################################################


st.subheader(
    "3D Simulation"
)


stpyvista(

    plotter,

    key="wormhole_viewer"

)



############################################################
# METRICS
############################################################


st.subheader(
    "Simulation Metrics"
)


metric_data = throat_metrics(

    throat_radius,

    curvature=1/throat_radius

)



col1,col2,col3 = st.columns(3)



with col1:

    st.metric(

        "Throat Radius",

        f"{metric_data['throat_radius']:.2f}"

    )



with col2:

    st.metric(

        "Curvature",

        f"{metric_data['curvature']:.3f}"

    )



with col3:

    st.metric(

        "Geometry",

        "Einstein-Rosen"

    )



############################################################
# EXPORT HOOK
############################################################

st.subheader(
    "Export"
)


if st.button(
    "Save Screenshot"
):

    try:

        plotter.screenshot(

            "wormhole_simulation.png"

        )


        st.success(

            "Screenshot saved"

        )


    except Exception as e:

        st.warning(

            "Screenshot unavailable on cloud renderer"

        )



############################################################
# INFORMATION
############################################################

st.markdown(
"""
### About this simulation

This viewer generates the wormhole procedurally.

No image textures are used.

The geometry is calculated from mathematical
spacetime models and rendered as a real 3D object.

Included:

- Einstein-Rosen bridge surface
- Event horizon visualization
- Procedural star field
- Interactive camera
- Spatial slicing
"""
)
