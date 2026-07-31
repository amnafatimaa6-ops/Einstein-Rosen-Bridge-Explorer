"""
wormholes.py

Core wormhole geometry generators.

Contains:
- Einstein-Rosen Bridge geometry
- Morris-Thorne traversable wormhole geometry
- Throat calculations
- Surface mesh generation

Used by Streamlit visualization pages.
"""

import numpy as np


############################################################
# EINSTEIN-ROSEN BRIDGE
############################################################

def einstein_rosen_bridge(
        mass=1.0,
        r_max=10.0,
        resolution=200
):
    """
    Generate Einstein-Rosen bridge embedding surface.

    Parameters
    ----------
    mass : float
        Black hole mass parameter

    r_max : float
        Maximum radial coordinate

    resolution : int
        Mesh resolution

    Returns
    -------
    X,Y,Z_upper,Z_lower
    """

    rs = 2 * mass


    r = np.linspace(
        rs + 0.01,
        r_max,
        resolution
    )


    theta = np.linspace(
        0,
        2*np.pi,
        resolution
    )


    R, T = np.meshgrid(
        r,
        theta
    )


    X = R*np.cos(T)

    Y = R*np.sin(T)


    Z = 2*np.sqrt(
        rs*(R-rs)
    )


    return (
        X,
        Y,
        Z,
        -Z
    )


############################################################
# MORRIS-THORNE WORMHOLE
############################################################

def morris_thorne_wormhole(
        throat_radius=2.0,
        r_max=15.0,
        resolution=200
):
    """
    Generate Morris-Thorne traversable wormhole.

    Shape function:

    b(r)=r0

    Embedding:

    z(r)=r0 arccosh(r/r0)
    """


    r = np.linspace(

        throat_radius,

        r_max,

        resolution

    )


    theta = np.linspace(

        0,

        2*np.pi,

        resolution

    )


    R,T=np.meshgrid(

        r,

        theta

    )


    X=R*np.cos(T)

    Y=R*np.sin(T)


    Z=(
        throat_radius *
        np.arccosh(
            R/throat_radius
        )
    )


    return (

        X,

        Y,

        Z,

        -Z

    )


############################################################
# WORMHOLE THROAT
############################################################

def throat_radius(
        shape_function
):
    """
    Return throat radius where

    b(r)=r

    For numerical shape functions.
    """

    values=[]


    r=np.linspace(
        0.1,
        20,
        1000
    )


    for x in r:

        values.append(

            abs(
                shape_function(x)-x
            )

        )


    index=np.argmin(values)


    return r[index]


############################################################
# RADIAL PROFILE
############################################################

def embedding_profile(
        wormhole="einstein_rosen",
        parameter=2,
        r_max=20,
        points=500
):
    """
    Generate 2D embedding curve.
    """


    r=np.linspace(

        parameter+0.01,

        r_max,

        points

    )


    if wormhole=="einstein_rosen":

        z=2*np.sqrt(

            parameter*
            (r-parameter)

        )


    elif wormhole=="morris_thorne":

        z=(

            parameter*

            np.arccosh(

                r/parameter

            )

        )


    else:

        raise ValueError(

            "Unknown wormhole type"

        )


############################################################
# MORRIS-THORNE SHAPE FUNCTION
############################################################

def morris_thorne_shape_function(
        r,
        throat_radius=2.0
):
    """
    Constant shape function:

    b(r)=r0

    Used for the simplest traversable wormhole.
    """

    return throat_radius



############################################################
# REDSHIFT FUNCTION
############################################################

def redshift_function(
        r,
        redshift_parameter=0.0
):
    """
    Morris-Thorne redshift function.

    Phi(r)=constant

    A zero value avoids horizons.
    """

    return redshift_parameter



############################################################
# METRIC COMPONENTS
############################################################

def morris_thorne_metric_components(
        r,
        throat_radius=2.0
):
    """
    Simplified Morris-Thorne metric components.

    Returns:

    g_tt
    g_rr
    g_theta_theta
    g_phi_phi
    """


    Phi = redshift_function(r)


    b = morris_thorne_shape_function(
        r,
        throat_radius
    )


    g_tt = -np.exp(
        2*Phi
    )


    g_rr = 1/(

        1-b/r

    )


    g_theta = r**2


    g_phi = r**2


    return {

        "g_tt":g_tt,

        "g_rr":g_rr,

        "g_theta_theta":g_theta,

        "g_phi_phi":g_phi

    }



############################################################
# EINSTEIN-ROSEN METRIC FACTOR
############################################################

def schwarzschild_factor(
        r,
        mass=1.0
):
    """
    Schwarzschild metric factor:

    f(r)=1-rs/r
    """


    rs = 2*mass


    return (

        1-rs/r

    )



############################################################
# HORIZON CHECK
############################################################

def has_event_horizon(
        r,
        mass=1.0
):
    """
    Determine if point is inside
    Schwarzschild horizon.
    """


    rs=2*mass


    return r <= rs



############################################################
# EXOTIC MATTER INDICATOR
############################################################

def energy_condition_parameter(
        r,
        throat_radius=2.0
):
    """
    Simplified NEC violation indicator.

    Negative values represent
    exotic matter requirements.
    """


    b = throat_radius


    density = (

        -b /

        (8*np.pi*r**3)

    )


    return density



############################################################
# WORMHOLE CROSS SECTION
############################################################

def wormhole_cross_section(
        radius=2.0,
        resolution=200
):
    """
    Generate circular throat cross-section.
    """


    theta=np.linspace(

        0,

        2*np.pi,

        resolution

    )


    x=radius*np.cos(theta)

    y=radius*np.sin(theta)


    return x,y



############################################################
# ROTATION MATRIX
############################################################

def rotate_geometry(
        X,
        Y,
        Z,
        angle_x=0,
        angle_y=0,
        angle_z=0
):
    """
    Rotate 3D wormhole mesh.

    Used by camera controls.
    """


    ax=np.radians(angle_x)

    ay=np.radians(angle_y)

    az=np.radians(angle_z)


    X1=X.copy()
    Y1=Y.copy()
    Z1=Z.copy()


    # X rotation

    Y2 = Y1*np.cos(ax)-Z1*np.sin(ax)

    Z2 = Y1*np.sin(ax)+Z1*np.cos(ax)


    # Y rotation

    X3 = X1*np.cos(ay)+Z2*np.sin(ay)

    Z3 = -X1*np.sin(ay)+Z2*np.cos(ay)


    # Z rotation

    X4 = X3*np.cos(az)-Y2*np.sin(az)

    Y4 = X3*np.sin(az)+Y2*np.cos(az)


    return (

        X4,

        Y4,

        Z3

    )



############################################################
# MESH INFORMATION
############################################################

def geometry_statistics(
        X,
        Y,
        Z
):
    """
    Return geometry statistics.
    """


    return {

        "points":X.size,

        "x_range":(

            float(np.min(X)),

            float(np.max(X))

        ),

        "y_range":(

            float(np.min(Y)),

            float(np.max(Y))

        ),

        "z_range":(

            float(np.min(Z)),

            float(np.max(Z))

        )

    }



############################################################
# EXPORT DATA
############################################################

def export_mesh_arrays(
        X,
        Y,
        Z
):
    """
    Prepare geometry for saving.
    """


    return np.column_stack(

        (

            X.flatten(),

            Y.flatten(),

            Z.flatten()

        )

    )

    return r,z,-z
