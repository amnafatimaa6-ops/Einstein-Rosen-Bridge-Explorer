import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Embedding Diagrams",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Embedding Diagram Explorer")

st.markdown("""
Embedding diagrams provide a way to visualize the curvature of
space around a black hole or wormhole by embedding a curved
2-dimensional surface into ordinary 3-dimensional Euclidean space.
""")

#############################################################
# Sidebar
#############################################################

st.sidebar.header("Geometry")

geometry = st.sidebar.selectbox(
    "Geometry",
    [
        "Einstein-Rosen Bridge",
        "Morris-Thorne Wormhole"
    ]
)

#############################################################

mass = st.sidebar.slider(
    "Mass / Throat Radius",
    1.0,
    10.0,
    2.0,
    0.1
)

#############################################################

r_max = st.sidebar.slider(
    "Maximum Radius",
    5.0,
    30.0,
    15.0,
    0.5
)

#############################################################

resolution = st.sidebar.slider(
    "Resolution",
    100,
    350,
    220,
    10
)

#############################################################

diagram = st.sidebar.radio(
    "Diagram Type",
    [
        "2D Profile",
        "3D Surface",
        "Wireframe"
    ]
)

#############################################################
# Geometry
#############################################################

theta = np.linspace(
    0,
    2*np.pi,
    resolution
)

#############################################################

if geometry == "Einstein-Rosen Bridge":

    rs = 2 * mass

    r = np.linspace(
        rs + 0.01,
        r_max,
        resolution
    )

    z = 2*np.sqrt(
        rs*(r-rs)
    )

else:

    throat = mass

    r = np.linspace(
        throat,
        r_max,
        resolution
    )

    z = throat*np.arccosh(
        r/throat
    )

#############################################################
# 2D PROFILE
#############################################################

if diagram == "2D Profile":

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=r,

            y=z,

            mode="lines",

            line=dict(width=4)

        )

    )

    fig.add_trace(

        go.Scatter(

            x=r,

            y=-z,

            mode="lines",

            line=dict(width=4)

        )

    )

    fig.update_layout(

        title="Embedding Profile",

        xaxis_title="Radial Coordinate",

        yaxis_title="Embedding Height"

    )

#############################################################
# 3D SURFACE
#############################################################

elif diagram == "3D Surface":

    R, T = np.meshgrid(
        r,
        theta
    )

    X = R*np.cos(T)

    Y = R*np.sin(T)

    Z = np.tile(
        z,
        (resolution,1)
    )

    fig = go.Figure()

    fig.add_surface(

        x=X,

        y=Y,

        z=Z,

        colorscale="Viridis",

        showscale=False

    )

    fig.add_surface(

        x=X,

        y=Y,

        z=-Z,

        colorscale="Viridis",

        showscale=False

    )

#############################################################
# WIREFRAME
#############################################################

else:

    R, T = np.meshgrid(
        r,
        theta
    )

    X = R*np.cos(T)

    Y = R*np.sin(T)

    Z = np.tile(
        z,
        (resolution,1)
    )

    fig = go.Figure()

    step = 8

    for i in range(0, resolution, step):

        fig.add_trace(

            go.Scatter3d(

                x=X[i],

                y=Y[i],

                z=Z[i],

                mode="lines",

                line=dict(
                    color="cyan",
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
                    color="cyan",
                    width=2
                ),

                showlegend=False

            )

        )

#############################################################

fig.update_layout(

    paper_bgcolor="black",

    plot_bgcolor="black",

    margin=dict(
        l=0,
        r=0,
        t=40,
        b=0
    )

)

st.plotly_chart(
    fig,
    use_container_width=True
)

#############################################################
# Physics Panel
#############################################################

col1, col2, col3 = st.columns(3)

col1.metric(
    "Geometry",
    geometry
)

col2.metric(
    "Mass / Throat",
    f"{mass:.2f}"
)

col3.metric(
    "Resolution",
    resolution
)

#############################################################

with st.expander("Embedding Theory"):

    st.markdown("""

Embedding diagrams are mathematical tools used to visualize
curved spacetime.

Instead of displaying four-dimensional spacetime,
they show a curved two-dimensional slice embedded inside
three-dimensional Euclidean space.

For an Einstein-Rosen Bridge,

z(r)=2√(2M(r−2M))

For a Morris-Thorne wormhole,

z(r)=b₀ arccosh(r/b₀)

These diagrams help visualize how spacetime curves around
black holes and traversable wormholes.

""")
