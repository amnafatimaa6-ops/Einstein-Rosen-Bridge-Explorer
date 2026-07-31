import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Physics Calculator",
    page_icon="🧮",
    layout="wide"
)

st.title("🧮 Black Hole Physics Calculator")

st.markdown("""
Compute important quantities for Schwarzschild black holes.
All values are calculated instantly as you move the sliders.
""")

############################################################
# CONSTANTS
############################################################

G = 6.67430e-11
c = 299792458
M_sun = 1.98847e30

############################################################
# SIDEBAR
############################################################

st.sidebar.header("Input Parameters")

mass = st.sidebar.slider(
    "Mass (Solar Masses)",
    1.0,
    100.0,
    10.0,
    0.5
)

distance = st.sidebar.slider(
    "Observer Distance (km)",
    50.0,
    500000.0,
    1000.0,
    10.0
)

############################################################

M = mass * M_sun
r = distance * 1000

############################################################
# PHYSICS
############################################################

schwarzschild_radius = (2 * G * M) / c**2

escape_velocity = np.sqrt(
    (2 * G * M) / r
)

escape_fraction = escape_velocity / c

time_dilation = np.sqrt(
    max(1 - schwarzschild_radius / r, 0)
)

redshift = (1 / time_dilation) - 1 if time_dilation > 0 else np.inf

surface_gravity = (G * M) / (schwarzschild_radius ** 2)

orbital_velocity = np.sqrt((G * M) / r)

orbital_period = 2 * np.pi * r / orbital_velocity

density = M / ((4/3) * np.pi * schwarzschild_radius**3)

############################################################
# RESULTS
############################################################

st.header("Calculated Values")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Schwarzschild Radius",
        f"{schwarzschild_radius/1000:.2f} km"
    )

    st.metric(
        "Escape Velocity",
        f"{escape_fraction:.4f} c"
    )

with c2:
    st.metric(
        "Time Dilation",
        f"{time_dilation:.6f}"
    )

    st.metric(
        "Redshift",
        f"{redshift:.6f}"
    )

with c3:
    st.metric(
        "Surface Gravity",
        f"{surface_gravity:.3e} m/s²"
    )

    st.metric(
        "Density",
        f"{density:.3e} kg/m³"
    )

############################################################

st.subheader("Orbital Motion")

st.metric(
    "Orbital Velocity",
    f"{orbital_velocity:.3e} m/s"
)

st.metric(
    "Orbital Period",
    f"{orbital_period:.2f} s"
)

############################################################
# TABLE
############################################################

st.subheader("Summary Table")

st.table({

    "Quantity":[

        "Mass",

        "Observer Distance",

        "Schwarzschild Radius",

        "Escape Velocity",

        "Surface Gravity",

        "Time Dilation",

        "Redshift",

        "Orbital Velocity",

        "Orbital Period",

        "Density"

    ],

    "Value":[

        f"{mass:.2f} M☉",

        f"{distance:.2f} km",

        f"{schwarzschild_radius/1000:.2f} km",

        f"{escape_fraction:.4f} c",

        f"{surface_gravity:.3e} m/s²",

        f"{time_dilation:.6f}",

        f"{redshift:.6f}",

        f"{orbital_velocity:.3e} m/s",

        f"{orbital_period:.2f} s",

        f"{density:.3e} kg/m³"

    ]

})



############################################################
# ADDITIONAL PHYSICS
############################################################

h = 6.62607015e-34
kB = 1.380649e-23
HBAR = h / (2 * np.pi)

############################################################
# PHOTON SPHERE & ISCO
############################################################

photon_sphere = 1.5 * schwarzschild_radius
isco = 3 * schwarzschild_radius

############################################################
# HAWKING TEMPERATURE
############################################################

hawking_temperature = (

    (HBAR * c**3)

    /

    (

        8 * np.pi * G * M * kB

    )

)

############################################################
# BEKENSTEIN-HKING ENTROPY
############################################################

planck_length = np.sqrt(

    HBAR * G / c**3

)

area = 4 * np.pi * schwarzschild_radius**2

entropy = (

    area

    /

    (

        4 * planck_length**2

    )

)

