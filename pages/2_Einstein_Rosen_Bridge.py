import streamlit as st

from utils.plotting import create_bridge

st.title("🌌 Einstein-Rosen Bridge Explorer")

st.sidebar.header("Physics")

mass = st.sidebar.slider(

    "Black Hole Mass",

    1.0,

    10.0,

    2.0,

    0.1

)

fig = create_bridge(mass)

st.plotly_chart(
    fig,
    use_container_width=True
)
