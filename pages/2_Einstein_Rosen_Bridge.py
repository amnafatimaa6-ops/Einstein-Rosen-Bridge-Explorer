import streamlit as st

from utils.plotting import create_bridge

st.set_page_config(
    page_title="Einstein-Rosen Bridge",
    layout="wide"
)

st.title("🌌 Einstein-Rosen Bridge Explorer")

st.markdown("""
Interactively explore the geometry of an Einstein-Rosen Bridge.

Rotate, zoom, slice and inspect the wormhole in real time.
""")

##################################################
# Sidebar
##################################################

st.sidebar.header("Physics")

mass = st.sidebar.slider(
    "Black Hole Mass",
    min_value=1.0,
    max_value=20.0,
    value=2.0,
    step=0.1
)

##################################################

st.sidebar.header("Camera")

camera_distance = st.sidebar.slider(
    "Camera Distance",
    2.0,
    10.0,
    4.0,
    0.1
)

camera_elevation = st.sidebar.slider(
    "Elevation",
    -90,
    90,
    30
)

camera_azimuth = st.sidebar.slider(
    "Azimuth",
    0,
    360,
    45
)

##################################################

st.sidebar.header("Appearance")

opacity = st.sidebar.slider(
    "Opacity",
    0.2,
    1.0,
    1.0,
    0.05
)

colorscale = st.sidebar.selectbox(
    "Colour Map",
    [
        "Viridis",
        "Plasma",
        "Turbo",
        "Inferno",
        "Cividis",
        "IceFire"
    ]
)

wireframe = st.sidebar.checkbox(
    "Wireframe",
    False
)

show_axes = st.sidebar.checkbox(
    "Show Axes",
    True
)

##################################################

st.sidebar.header("Cross Section")

slice_type = st.sidebar.selectbox(

    "Slice Type",

    [

        "None",

        "Horizontal",

        "Vertical X",

        "Vertical Y",

        "Cylinder",

        "Wedge"

    ]

)

slice_value = st.sidebar.slider(

    "Slice Position",

    -10.0,

    10.0,

    0.0,

    0.1

)

##################################################

st.sidebar.header("Animation")

auto_rotate = st.sidebar.checkbox(
    "Auto Rotate",
    False
)

rotation_speed = st.sidebar.slider(
    "Rotation Speed",
    1,
    10,
    3
)

##################################################

fig = create_bridge(

    mass=mass,

    distance=camera_distance,

    elevation=camera_elevation,

    azimuth=camera_azimuth,

    opacity=opacity,

    colorscale=colorscale,

    wireframe=wireframe,

    show_axes=show_axes,

    slice_type=slice_type,

    slice_value=slice_value,

    auto_rotate=auto_rotate,

    rotation_speed=rotation_speed

)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={
        "displaylogo": False,
        "scrollZoom": True
    }
)

##################################################

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Mass",
        f"{mass:.2f}"
    )

with col2:
    st.metric(
        "Schwarzschild Radius",
        f"{2*mass:.2f}"
    )

with col3:
    st.metric(
        "Slice",
        slice_type
    )

##################################################

with st.expander("About Einstein-Rosen Bridges"):

    st.markdown("""

An Einstein-Rosen Bridge is a solution of Einstein's field equations
connecting two asymptotically flat regions of spacetime.

This application visualizes the embedding surface of the
Schwarzschild geometry.

Features include:

- Interactive 3D rotation
- Live slicing
- Adjustable black hole mass
- Camera control
- Wireframe mode
- Multiple colour maps
- Real-time rendering

Future versions will include:

- Particle trajectories
- Photon geodesics
- Fly-through animation
- Morris-Thorne comparison
- Curvature heat maps
- Gravitational lensing
- Event horizon rendering

""")
