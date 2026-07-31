import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Mathematics",
    page_icon="📐",
    layout="wide"
)

st.title("📐 Mathematics of Wormholes & Black Holes")

st.markdown("""
This section summarises the mathematics behind the
Einstein–Rosen Bridge, Schwarzschild black holes,
and Morris–Thorne traversable wormholes.

The equations shown here are those commonly introduced
in undergraduate General Relativity courses.
""")

###########################################################
# SIDEBAR
###########################################################

st.sidebar.header("Parameters")

mass = st.sidebar.slider(
    "Mass (M☉)",
    1.0,
    20.0,
    5.0,
    0.5
)

r = st.sidebar.slider(
    "Radial Coordinate",
    2.5,
    50.0,
    10.0,
    0.5
)

throat = st.sidebar.slider(
    "Throat Radius",
    1.0,
    10.0,
    2.0,
    0.1
)

###########################################################
# CONSTANTS
###########################################################

G = 6.67430e-11
c = 299792458
M_sun = 1.98847e30

M = mass * M_sun

rs = (2 * G * M) / c**2

###########################################################
# EINSTEIN FIELD EQUATIONS
###########################################################

st.header("Einstein Field Equations")

st.latex(r"""
G_{\mu\nu}
+
\Lambda g_{\mu\nu}
=
\frac{8\pi G}{c^4}
T_{\mu\nu}
""")

st.markdown("""
These equations relate the curvature of spacetime
to the energy and momentum of matter.
""")

###########################################################
# SCHWARZSCHILD METRIC
###########################################################

st.header("Schwarzschild Metric")

st.latex(r"""
ds^2=
-
\left(
1-
\frac{2GM}{rc^2}
\right)
c^2dt^2
+
\left(
1-
\frac{2GM}{rc^2}
\right)^{-1}
dr^2
+
r^2
d\Omega^2
""")

st.markdown("""
The Schwarzschild metric describes the spacetime
outside a static, spherically symmetric mass.
""")

###########################################################
# EINSTEIN–ROSEN BRIDGE
###########################################################

st.header("Einstein–Rosen Bridge")

st.latex(r"""
z(r)=
2
\sqrt{
r_s
(r-r_s)
}
""")

st.markdown("""
This embedding function produces the familiar bridge
connecting two asymptotically flat regions.
""")

###########################################################
# MORRIS–THORNE METRIC
###########################################################

st.header("Morris–Thorne Wormhole")

st.latex(r"""
ds^2=
-
e^{2\Phi(r)}
dt^2
+
\frac{
dr^2
}{
1-
\frac{b(r)}{r}
}
+
r^2d\Omega^2
""")

st.markdown("""
Here,

- Φ(r) is the redshift function.

- b(r) is the shape function.

For a traversable wormhole,
the throat satisfies

b(r₀)=r₀.
""")

###########################################################
# EMBEDDING FUNCTION
###########################################################

radius = np.linspace(
    rs/1000 + 0.01,
    100,
    400
)

embedding = 2 * np.sqrt(
    (rs/1000) *
    (radius - rs/1000)
)

fig = go.Figure()

fig.add_trace(

    go.Scatter(

        x=radius,

        y=embedding,

        mode="lines",

        line=dict(
            color="cyan",
            width=4
        ),

        name="Upper Surface"

    )

)

fig.add_trace(

    go.Scatter(

        x=radius,

        y=-embedding,

        mode="lines",

        line=dict(
            color="cyan",
            width=4
        ),

        showlegend=False

    )

)

fig.update_layout(

    title="Einstein–Rosen Embedding",

    paper_bgcolor="black",

    plot_bgcolor="black",

    font=dict(color="white"),

    xaxis_title="Radius",

    yaxis_title="Embedding Height"

)

st.plotly_chart(
    fig,
    use_container_width=True
)


###########################################################
# EFFECTIVE POTENTIAL
###########################################################

st.header("Effective Potential")

L = st.slider(
    "Angular Momentum (L)",
    1.0,
    10.0,
    4.0,
    0.1
)

radius = np.linspace(
    rs * 1.05,
    rs * 20,
    500
)

V = (
    -G * M / radius
    + (L**2) / (2 * radius**2)
    - (G * M * L**2) / (c**2 * radius**3)
)

fig2 = go.Figure()

fig2.add_trace(

    go.Scatter(

        x=radius / 1000,

        y=V,

        mode="lines",

        line=dict(
            color="gold",
            width=4
        ),

        name="Effective Potential"

    )

)

fig2.update_layout(

    title="Effective Potential",

    paper_bgcolor="black",

    plot_bgcolor="black",

    font=dict(color="white"),

    xaxis_title="Radius (km)",

    yaxis_title="V(r)"

)

st.plotly_chart(
    fig2,
    use_container_width=True
)

###########################################################
# SCHWARZSCHILD RADIUS
###########################################################

st.header("Schwarzschild Radius")

st.latex(r"""
r_s=\frac{2GM}{c^2}
""")

