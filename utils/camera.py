"""
Camera utilities for the 3D explorer.
"""

import numpy as np


def camera_position(distance, elevation, azimuth):
    """
    Convert spherical coordinates into Plotly camera coordinates.
    """

    elev = np.radians(elevation)
    azim = np.radians(azimuth)

    x = distance * np.cos(elev) * np.cos(azim)
    y = distance * np.cos(elev) * np.sin(azim)
    z = distance * np.sin(elev)

    return dict(
        eye=dict(
            x=float(x),
            y=float(y),
            z=float(z)
        )
    )
