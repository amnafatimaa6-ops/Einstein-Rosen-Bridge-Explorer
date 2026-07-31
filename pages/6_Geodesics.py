import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.integrate import solve_ivp

st.set_page_config(
    page_title="Geodesic Simulator",
    page_icon="🛰️",
    layout="wide"
)

st.title("🛰️ Schwarzschild Geodesic Simulator")

st.markdown("""
Simulate the motion of photons and massive particles
around a Schwarzschild black hole.

The trajectories are computed numerically from the
geodesic equations.
""")

##############################################################
# SIDEBAR
##############################################################

st.sidebar.header("Central Object")

mass = st.sidebar.slider(
    "Black Hole Mass",
    1.0,
    20.0,
    5.0,
    0.1
)

##############################################################

st.sidebar.header("Particle")

particle = st.sidebar.selectbox(

    "Particle Type",

    [

        "Photon",

        "Massive Particle"

    ]

)

##############################################################

initial_radius = st.sidebar.slider(

    "Initial Radius",

    5.0,

    40.0,

    15.0,

    0.5

)

##############################################################

initial_velocity = st.sidebar.slider(

    "Tangential Velocity",

    0.1,

    1.5,

    0.65,

    0.01

)

##############################################################

simulation_time = st.sidebar.slider(

    "Simulation Time",

    20,

    300,

    100

)

##############################################################

resolution = st.sidebar.slider(

    "Integration Steps",

    100,

    3000,

    1000,

    100

)

##############################################################
# CONSTANTS
##############################################################

G = 1.0
C = 1.0

rs = 2 * G * mass / (C**2)

##############################################################
# GEODESIC EQUATIONS
##############################################################

def geodesic(t, y):

    r = y[0]

    phi = y[1]

    vr = y[2]

    vphi = y[3]

    if r <= rs:

        r = rs + 0.001

    drdt = vr

    dphidt = vphi

    radial_acceleration = (

        -(G*mass)/(r**2)

        +

        r*(vphi**2)

    )

    angular_acceleration = (

        -2*vr*vphi/r

    )

    return [

        drdt,

        dphidt,

        radial_acceleration,

        angular_acceleration

    ]

##############################################################
# INITIAL CONDITIONS
##############################################################

y0 = [

    initial_radius,

    0.0,

    0.0,

    initial_velocity

]

##############################################################
# NUMERICAL SOLVER
##############################################################

times = np.linspace(

    0,

    simulation_time,

    resolution

)

solution = solve_ivp(

    geodesic,

    [

        0,

        simulation_time

    ],

    y0,

    t_eval=times,

    rtol=1e-8,

    atol=1e-8

)

##############################################################
# POLAR TO CARTESIAN
##############################################################

r = solution.y[0]

phi = solution.y[1]

x = r*np.cos(phi)


##############################################################
# TRAJECTORY FIGURE
##############################################################

fig = go.Figure()

##############################################################
# EVENT HORIZON
##############################################################

theta = np.linspace(0, 2*np.pi, 400)

hx = rs * np.cos(theta)
hy = rs * np.sin(theta)

fig.add_trace(

    go.Scatter(

        x=hx,

        y=hy,

        mode="lines",

        fill="toself",

        fillcolor="black",

        line=dict(
            color="black",
            width=2
        ),

        name="Event Horizon"

    )

)

##############################################################
# PHOTON SPHERE
##############################################################

photon_radius = 1.5 * rs

px = photon_radius*np.cos(theta)

py = photon_radius*np.sin(theta)

fig.add_trace(

    go.Scatter(

        x=px,

        y=py,

        mode="lines",

        line=dict(

            dash="dash",

            color="gold",

            width=2

        ),

        name="Photon Sphere"

    )

)

##############################################################
# TRAJECTORY
##############################################################

if particle == "Photon":

    colour = "cyan"

else:

    colour = "lime"

fig.add_trace(

    go.Scatter(

        x=x,

        y=y,

        mode="lines",

        line=dict(

            color=colour,

            width=3

        ),

        name=particle

    )

)

##############################################################
# START / END POINTS
##############################################################

fig.add_trace(

    go.Scatter(

        x=[x[0]],

        y=[y[0]],

        mode="markers",

        marker=dict(

            size=10,

            color="green"

        ),

        name="Start"

    )

)

fig.add_trace(

    go.Scatter(

        x=[x[-1]],

        y=[y[-1]],

        mode="markers",

        marker=dict(

            size=10,

            color="red"

        ),

        name="End"

    )

)

##############################################################
# LAYOUT
##############################################################

fig.update_layout(

    title="Schwarzschild Geodesic",

    paper_bgcolor="black",

    plot_bgcolor="black",

    font=dict(color="white"),

    xaxis=dict(

        title="X",

        scaleanchor="y",

        showgrid=True,

        zeroline=False

    ),

    yaxis=dict(

        title="Y",

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

##############################################################
# METRICS
##############################################################

st.divider()

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

    "Initial Radius",

    f"{initial_radius:.2f}"

)

c4.metric(

    "Velocity",

    f"{initial_velocity:.2f}"

)

##############################################################
# ORBIT DATA
##############################################################

st.subheader("Simulation Output")

st.write({

    "Current Radius":

        float(r[-1]),

    "Final X":

        float(x[-1]),

    "Final Y":

        float(y[-1]),

    "Steps":

        len(times)

})

##############################################################
# ENERGY (Approximate)
##############################################################

energy = 0.5*(initial_velocity**2) - mass/initial_radius

angular = initial_radius*initial_velocity

col1,col2 = st.columns(2)

with col1:

    st.metric(

        "Approx. Specific Energy",

        f"{energy:.4f}"

    )

with col2:

    st.metric(

        "Angular Momentum",

        f"{angular:.4f}"

    )

##############################################################
# ANIMATION
##############################################################

animate = st.checkbox(

    "Animate Trajectory",

    False

)

if animate:

    progress = st.progress(0)

    frame = st.empty()

    for i in range(

        5,

        len(x),

        5

    ):

        temp = go.Figure()

        temp.add_trace(

            go.Scatter(

                x=hx,

                y=hy,

                fill="toself",

                fillcolor="black",

                mode="lines",

                line=dict(color="black")

            )

        )

        temp.add_trace(

            go.Scatter(

                x=x[:i],

                y=y[:i],

                mode="lines",

                line=dict(

                    color=colour,

                    width=3

                )

            )

        )

        temp.update_layout(

            paper_bgcolor="black",

            plot_bgcolor="black",

            xaxis=dict(scaleanchor="y")

        )

        frame.plotly_chart(

            temp,

            use_container_width=True

        )

        progress.progress(

            i/len(x)

        )

##############################################################
# THEORY
##############################################################

with st.expander("Physics"):

    st.markdown(r"""

The trajectory is obtained by numerically integrating
the geodesic equations in Schwarzschild spacetime.

Important radii:

- Schwarzschild Radius

\[
r_s=\frac{2GM}{c^2}
\]

Photon Sphere

\[
r=\frac{3GM}{c^2}
\]

Outside these regions,
particles may orbit, escape or fall inward depending
on their initial conditions.

This simulator uses SciPy's Runge-Kutta solver
(`solve_ivp`) to integrate the equations of motion.

""")
y = r*np.sin(phi)
