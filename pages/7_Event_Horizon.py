import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Event Horizon Explorer",
    page_icon="⚫",
    layout="wide"
)

st.title("⚫ Event Horizon Explorer")

st.markdown("""
Explore how the event horizon changes as the mass of a
Schwarzschild black hole changes.
""")

############################################################
# SIDEBAR
############################################################

st.sidebar.header("Black Hole")

mass = st.sidebar.slider(
    "Mass (Solar Masses)",
    1.0,
    50.0,
    10.0,
    0.5
)

############################################################

G = 6.67430e-11
c = 299792458
M_sun = 1.98847e30

mass_kg = mass * M_sun

############################################################
# PHYSICS
############################################################

schwarzschild_radius = (

    2 * G * mass_kg

) / (c**2)

schwarzschild_km = schwarzschild_radius / 1000

photon_sphere = 1.5 * schwarzschild_km

isco = 3 * schwarzschild_km

############################################################

distance = st.sidebar.slider(

    "Observer Distance (km)",

    schwarzschild_km + 5,

    schwarzschild_km * 30,

    schwarzschild_km * 8

)

############################################################

show_photon = st.sidebar.checkbox(
    "Show Photon Sphere",
    True
)

show_isco = st.sidebar.checkbox(
    "Show ISCO",
    True
)

############################################################

resolution = st.sidebar.slider(

    "Resolution",

    100,

    500,

    250,

    10

)

############################################################
# GEOMETRY
############################################################

theta = np.linspace(

    0,

    2*np.pi,

    resolution

)

############################################################

hx = schwarzschild_km*np.cos(theta)

hy = schwarzschild_km*np.sin(theta)

############################################################

px = photon_sphere*np.cos(theta)

py = photon_sphere*np.sin(theta)

############################################################

ix = isco*np.cos(theta)

iy = isco*np.sin(theta)

############################################################
# ESCAPE VELOCITY
############################################################

escape_velocity = np.sqrt(

    (2*G*mass_kg)

    /(distance*1000)

)

escape_fraction = escape_velocity/c

############################################################
# TIME DILATION
############################################################

ratio = schwarzschild_km/distance

ratio = min(ratio,0.999999)

time_dilation = np.sqrt(

    1-ratio

)

############################################################
# GRAVITATIONAL REDSHIFT
############################################################

redshift = (

    1/time_dilation

)-1

############################################################
# FIGURE
############################################################

fig = go.Figure()

############################################################
# EVENT HORIZON
############################################################

fig.add_trace(

    go.Scatter(

        x=hx,

        y=hy,

        fill="toself",

        fillcolor="black",

        mode="lines",

        line=dict(

            color="white",

            width=2

        ),

        name="Event Horizon"

    )

)

############################################################
# PHOTON SPHERE
############################################################

if show_photon:

    fig.add_trace(

        go.Scatter(

            x=px,

            y=py,

            mode="lines",

            line=dict(

                color="gold",

                dash="dash",

                width=3

            ),

            name="Photon Sphere"

        )

    )

############################################################
# ISCO
############################################################

if show_isco:

    fig.add_trace(

        go.Scatter(

            x=ix,

            y=iy,

            mode="lines",

            line=dict(

                color="cyan",

                dash="dot",

                width=3

            ),

            name="ISCO"

        )

    )


############################################################
# OBSERVER
############################################################

fig.add_trace(

    go.Scatter(

        x=[distance],

        y=[0],

        mode="markers+text",

        marker=dict(

            color="lime",

            size=12,

            symbol="diamond"

        ),

        text=["Observer"],

        textposition="top center",

        name="Observer"

    )

)

############################################################
# RADIAL GUIDE
############################################################

fig.add_trace(

    go.Scatter(

        x=[0,distance],

        y=[0,0],

        mode="lines",

        line=dict(

            color="white",

            dash="dot"

        ),

        showlegend=False

    )

)

############################################################
# LAYOUT
############################################################

