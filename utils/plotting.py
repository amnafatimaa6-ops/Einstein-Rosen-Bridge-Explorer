"""
plotting.py

Visualization utilities for Einstein-Rosen Bridge Explorer.

Contains:
- Einstein-Rosen bridge plots
- Wormhole surfaces
- Embedding plots
- General 3D helpers
"""

import numpy as np
import plotly.graph_objects as go



############################################################
# EINSTEIN-ROSEN BRIDGE
############################################################

def create_bridge(
        throat_radius=2,
        length=10,
        resolution=200
):
    """
    Create Einstein-Rosen Bridge 3D visualization.

    Returns Plotly Figure.
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


    # bridge radius profile
    R = throat_radius + U**2


    X = R*np.cos(T)

    Y = R*np.sin(T)

    Z = U



    fig = go.Figure(

        data=[

            go.Surface(

                x=X,

                y=Y,

                z=Z,

                colorscale="Viridis",

                opacity=0.9,

                showscale=False

            )

        ]

    )


    fig.update_layout(

        title="Einstein-Rosen Bridge",

        scene=dict(

            xaxis_title="X",

            yaxis_title="Y",

            zaxis_title="Z",

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
# GENERIC SURFACE PLOT
############################################################

def surface_plot(
        X,
        Y,
        Z,
        title="3D Surface"
):
    """
    Plot any 3D surface.
    """


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
# SCATTER 3D
############################################################

def scatter_3d(
        x,
        y,
        z,
        title="3D Scatter"
):
    """
    Plot particles or trajectories.
    """


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
    """
    Plot particle path.
    """


    fig = go.Figure(

        data=[

            go.Scatter3d(

                x=x,

                y=y,

                z=z,

                mode="lines"

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
    """
    Create event horizon sphere.
    """


    phi=np.linspace(

        0,

        np.pi,

        resolution

    )


    theta=np.linspace(

        0,

        2*np.pi,

        resolution

    )


    P,T=np.meshgrid(

        phi,

        theta

    )


    X=radius*np.sin(P)*np.cos(T)

    Y=radius*np.sin(P)*np.sin(T)

    Z=radius*np.cos(P)



    return surface_plot(

        X,

        Y,

        Z,

        "Event Horizon"

    )
