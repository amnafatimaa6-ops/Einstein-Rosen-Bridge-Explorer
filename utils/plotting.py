"""
plotting.py

Interactive Plotly visualization utilities for the
Einstein-Rosen Bridge Explorer.
"""

import numpy as np
import plotly.graph_objects as go

from utils.geometry import einstein_rosen_bridge
from utils.camera import camera_position

from utils.slicing import (
    horizontal_slice,
    vertical_slice_x,
    vertical_slice_y,
    cylindrical_slice,
    wedge_slice
)


def apply_slice(
        X,
        Y,
        Z,
        slice_type,
        slice_value):

    if slice_type == "Horizontal":
        return horizontal_slice(
            X,
            Y,
            Z,
            slice_value
        )

    if slice_type == "Vertical X":
        return vertical_slice_x(
            X,
            Y,
            Z,
            slice_value
        )

    if slice_type == "Vertical Y":
        return vertical_slice_y(
            X,
            Y,
            Z,
            slice_value
        )

    if slice_type == "Cylinder":
        return cylindrical_slice(
            X,
            Y,
            Z,
            abs(slice_value)
        )

    if slice_type == "Wedge":
        return wedge_slice(
            X,
            Y,
            Z,
            slice_value * 12
        )

    return X, Y, Z


def add_surface(
        fig,
        X,
        Y,
        Z,
        opacity,
        colorscale):

    fig.add_surface(

        x=X,
        y=Y,
        z=Z,

        opacity=opacity,

        colorscale=colorscale,

        showscale=False,

        hovertemplate=
        "<b>X</b>: %{x:.2f}<br>"
        "<b>Y</b>: %{y:.2f}<br>"
        "<b>Z</b>: %{z:.2f}<extra></extra>"

    )


def add_wireframe(
        fig,
        X,
        Y,
        Z):

    step = 8

    for i in range(0, X.shape[0], step):

        fig.add_trace(

            go.Scatter3d(

                x=X[i],

                y=Y[i],

                z=Z[i],

                mode="lines",

                line=dict(
                    width=2,
                    color="white"
                ),

                showlegend=False

            )

        )

    for j in range(0, X.shape[1], step):

        fig.add_trace(

            go.Scatter3d(

                x=X[:, j],

                y=Y[:, j],

                z=Z[:, j],

                mode="lines",

                line=dict(
                    width=2,
                    color="white"
                ),

                showlegend=False

            )

        )


def add_event_horizon(
        fig,
        mass):

    rs = 2 * mass

    u = np.linspace(0, np.pi, 40)

    v = np.linspace(0, 2 * np.pi, 40)

    u, v = np.meshgrid(u, v)

    x = rs * np.sin(u) * np.cos(v)
    y = rs * np.sin(u) * np.sin(v)
    z = rs * np.cos(u)

    fig.add_surface(

        x=x,

        y=y,

        z=z,

        opacity=0.30,

        colorscale="Reds",

        showscale=False

    )


def create_bridge(

        mass,

        distance,

        elevation,

        azimuth,

        opacity,

        colorscale,

        wireframe,

        show_axes,

        slice_type,

        slice_value,

        auto_rotate,

        rotation_speed

):

    X, Y, Z = einstein_rosen_bridge(mass)

    X, Y, Z = apply_slice(

        X,
        Y,
        Z,

        slice_type,

        slice_value

    )

    fig = go.Figure()

    add_surface(

        fig,

        X,

        Y,

        Z,

        opacity,

        colorscale

    )

    add_surface(

        fig,

        X,

        Y,

        -Z,

        opacity,

        colorscale

    )

    if wireframe:

        add_wireframe(

            fig,

            X,

            Y,

            Z

        )

        add_wireframe(

            fig,

            X,

            Y,

            -Z

        )

    add_event_horizon(

        fig,

        mass

    )

    if auto_rotate:

        azimuth += rotation_speed

    fig.update_layout(

        title="Einstein-Rosen Bridge",

        paper_bgcolor="black",

        plot_bgcolor="black",

        margin=dict(
            l=0,
            r=0,
            b=0,
            t=45
        ),

        scene=dict(

            aspectmode="data",

            camera=camera_position(

                distance,

                elevation,

                azimuth

            ),