############################################################
# LIGHT CROSSING TIME
############################################################

crossing_time = schwarzschild_radius / c

############################################################
# METRICS
############################################################

st.divider()

st.subheader("Additional Physics")

c1, c2 = st.columns(2)

with c1:

    st.metric(

        "Photon Sphere",

        f"{photon_sphere/1000:.2f} km"

    )

    st.metric(

        "ISCO",

        f"{isco/1000:.2f} km"

    )

    st.metric(

        "Light Crossing Time",

        f"{crossing_time:.6e} s"

    )

with c2:

    st.metric(

        "Hawking Temperature",

        f"{hawking_temperature:.3e} K"

    )

    st.metric(

        "Entropy",

        f"{entropy:.3e}"

    )

############################################################
# RADIAL PLOT
############################################################

st.subheader("Escape Velocity vs Radius")

radii = np.linspace(

    schwarzschild_radius * 1.05,

    schwarzschild_radius * 25,

    500

)

velocity = np.sqrt(

    (2 * G * M)

    / radii

)

velocity /= c

import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(

    go.Scatter(

        x=radii / 1000,

        y=velocity,

        mode="lines",

        line=dict(

            color="cyan",

            width=4

        ),

        name="Escape Velocity"

    )

)

fig.add_vline(

    x=schwarzschild_radius / 1000,

    line_dash="dash",

    line_color="red"

)

fig.update_layout(

    title="Escape Velocity",

    xaxis_title="Radius (km)",

    yaxis_title="Fraction of c",

    paper_bgcolor="black",

    plot_bgcolor="black",

    font=dict(

        color="white"

    )

)

st.plotly_chart(

    fig,

    use_container_width=True

)

############################################################
# FORMULAE
############################################################

with st.expander("Formula Sheet"):

    st.markdown(r"""

### Schwarzschild Radius

\[
r_s=\frac{2GM}{c^2}
\]

---

### Escape Velocity

\[
v_e=\sqrt{\frac{2GM}{r}}
\]

---

### Time Dilation

\[
d\tau=
dt\sqrt{1-\frac{r_s}{r}}
\]

---

### Hawking Temperature

\[
T=
\frac{\hbar c^3}
{8\pi G M k_B}
\]

---

### Bekenstein-Hawking Entropy

\[
S=
\frac{A}
{4l_p^2}
\]

---

### Photon Sphere

\[
r=\frac{3GM}{c^2}
\]

---

### ISCO

\[
r=\frac{6GM}{c^2}
\]

""")

############################################################
# SCIENTIFIC NOTES
############################################################

with st.expander("Interpretation"):

    st.markdown("""

### Schwarzschild Radius

Defines the event horizon of a non-rotating black hole.

---

### Photon Sphere

The radius where light can orbit the black hole in an unstable circular path.

---

### ISCO

The innermost stable circular orbit for matter around a Schwarzschild black hole.

---

### Hawking Temperature

Black holes emit extremely weak thermal radiation. The larger the mass, the lower the temperature.

---

### Entropy

The Bekenstein–Hawking entropy is proportional to the area of the event horizon, not its volume. This idea underpins the holographic principle.

---

### Time Dilation

As an observer approaches the event horizon, time runs increasingly slowly relative to a distant observer.

""")

############################################################
# EXPORT
############################################################

st.download_button(

    "Download Results",

    data=f"""
Mass (Solar Masses): {mass}
Observer Distance (km): {distance}
Schwarzschild Radius (km): {schwarzschild_radius/1000}
Photon Sphere (km): {photon_sphere/1000}
ISCO (km): {isco/1000}
Escape Velocity (c): {escape_fraction}
Time Dilation: {time_dilation}
Redshift: {redshift}
Surface Gravity (m/s²): {surface_gravity}
Density (kg/m³): {density}
Hawking Temperature (K): {hawking_temperature}
Entropy: {entropy}
Light Crossing Time (s): {crossing_time}
""",

    file_name="black_hole_calculations.txt",

    mime="text/plain"

)

############################################################
# FOOTER
############################################################

st.success(
    "Physics calculations complete. Adjust the sliders to explore how black hole properties change with mass and observer distance."
)
