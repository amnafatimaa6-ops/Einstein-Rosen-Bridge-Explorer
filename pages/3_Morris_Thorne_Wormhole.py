import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Morris-Thorne Wormhole",
    page_icon="🌀",
    layout="wide"
)

st.title("🌀 Morris-Thorne Wormhole Explorer")

st.markdown("""
Interactive visualization of a traversable Morris-Thorne wormhole.

Everything below is generated mathematically in real time.
""")

###############################################
# Sidebar
###############################################

st.sidebar.header("Geometry")

throat = st.sidebar.slider(
    "Throat Radius",
    1.0,
    10.0,
    2.0,
    0.1
)

r_max = st.sidebar.slider(
    "Maximum Radius",
    5.0,
    30.0,
    15.0,
    0.5
)

resolution = st.sidebar.slider(
    "Resolution",
    80,
    300,
    180,
    10
)

###############################################

st.sidebar.header("Camera")

distance = st.sidebar.slider(
    "Camera Distance",
    2.0,
    10.0,
    4.0
)

elevation = st.sidebar.slider(
    "Elevation",
    -90,
    90,
    25
)

azimuth = st.sidebar.slider(
    "Azimuth",
    0,
    360,
    45
)

###############################################

st.sidebar.header("Appearance")

opacity = st.sidebar.slider(
    "Opacity",
    0.2,
    1.0,
    1.0
)

colorscale = st.sidebar.selectbox(

    "Colour Map",

    [

        "Viridis",
        "Turbo",
        "Inferno",
        "Plasma",
        "IceFire",
        "Cividis"

    ]

)

wireframe = st.sidebar.checkbox(
    "Wireframe",
    False
)

###############################################
# Geometry
###############################################

r = np.linspace(
    throat,
    r_max,
    resolution
)

theta = np.linspace(
    0,
    2*np.pi,
    resolution
)

R, T = np.meshgrid(
    r,
    theta
)

X = R*np.cos(T)

Y = R*np.sin(T)

Z = throat*np.arccosh(R/throat)

###############################################
# Figure
###############################################

fig = go.Figure()

fig.add_surface(

    x=X,
    y=Y,
    z=Z,

    colorscale=colorscale,

    opacity=opacity,

    showscale=False

)

fig.add_surface(

    x=X,
    y=Y,
    z=-Z,

    colorscale=colorscale,

    opacity=opacity,

    showscale=False

)

###############################################
# Wireframe
###############################################

if wireframe:

    step = 8

    for i in range(0, resolution, step):

        fig.add_trace(

            go.Scatter3d(

                x=X[i],

                y=Y[i],

                z=Z[i],

                mode="lines",

                line=dict(
                    color="white",
                    width=2
                ),

                showlegend=False

            )

        )

        fig.add_trace(

            go.Scatter3d(

                x=X[i],

                y=Y[i],

                z=-Z[i],

                mode="lines",

                line=dict(
                    color="white",
                    width=2
                ),

                showlegend=False

            )

        )

###############################################
# Camera
###############################################

e = np.radians(elevation)

a = np.radians(azimuth)

camera = dict(

    eye=dict(

        x=distance*np.cos(e)*np.cos(a),

        y=distance*np.cos(e)*np.sin(a),

        z=distance*np.sin(e)

    )

)

###############################################

fig.update_layout(

    title="Traversable Morris-Thorne Wormhole",

    paper_bgcolor="black",

    plot_bgcolor="black",

    margin=dict(
        l=0,
        r=0,
        t=40,
        b=0
    ),

    scene=dict(

        camera=camera,

        aspectmode="data",

        xaxis=dict(
            backgroundcolor="black"
        ),

        yaxis=dict(
            backgroundcolor="black"
        ),

        zaxis=dict(
            backgroundcolor="black"
        )

    )

)

st.plotly_chart(
    fig,
    use_container_width=True
)

###############################################
# Physics Panel
###############################################

col1, col2, col3 = st.columns(3)

col1.metric(
    "Throat Radius",
    f"{throat:.2f}"
)

col2.metric(
    "Maximum Radius",
    f"{r_max:.2f}"
)

col3.metric(
    "Mesh Resolution",
    resolution
)

###############################################

with st.expander("About Morris-Thorne Wormholes"):

    st.markdown("""

A Morris-Thorne wormhole is a hypothetical traversable
wormhole proposed in 1988.

Unlike the Einstein-Rosen bridge,
it does not collapse immediately and,
in theory,
could allow travel between two distant regions
of spacetime if supported by exotic matter.

This visualization uses the embedding surface

z(r)=±b₀ arccosh(r/b₀)

where b₀ represents the throat radius.

Move the sliders to explore how the
wormhole geometry changes.

""")
