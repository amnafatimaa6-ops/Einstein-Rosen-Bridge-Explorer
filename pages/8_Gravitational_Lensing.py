import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Gravitational Lensing",
    page_icon="🌌",
    layout="wide"
)

st.title("🌌 Gravitational Lensing Simulator")

st.markdown("""
Observe how a massive black hole bends the paths of light
from distant background stars.

This simulator demonstrates the basic principles of
gravitational lensing using a simplified physical model.
""")

###########################################################
# SIDEBAR
###########################################################

st.sidebar.header("Lens")

mass = st.sidebar.slider(
    "Black Hole Mass (Solar Masses)",
    1.0,
    100.0,
    20.0,
    1.0
)

###########################################################

lens_strength = st.sidebar.slider(
    "Lens Strength",
    0.5,
    8.0,
    2.5,
    0.1
)

###########################################################

num_stars = st.sidebar.slider(
    "Number of Stars",
    200,
    5000,
    1500,
    100
)

###########################################################

show_einstein_ring = st.sidebar.checkbox(
    "Show Einstein Ring",
    True
)

show_grid = st.sidebar.checkbox(
    "Show Background Grid",
    False
)

###########################################################

seed = st.sidebar.number_input(
    "Random Seed",
    value=42
)

###########################################################
# RANDOM STAR FIELD
###########################################################

np.random.seed(seed)

x = np.random.uniform(-10, 10, num_stars)
y = np.random.uniform(-10, 10, num_stars)

###########################################################
# DISTANCE FROM BLACK HOLE
###########################################################

r = np.sqrt(x**2 + y**2)

r = np.maximum(r, 0.15)

###########################################################
# DEFLECTION
###########################################################

alpha = lens_strength / r

###########################################################
# DEFLECTED POSITIONS
###########################################################

x_deflected = x + alpha * (x / r)
y_deflected = y + alpha * (y / r)

###########################################################
# FIGURE
###########################################################

fig = go.Figure()

###########################################################
# ORIGINAL STARS
###########################################################

fig.add_trace(

    go.Scatter(

        x=x,

        y=y,

        mode="markers",

        marker=dict(

            size=2,

            color="gray"

        ),

        name="Original Stars",

        visible="legendonly"

    )

)

###########################################################
# DEFLECTED STARS
###########################################################

fig.add_trace(

    go.Scatter(

        x=x_deflected,

        y=y_deflected,

        mode="markers",

        marker=dict(

            size=3,

            color="white"

        ),

        name="Lensed Stars"

    )

)

###########################################################
# BLACK HOLE
###########################################################

fig.add_trace(

    go.Scatter(

        x=[0],

        y=[0],

        mode="markers",

        marker=dict(

            size=22,

            color="black",

            line=dict(

                color="white",

                width=2

            )

        ),

        name="Black Hole"

    )

)

###########################################################
# EINSTEIN RING
###########################################################

if show_einstein_ring:

    theta = np.linspace(
        0,
        2*np.pi,
        500
    )

    radius = np.sqrt(lens_strength)

    ring_x = radius*np.cos(theta)
    ring_y = radius*np.sin(theta)

    fig.add_trace(

        go.Scatter(

            x=ring_x,

            y=ring_y,

            mode="lines",

            line=dict(

                color="gold",

                width=3

            ),

            name="Einstein Ring"

        )

    )

###########################################################
# DEFLECTION VECTORS
###########################################################

show_vectors = st.sidebar.checkbox(
    "Show Light Deflection",
    False
)