st.markdown(f"""

For the current mass

**M = {mass:.2f} M☉**

the Schwarzschild radius is

### **{rs/1000:.3f} km**

""")

###########################################################
# PROPER DISTANCE
###########################################################

st.header("Proper Radial Distance")

st.latex(r"""
l(r)=
\int
\frac{dr}
{\sqrt{1-r_s/r}}
""")

st.markdown("""
This integral measures the physical radial distance
instead of the coordinate distance.
""")

###########################################################
# GEODESIC EQUATION
###########################################################

st.header("Geodesic Equation")

st.latex(r"""
\frac{d^2x^\mu}{d\tau^2}
+
\Gamma^\mu_{\alpha\beta}
\frac{dx^\alpha}{d\tau}
\frac{dx^\beta}{d\tau}
=0
""")

st.markdown("""
Particles and photons follow geodesics in curved
spacetime rather than experiencing gravity as a force.
""")

###########################################################
# CHRISTOFFEL SYMBOLS
###########################################################

st.header("Christoffel Symbols")

st.latex(r"""
\Gamma^\mu_{\alpha\beta}
=
\frac12
g^{\mu\nu}
(
\partial_\alpha g_{\nu\beta}
+
\partial_\beta g_{\nu\alpha}
-
\partial_\nu g_{\alpha\beta}
)
""")

###########################################################
# RIEMANN CURVATURE
###########################################################

st.header("Riemann Curvature Tensor")

st.latex(r"""
R^\rho_{\ \sigma\mu\nu}
=
\partial_\mu
\Gamma^\rho_{\nu\sigma}
-
\partial_\nu
\Gamma^\rho_{\mu\sigma}
+
\Gamma^\rho_{\mu\lambda}
\Gamma^\lambda_{\nu\sigma}
-
\Gamma^\rho_{\nu\lambda}
\Gamma^\lambda_{\mu\sigma}
""")

###########################################################
# RICCI TENSOR
###########################################################

st.header("Ricci Tensor")

st.latex(r"""
R_{\mu\nu}
=
R^\lambda_{\mu\lambda\nu}
""")

###########################################################
# RICCI SCALAR
###########################################################

st.header("Ricci Scalar")

st.latex(r"""
R
=
g^{\mu\nu}
R_{\mu\nu}
""")

###########################################################
# KRETSCHMANN SCALAR
###########################################################

st.header("Kretschmann Scalar")

st.latex(r"""
K=
R_{\mu\nu\rho\sigma}
R^{\mu\nu\rho\sigma}
=
\frac{48G^2M^2}
{c^4r^6}
""")

st.markdown("""
Unlike the coordinate singularity at the event horizon,
the Kretschmann scalar diverges at **r = 0**, revealing the
true spacetime singularity.
""")

###########################################################
# FORMULA SUMMARY
###########################################################

st.subheader("Quick Reference")

st.table({

"Equation":[

"Einstein Field Equation",

"Schwarzschild Radius",

"Photon Sphere",

"ISCO",

"Time Dilation",

"Escape Velocity",

"Hawking Temperature",

"Entropy"

],

"Formula":[

r"$G_{\mu\nu}=\frac{8\pi G}{c^4}T_{\mu\nu}$",

r"$r_s=2GM/c^2$",

r"$3GM/c^2$",

r"$6GM/c^2$",

r"$\sqrt{1-r_s/r}$",

r"$\sqrt{2GM/r}$",

r"$\hbar c^3 /(8\pi GMk_B)$",

r"$A/(4l_p^2)$"

]

})

###########################################################
# GLOSSARY
###########################################################

with st.expander("Mathematical Glossary"):

    st.markdown("""

**Metric Tensor** — Describes distances in spacetime.

**Christoffel Symbols** — Describe how coordinates change in curved spacetime.

**Geodesic** — The straightest possible path through curved spacetime.

**Ricci Tensor** — Measures how matter curves spacetime.

**Ricci Scalar** — Overall curvature.

**Riemann Tensor** — Complete description of spacetime curvature.

**Kretschmann Scalar** — Detects true gravitational singularities.

""")

###########################################################
# EXPORT
###########################################################

equations = """
Einstein Field Equation
Gμν = (8πG/c⁴)Tμν

Schwarzschild Radius
rₛ = 2GM/c²

Schwarzschild Metric
ds² = -(1-rₛ/r)c²dt² + (1-rₛ/r)⁻¹dr² + r²dΩ²

Einstein–Rosen Embedding
z(r)=2√(rₛ(r-rₛ))

Morris–Thorne Metric
ds²=-e²Φdt²+dr²/(1-b/r)+r²dΩ²

Geodesic Equation
d²xμ/dτ² + Γμαβ dxα/dτ dxβ/dτ = 0
"""

st.download_button(
    "📄 Download Formula Sheet",
    equations,
    file_name="wormhole_mathematics.txt",
    mime="text/plain"
)

###########################################################
# FOOTER
###########################################################

st.success(
    "This page summarizes the core mathematics used throughout the Einstein–Rosen Bridge Explorer."
)
