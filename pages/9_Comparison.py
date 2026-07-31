import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Wormhole Comparison",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ Einstein-Rosen vs Morris-Thorne")

st.markdown("""
Compare two of the most famous wormhole geometries
side-by-side.

The left figure displays the Einstein-Rosen Bridge
while the right figure shows a traversable
Morris-Thorne Wormhole.
""")

###########################################################
# SIDEBAR
###########################################################

st.sidebar.header("Geometry")

mass = st.sidebar.slider(
    "Black Hole Mass",
    1.0,
    10.0,
    2.0,
    0.1
)

throat = st.sidebar.slider(
    "Throat Radius",
    1.0,
    10.0,
    2.0,
    0.1
)

resolution = st.sidebar.slider(
    "Resolution",
    80,
    250,
    150,
    10
)

rmax = st.sidebar.slider(
    "Maximum Radius",
    5.0,
    25.0,
    15.0,
    0.5
)

colorscale = st.sidebar.selectbox(
    "Colour Map",
    [
        "Viridis",
        "Plasma",
        "Turbo",
        "Inferno",
        "Cividis"
    ]
)

wireframe = st.sidebar.checkbox(
    "Wireframe",
    False
)

###########################################################
# EINSTEIN-ROSEN GEOMETRY
###########################################################

rs = 2 * mass

r1 = np.linspace(
    rs + 0.01,
    rmax,
    resolution
)

theta = np.linspace(
    0,
    2*np.pi,
    resolution
)

R1, T1 = np.meshgrid(
    r1,
    theta
)

X1 = R1*np.cos(T1)
Y1 = R1*np.sin(T1)

Z1 = 2*np.sqrt(
    rs*(R1-rs)
)

###########################################################
# MORRIS-THORNE GEOMETRY
###########################################################

r2 = np.linspace(
    throat,
    rmax,
    resolution
)

R2, T2 = np.meshgrid(
    r2,
    theta
)

X2 = R2*np.cos(T2)
Y2 = R2*np.sin(T2)

Z2 = throat*np.arccosh(
    R2/throat
)

###########################################################
# FIGURE 1
###########################################################

fig_er = go.Figure()

fig_er.add_surface(

    x=X1,
    y=Y1,
    z=Z1,

    colorscale=colorscale,
    showscale=False

)

fig_er.add_surface(

    x=X1,
    y=Y1,
    z=-Z1,

    colorscale=colorscale,
    showscale=False

)

###########################################################
# FIGURE 2
###########################################################

fig_mt = go.Figure()

fig_mt.add_surface(

    x=X2,
    y=Y2,
    z=Z2,

    colorscale=colorscale,
    showscale=False

)

fig_mt.add_surface(

    x=X2,
    y=Y2,
    z=-Z2,

    colorscale=colorscale,
    showscale=False

)

###########################################################
# WIREFRAME
###########################################################

if wireframe:

    step = 8

    for i in range(0,resolution,step):

        fig_er.add_trace(

            go.Scatter3d(

                x=X1[i],
                y=Y1[i],
                z=Z1[i],

                mode="lines",

                line=dict(
                    color="white",
                    width=2
                ),

                showlegend=False

            )

        )

        fig_mt.add_trace(

            go.Scatter3d(

                x=X2[i],
                y=Y2[i],
                z=Z2[i],

                mode="lines",

                line=dict(
                    color="white",
                    width=2
                ),

                showlegend=False

            )

        )

###########################################################
# DISPLAY
###########################################################

left,right = st.columns(2)

with left:

    fig_er.update_layout(

        title="Einstein-Rosen Bridge",

        paper_bgcolor="black",

        plot_bgcolor="black",

        margin=dict(l=0,r=0,t=40,b=0)

    )

    st.plotly_chart(

        fig_er,

        use_container_width=True

    )

with right:

    fig_mt.update_layout(

        title="Morris-Thorne Wormhole",

        paper_bgcolor="black",

        plot_bgcolor="black",

        margin=dict(l=0,r=0,t=40,b=0)

    )

    st.plotly_chart(

        fig_mt,

        use_container_width=True

    )
