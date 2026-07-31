import streamlit as st

st.set_page_config(
    page_title="References",
    page_icon="📚",
    layout="wide"
)

st.title("📚 References")

st.markdown("""
This project combines concepts from **General Relativity,
Black Hole Physics, Wormhole Theory,
Computational Physics, and Scientific Visualization**.

Below are the primary references used throughout
the Einstein–Rosen Bridge Explorer.
""")

##############################################################
# BOOKS
##############################################################

st.header("📖 Books")

st.markdown("""

### General Relativity

• Sean Carroll — *Spacetime and Geometry*

• Robert M. Wald — *General Relativity*

• Charles W. Misner,
Kip S. Thorne,
John A. Wheeler

*Gravitation*

• Bernard Schutz

*A First Course in General Relativity*

---

### Black Holes

• Kip Thorne

*Black Holes and Time Warps*

• Stephen Hawking

*A Brief History of Time*

• James B. Hartle

*Gravity*

---

### Wormholes

• Matt Visser

*Lorentzian Wormholes*

• Morris & Thorne (1988)

*Wormholes in Spacetime*

""")

##############################################################
# CLASSIC PAPERS
##############################################################

st.header("📄 Research Papers")

papers = [

("1935",
"Einstein & Rosen",
"The Particle Problem in the General Theory of Relativity"),

("1916",
"Karl Schwarzschild",
"On the Gravitational Field of a Point Mass"),

("1988",
"Morris & Thorne",
"Wormholes in Spacetime and Their Use for Interstellar Travel"),

("1974",
"Stephen Hawking",
"Black Hole Explosions"),

("1973",
"Bekenstein",
"Black Hole Entropy")

]

for year,author,title in papers:

    st.markdown(f"""
**{year}**

**{author}**

*{title}*
""")

##############################################################
# NASA / ESA / SCIENTIFIC DATA
##############################################################

st.header("🛰 Scientific Data Sources")

st.markdown("""

• NASA

- Chandra X-ray Observatory

- Hubble Space Telescope

- James Webb Space Telescope

- HEASARC

- ADS

---

• ESA

- Gaia

- Euclid Mission

---

• LIGO

- GWOSC

---

• Event Horizon Telescope

- Black Hole Images

""")

##############################################################
# PYTHON LIBRARIES
##############################################################

st.header("🐍 Python Libraries")

libraries = [

"NumPy",

"SciPy",

"Plotly",

"PyVista",

"VTK",

"Streamlit",

"Pandas",

"SymPy",

"Matplotlib"

]

st.table({

"Library":libraries

})

##############################################################
# FORMULAE USED
##############################################################

st.header("📐 Main Equations")

st.latex(r"""
r_s=\frac{2GM}{c^2}
""")

st.latex(r"""
ds^2=
-
\left(
1-\frac{2GM}{rc^2}
\right)
c^2dt^2
+
\left(
1-\frac{2GM}{rc^2}
\right)^{-1}
dr^2
+r^2d\Omega^2
""")

st.latex(r"""
z(r)=
2
\sqrt{
r_s(r-r_s)
}
""")

st.latex(r"""
ds^2=
-
e^{2\Phi(r)}
dt^2
+
\frac{dr^2}
{1-\frac{b(r)}{r}}
+
r^2d\Omega^2
""")

##############################################################
# PROJECT FEATURES
##############################################################

st.header("🚀 Features Demonstrated")

features = [

"Einstein–Rosen Bridge",

"Morris–Thorne Wormhole",

"Interactive 3D Explorer",

"Embedding Diagrams",

"Geodesic Simulation",

"Event Horizon Explorer",

"Gravitational Lensing",

"Physics Calculator",

"Mathematical Reference",

"Scientific Visualization"

]

for feature in features:

    st.markdown(f"✅ {feature}")

##############################################################
# FUTURE WORK
##############################################################

st.header("🔭 Future Improvements")

future = [

"Rotating Kerr Black Holes",

"Kerr–Newman Geometry",

"Reissner–Nordström Solution",

"Penrose Diagrams",

"Ray Tracing",

"GPU Acceleration",

"Real LIGO Data Integration",

"NASA HEASARC Catalogs",

"Interactive Tensor Calculator",

"VR Wormhole Explorer"

]

for item in future:

    st.markdown(f"• {item}")

##############################################################
# ABOUT PROJECT
##############################################################

st.header("💡 About")

st.info("""

Einstein–Rosen Bridge Explorer is an educational and
scientific visualization platform built with

• Streamlit

• Plotly

• PyVista

• NumPy

• SciPy

Its purpose is to help students and researchers
visualize General Relativity, black holes,
wormholes, geodesics, and spacetime geometry
through interactive simulations.

""")

##############################################################
# VERSION
##############################################################

st.divider()

c1, c2, c3 = st.columns(3)

c1.metric(
    "Version",
    "1.0.0"
)

c2.metric(
    "Pages",
    "12"
)

c3.metric(
    "License",
    "MIT"
)

##############################################################
# FOOTER
##############################################################

st.success(
    "Thank you for exploring the Einstein–Rosen Bridge Explorer. Keep questioning the universe! 🌌"
)
