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





############################################################
# EMBEDDING PROFILE COMPARISON
############################################################

st.divider()

st.subheader("Embedding Profile Comparison")

profile = go.Figure()

############################################################

profile.add_trace(

    go.Scatter(

        x=r1,

        y=2*np.sqrt(rs*(r1-rs)),

        mode="lines",

        line=dict(

            color="cyan",

            width=4

        ),

        name="Einstein-Rosen"

    )

)

profile.add_trace(

    go.Scatter(

        x=r1,

        y=-2*np.sqrt(rs*(r1-rs)),

        mode="lines",

        line=dict(

            color="cyan",

            width=4

        ),

        showlegend=False

    )

)

############################################################

profile.add_trace(

    go.Scatter(

        x=r2,

        y=throat*np.arccosh(r2/throat),

        mode="lines",

        line=dict(

            color="gold",

            width=4

        ),

        name="Morris-Thorne"

    )

)

profile.add_trace(

    go.Scatter(

        x=r2,

        y=-throat*np.arccosh(r2/throat),

        mode="lines",

        line=dict(

            color="gold",

            width=4

        ),

        showlegend=False

    )

)

############################################################

profile.update_layout(

    paper_bgcolor="black",

    plot_bgcolor="black",

    font=dict(color="white"),

    title="Embedding Diagram Overlay",

    xaxis_title="Radial Coordinate",

    yaxis_title="Embedding Height"

)

st.plotly_chart(

    profile,

    use_container_width=True

)

############################################################
# COMPARISON TABLE
############################################################

st.subheader("Comparison")

comparison = {

    "Property":[

        "Solution",

        "Traversable",

        "Collapse",

        "Event Horizon",

        "Requires Exotic Matter",

        "Stable",

        "Discovered",

        "Main Purpose"

    ],

    "Einstein-Rosen":[

        "Schwarzschild",

        "No",

        "Yes",

        "Yes",

        "No",

        "No",

        "1935",

        "Black Hole Geometry"

    ],

    "Morris-Thorne":[

        "Traversable Metric",

        "Yes",

        "No (Idealised)",

        "No",

        "Yes",

        "Theoretical",

        "1988",

        "Interstellar Travel"

    ]

}

st.table(comparison)

############################################################
# METRICS
############################################################

st.subheader("Current Parameters")

c1,c2,c3,c4 = st.columns(4)

c1.metric(

    "Mass",

    f"{mass:.2f}"

)

c2.metric(

    "Schwarzschild Radius",

    f"{rs:.2f}"

)

c3.metric(

    "Throat Radius",

    f"{throat:.2f}"

)

c4.metric(

    "Resolution",

    resolution

)

############################################################
# PHYSICS SUMMARY
############################################################

st.subheader("Key Differences")

st.success("""

Einstein-Rosen Bridge

• Natural solution of General Relativity

• Connects two asymptotically flat universes

• Contains an event horizon

• Pinches off before traversal is possible

""")

st.info("""

Morris-Thorne Wormhole

• Artificial traversable geometry

• No event horizon

• Remains open in the idealised solution

• Requires exotic matter with negative energy density

""")

############################################################
# EQUATIONS
############################################################

with st.expander("Mathematics"):

    st.markdown(r"""

### Einstein–Rosen Bridge

Embedding surface

\[
z(r)=2\sqrt{r_s(r-r_s)}
\]

---

Schwarzschild Metric

\[
ds^2=
-\left(1-\frac{2GM}{rc^2}\right)c^2dt^2
+
\left(1-\frac{2GM}{rc^2}\right)^{-1}dr^2
+r^2d\Omega^2
\]

---

### Morris–Thorne Metric

\[
ds^2=
-e^{2\Phi(r)}dt^2
+
\frac{dr^2}
{1-\frac{b(r)}{r}}
+
r^2d\Omega^2
\]

where

- \(\Phi(r)\) is the redshift function

- \(b(r)\) is the shape function

""")

############################################################
# FINAL SUMMARY
############################################################

st.divider()

st.markdown("""
### Interpretation

Although both geometries resemble wormholes in embedding diagrams,
their physical properties are very different.

- **Einstein–Rosen Bridge:** arises naturally from the Schwarzschild solution but is not traversable because it collapses too quickly.

- **Morris–Thorne Wormhole:** is a theoretical traversable wormhole that avoids an event horizon but requires exotic matter to remain open.

Embedding diagrams help visualize the spatial curvature, but they do not represent the full four-dimensional spacetime.
""")

        use_container_width=True

    )
