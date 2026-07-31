import numpy as np


def horizontal_slice(X, Y, Z, slice_height):
    """
    Remove everything ABOVE a given Z height.

    Parameters
    ----------
    X, Y, Z : ndarray
        Surface coordinates

    slice_height : float
        Height at which to cut

    Returns
    -------
    Xs, Ys, Zs
    """

    Xs = X.copy()
    Ys = Y.copy()
    Zs = Z.copy()

    mask = Zs > slice_height

    Xs[mask] = np.nan
    Ys[mask] = np.nan
    Zs[mask] = np.nan

    return Xs, Ys, Zs


def vertical_slice_x(X, Y, Z, x_position):
    """
    Slice along the X direction.
    """

    Xs = X.copy()
    Ys = Y.copy()
    Zs = Z.copy()

    mask = Xs > x_position

    Xs[mask] = np.nan
    Ys[mask] = np.nan
    Zs[mask] = np.nan

    return Xs, Ys, Zs


def vertical_slice_y(X, Y, Z, y_position):
    """
    Slice along the Y direction.
    """

    Xs = X.copy()
    Ys = Y.copy()
    Zs = Z.copy()

    mask = Ys > y_position

    Xs[mask] = np.nan
    Ys[mask] = np.nan
    Zs[mask] = np.nan

    return Xs, Ys, Zs


def cylindrical_slice(X, Y, Z, radius):
    """
    Remove everything outside a cylinder.

    Useful for exposing the wormhole throat.
    """

    Xs = X.copy()
    Ys = Y.copy()
    Zs = Z.copy()

    R = np.sqrt(Xs**2 + Ys**2)

    mask = R > radius

    Xs[mask] = np.nan
    Ys[mask] = np.nan
    Zs[mask] = np.nan

    return Xs, Ys, Zs


def wedge_slice(X, Y, Z, angle):
    """
    Remove a wedge from the wormhole.

    Great for seeing inside the bridge.
    """

    Xs = X.copy()
    Ys = Y.copy()
    Zs = Z.copy()

    theta = np.degrees(np.arctan2(Ys, Xs))

    mask = theta > angle

    Xs[mask] = np.nan
    Ys[mask] = np.nan
    Zs[mask] = np.nan
