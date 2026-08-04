import pyvista as pv


def create_event_horizon(radius=1.0, resolution=100):
    """
    Create a spherical event horizon mesh.

    Parameters
    ----------
    radius : float
        Event horizon radius.

    resolution : int
        Sphere resolution.

    Returns
    -------
    pyvista.PolyData
        Sphere mesh.
    """

    sphere = pv.Sphere(
        radius=radius,
        theta_resolution=resolution,
        phi_resolution=resolution
    )

    return sphere
