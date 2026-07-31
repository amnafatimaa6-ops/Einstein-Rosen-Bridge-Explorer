import numpy as np


def einstein_rosen_bridge(mass=1.0,
                          r_max=12,
                          resolution=220):
    """
    Generate the Einstein-Rosen Bridge surface.

    Returns
    -------
    X,Y,Z arrays ready for Plotly Surface().
    """

    # Schwarzschild radius
    rs = 2 * mass

    # Radial coordinates
    r = np.linspace(rs + 0.001, r_max, resolution)

    theta = np.linspace(0, 2 * np.pi, resolution)

    R, Theta = np.meshgrid(r, theta)

    # Embedding equation
    Z = 2 * np.sqrt(rs * (R - rs))

    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)

    return X, Y, Z
