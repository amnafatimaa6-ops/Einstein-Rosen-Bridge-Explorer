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
import pyvista as pv

from stpyvista import stpyvista


from utils.wormholes import einstein_rosen_bridge
from utils.event_horizon import create_event_horizon
from utils.stars import generate_stars
from utils.slicing import slice_mesh
from utils.metrics import throat_metrics



############################################################
# PAGE CONFIG
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
# CONTROLS
############################################################

st.sidebar.header(
    "Simulation Controls"
)



throat_radius = st.sidebar.slider(

    "Throat radius",

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

    "Show Stars",

    True

)



enable_slice = st.sidebar.checkbox(

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

    off_screen=True,

    window_size=(900,700)

)



############################################################
# WORMHOLE
############################################################

wormhole = einstein_rosen_bridge(

    throat_radius=throat_radius,

    length=bridge_length,

    resolution=resolution

)



plotter.add_mesh(

    wormhole,

    color="cyan",

    opacity=0.85,

    smooth_shading=True

)



############################################################
# SLICE
############################################################

if enable_slice:


    sliced = slice_mesh(

        wormhole,

        position=slice_position

    )


    plotter.add_mesh(

        sliced,

        color="yellow"

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

        opacity=0.95

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

        point_size=2

    )



############################################################
# LIGHTING
############################################################

try:

    light = pv.Light()

    light.position = (

        20,

        20,

        20

    )

    light.intensity = 1.5


    plotter.add_light(

        light

    )


except Exception:

    pass



############################################################
# CAMERA
############################################################

plotter.camera_position = [

    (

        35,

        35,

        25

    ),

    (

        0,

        0,

        0

    ),

    (

        0,

        0,

        1

    )

]



############################################################
# PROJECTION FIX
############################################################

try:

    plotter.enable_parallel_projection(

        False

    )

except Exception:

    pass



############################################################
# VIEW SETTINGS
############################################################

try:

    plotter.show_axes()

except Exception:

    pass



plotter.set_background(

    "black"

)



############################################################
# DISPLAY 3D VIEWER
############################################################

st.subheader(

    "🌌 3D Wormhole Simulation"

)



try:

    stpyvista(

        plotter

    )


except Exception as e:

    st.error(

        f"3D rendering failed: {e}"

    )



############################################################
# METRICS
############################################################

st.subheader(

    "Simulation Metrics"

)



metrics = throat_metrics(

    throat_radius,

    curvature=1/throat_radius

)



c1,c2,c3 = st.columns(3)



with c1:

    st.metric(

        "Throat Radius",

        f"{metrics['throat_radius']:.2f}"

    )



with c2:

    st.metric(

        "Curvature",

        f"{metrics['curvature']:.3f}"

    )



with c3:

    st.metric(

        "Model",

        "Einstein-Rosen"

    )



############################################################
# EXPORT
############################################################

st.subheader(

    "Export"

)



if st.button(

    "Capture Screenshot"

):

    try:

        plotter.screenshot(

            "wormhole.png"

        )


        st.success(

            "Screenshot created"

        )


    except Exception:

        st.warning(

            "Screenshot unavailable on cloud"

        )



############################################################
# DESCRIPTION
############################################################

st.markdown(
"""
## Physics

This simulation generates the geometry procedurally.

No image textures are used.

The visualization includes:

- Einstein-Rosen bridge geometry
- Event horizon
- Procedural star field
- Interactive 3D camera
- Spatial slicing

The model is based on General Relativity solutions.
"""
)