fig.update_layout(

    title="Schwarzschild Event Horizon",

    paper_bgcolor="black",

    plot_bgcolor="black",

    font=dict(

        color="white"

    ),

    xaxis=dict(

        title="Distance (km)",

        scaleanchor="y",

        showgrid=True,

        zeroline=False

    ),

    yaxis=dict(

        title="Distance (km)",

        showgrid=True,

        zeroline=False

    ),

    legend=dict(

        bgcolor="rgba(0,0,0,0)"

    )

)

st.plotly_chart(

    fig,

    use_container_width=True

)

############################################################
# METRICS
############################################################

st.divider()

c1,c2,c3,c4 = st.columns(4)

c1.metric(

    "Mass",

    f"{mass:.1f} M☉"

)

c2.metric(

    "Event Horizon",

    f"{schwarzschild_km:.2f} km"

)

c3.metric(

    "Photon Sphere",

    f"{photon_sphere:.2f} km"

)

c4.metric(

    "ISCO",

    f"{isco:.2f} km"

)

############################################################
# SECOND ROW
############################################################

c1,c2,c3 = st.columns(3)

c1.metric(

    "Escape Velocity",

    f"{escape_fraction:.3f} c"

)

c2.metric(

    "Time Dilation",

    f"{time_dilation:.5f}"

)

c3.metric(

    "Gravitational Redshift",

    f"{redshift:.5f}"

)

############################################################
# COMPACT TABLE
############################################################

st.subheader("Computed Values")

st.table({

    "Quantity":[

        "Schwarzschild Radius",

        "Photon Sphere",

        "ISCO",

        "Observer Distance",

        "Escape Velocity",

        "Time Dilation",

        "Redshift"

    ],

    "Value":[

        f"{schwarzschild_km:.2f} km",

        f"{photon_sphere:.2f} km",

        f"{isco:.2f} km",

        f"{distance:.2f} km",

        f"{escape_fraction:.3f} c",

        f"{time_dilation:.5f}",

        f"{redshift:.5f}"

    ]

})

############################################################
# MASS EVOLUTION
############################################################

animate = st.checkbox(

    "Animate Mass Increase",

    False

)

if animate:

    placeholder = st.empty()

    progress = st.progress(0)

    masses = np.linspace(

        1,

        mass,

        50

    )

    for i,m in enumerate(masses):

        rs = (

            2*G*(m*M_sun)

        )/(c**2)/1000

        xx = rs*np.cos(theta)

        yy = rs*np.sin(theta)

        temp = go.Figure()

        temp.add_trace(

            go.Scatter(

                x=xx,

                y=yy,

                fill="toself",

                fillcolor="black",

                mode="lines",

                line=dict(color="white")

            )

        )

        temp.update_layout(

            paper_bgcolor="black",

            plot_bgcolor="black",

            xaxis=dict(scaleanchor="y"),

            showlegend=False

        )

        placeholder.plotly_chart(

            temp,

            use_container_width=True

        )

        progress.progress(

            (i+1)/len(masses)

        )

############################################################
# THEORY
############################################################

with st.expander("Physics Behind the Event Horizon"):

    st.markdown(r"""

### Schwarzschild Radius

\[
r_s=\frac{2GM}{c^2}
\]

The event horizon marks the boundary beyond which
no signal can escape.

---

### Photon Sphere

\[
r=\frac{3GM}{c^2}
\]

Light can orbit the black hole at this radius,
although the orbit is unstable.

---

### ISCO

\[
r=\frac{6GM}{c^2}
\]

This is the **Innermost Stable Circular Orbit**
for a non-rotating Schwarzschild black hole.

---

### Time Dilation

\[
d\tau = dt\sqrt{1-\frac{r_s}{r}}
\]

A clock close to the event horizon runs more
slowly compared with one far away.

---

### Gravitational Redshift

\[
z=\frac1{\sqrt{1-r_s/r}}-1
\]

Light escaping the gravitational field loses energy
and is shifted toward longer wavelengths.

""")

############################################################
# FOOTER
############################################################

st.info(
    "Tip: Increase the black hole mass and move the observer closer to the event horizon to see how relativistic effects become stronger."
)