if show_vectors:

    step = max(1, num_stars // 120)

    for i in range(0, num_stars, step):

        fig.add_trace(

            go.Scatter(

                x=[x[i], x_deflected[i]],

                y=[y[i], y_deflected[i]],

                mode="lines",

                line=dict(

                    color="rgba(0,255,255,0.35)",

                    width=1

                ),

                showlegend=False

            )

        )

###########################################################
# BACKGROUND GRID
###########################################################

if show_grid:

    grid = np.linspace(-10,10,21)

    for g in grid:

        fig.add_trace(

            go.Scatter(

                x=[-10,10],

                y=[g,g],

                mode="lines",

                line=dict(

                    color="rgba(80,80,80,0.25)",

                    width=1

                ),

                showlegend=False

            )

        )

        fig.add_trace(

            go.Scatter(

                x=[g,g],

                y=[-10,10],

                mode="lines",

                line=dict(

                    color="rgba(80,80,80,0.25)",

                    width=1

                ),

                showlegend=False

            )

        )

###########################################################
# LAYOUT
###########################################################

fig.update_layout(

    title="Gravitational Lensing",

    paper_bgcolor="black",

    plot_bgcolor="black",

    font=dict(

        color="white"

    ),

    xaxis=dict(

        title="X",

        scaleanchor="y",

        showgrid=False,

        zeroline=False,

        range=[-10,10]

    ),

    yaxis=dict(

        title="Y",

        showgrid=False,

        zeroline=False,

        range=[-10,10]

    ),

    legend=dict(

        bgcolor="rgba(0,0,0,0)"

    )

)

st.plotly_chart(

    fig,

    use_container_width=True

)

###########################################################
# APPROXIMATE PHYSICS
###########################################################

einstein_radius = np.sqrt(lens_strength)

average_deflection = np.mean(alpha)

maximum_deflection = np.max(alpha)

magnification = np.mean(

    np.sqrt(

        x_deflected**2 +

        y_deflected**2

    ) /

    np.sqrt(

        x**2 +

        y**2

    )

)

###########################################################
# METRICS
###########################################################

st.divider()

c1,c2,c3,c4 = st.columns(4)

c1.metric(

    "Lens Mass",

    f"{mass:.1f} M☉"

)

c2.metric(

    "Einstein Radius",

    f"{einstein_radius:.3f}"

)

c3.metric(

    "Average Deflection",

    f"{average_deflection:.3f}"

)

c4.metric(

    "Max Deflection",

    f"{maximum_deflection:.3f}"

)

###########################################################
# SECOND ROW
###########################################################

c1,c2,c3 = st.columns(3)

c1.metric(

    "Stars",

    f"{num_stars:,}"

)

c2.metric(

    "Lens Strength",

    f"{lens_strength:.2f}"

)

c3.metric(

    "Approx. Magnification",

    f"{magnification:.3f}"

)

###########################################################
# MASS ANIMATION
###########################################################

animate = st.checkbox(

    "Animate Lens Growth",

    False

)

if animate:

    holder = st.empty()

    progress = st.progress(0)

    values = np.linspace(

        0.5,

        lens_strength,

        40

    )

    theta = np.linspace(

        0,

        2*np.pi,

        300

    )

    for i,val in enumerate(values):

        temp = go.Figure()

        temp.add_trace(

            go.Scatter(

                x=x,

                y=y,

                mode="markers",

                marker=dict(

                    size=2,

                    color="gray"

                ),

                showlegend=False

            )

        )

        rr = np.sqrt(val)

        temp.add_trace(

            go.Scatter(

                x=rr*np.cos(theta),

                y=rr*np.sin(theta),

                mode="lines",

                line=dict(

                    color="gold",

                    width=3

                ),

                showlegend=False

            )

        )

        temp.add_trace(

            go.Scatter(

                x=[0],

                y=[0],

                mode="markers",

                marker=dict(

                    size=20,

                    color="black",

                    line=dict(

                        color="white",

                        width=2

                    )

                ),

                showlegend=False

            )

        )

        temp.update_layout(

            paper_bgcolor="black",

            plot_bgcolor="black",

            xaxis=dict(

                scaleanchor="y",

                range=[-10,10]

            ),

            yaxis=dict(

                range=[-10,10]

            )

        )

        holder.plotly_chart(

            temp,

            use_container_width=True

        )

        progress.progress(

            (i+1)/len(values)

        )

###########################################################
# THEORY
###########################################################

with st.expander("Physics of Gravitational Lensing"):

    st.markdown(r"""

### General Relativity

Mass curves spacetime.

Light follows geodesics in curved spacetime,
causing distant objects to appear distorted.

---

### Deflection Angle

For weak gravitational fields

\[
\alpha=\frac{4GM}{c^2b}
\]

where

- \(M\) = lens mass

- \(b\) = impact parameter

---

### Einstein Ring

Perfect alignment between source,
lens and observer produces
an Einstein Ring.

---

### Applications

Gravitational lensing is used to

- Detect exoplanets

- Measure galaxy masses

- Observe dark matter

- Study galaxy clusters

- Observe distant galaxies

""")

###########################################################
# FOOTER
###########################################################

st.success(

    "Increase the lens strength to observe larger deflections and a more prominent Einstein Ring."

)
