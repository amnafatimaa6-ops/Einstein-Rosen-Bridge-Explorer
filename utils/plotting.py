"""
plotting.py

Visualization utilities for Einstein-Rosen Bridge Explorer.

Uses Plotly for Streamlit rendering.
"""

import numpy as np
import plotly.graph_objects as go



############################################################
# EINSTEIN-ROSEN BRIDGE
############################################################

def create_bridge(
        throat_radius=2,
        length=10,
        resolution=200,
        mass=None,
        **kwargs
):
    """
    Create Einstein-Rosen Bridge 3D surface.

    Parameters
    ----------
    throat_radius:
        Wormhole throat size

    length:
        Length of bridge along z-axis

    resolution:
        Mesh resolution

    mass:
        Optional black hole mass parameter

    Returns
    -------
    Plotly Figure
    """


    u = np.linspace(

        -length,

        length,

        resolution

    )


    theta = np.linspace(

        0,

        2*np.pi,

        resolution

    )


    U, T = np.meshgrid(

        u,

        theta

    )


    ########################################################
    # Einstein-Rosen geometry
    ########################################################


    R = throat_radius + np.abs(U)**2


    X = R * np.cos(T)

    Y = R * np.sin(T)

    Z = U



    ########################################################
    # Plotly surface
    ########################################################


    fig = go.Figure(

        data=[

            go.Surface(

                x=X,

                y=Y,

                z=Z,

                colorscale="Viridis",

                opacity=0.95,

                showscale=False

            )

        ]

    )



    fig.update_layout(

        title="Einstein-Rosen Bridge",

        scene=dict(

            xaxis_title="Spatial X",

            yaxis_title="Spatial Y",

            zaxis_title="Spatial Z",

            aspectmode="data"

        ),

        margin=dict(

            l=0,

            r=0,

            b=0,

            t=40

        )

    )


    return fig





############################################################
# GENERIC SURFACE
############################################################

def surface_plot(
        X,
        Y,
        Z,
        title="3D Surface"
):


    fig = go.Figure(

        data=[

            go.Surface(

                x=X,

                y=Y,

                z=Z,

                colorscale="Viridis"

            )

        ]

    )


    fig.update_layout(

        title=title,

        scene=dict(

            aspectmode="data"

        )

    )


    return fig





############################################################
# 3D SCATTER
############################################################

def scatter_3d(
        x,
        y,
        z,
        title="3D Scatter"
):


    fig = go.Figure(

        data=[

            go.Scatter3d(

                x=x,

                y=y,

                z=z,

                mode="markers",

                marker=dict(

                    size=3

                )

            )

        ]

    )


    fig.update_layout(

        title=title,

        scene=dict(

            aspectmode="data"

        )

    )


    return fig





############################################################
# TRAJECTORY PLOT
############################################################

def trajectory_plot(
        x,
        y,
        z,
        title="Trajectory"
):


    fig = go.Figure(

        data=[

            go.Scatter3d(

                x=x,

                y=y,

                z=z,

                mode="lines",

                line=dict(

                    width=5

                )

            )

        ]

    )


    fig.update_layout(

        title=title,

        scene=dict(

            aspectmode="data"

        )

    )


    return fig





############################################################
# EVENT HORIZON SPHERE
############################################################

def black_hole_sphere(
        radius=2,
        resolution=100
):


    phi = np.linspace(

        0,

        np.pi,

        resolution

    )


    theta = np.linspace(

        0,

        2*np.pi,

        resolution

    )


    P,T = np.meshgrid(

        phi,

        theta

    )


    X = radius*np.sin(P)*np.cos(T)

    Y = radius*np.sin(P)*np.sin(T)

    Z = radius*np.cos(P)



    return surface_plot(

        X,

        Y,

        Z,

        "Event Horizon"

    )





############################################################
# EMBEDDING DIAGRAM
############################################################

def embedding_plot(
        r,
        z,
        title="Embedding Diagram"
):


    theta=np.linspace(

        0,

        2*np.pi,

        len(r)

    )


    R,T=np.meshgrid(

        r,

        theta

    )


    Z=np.tile(

        z,

        (

            len(theta),

            1

        )

    )


    X=R*np.cos(T)

    Y=R*np.sin(T)



    return surface_plot(

        X,

        Y,

        Z,

        title

    )





############################################################
# ADD STAR FIELD
############################################################

def add_stars(
        fig,
        stars
):


    fig.add_trace(

        go.Scatter3d(

            x=stars["x"],

            y=stars["y"],

            z=stars["z"],

            mode="markers",

            marker=dict(

                size=2,

                opacity=0.8

            ),

            name="Stars"

        )

    )


    return fig
