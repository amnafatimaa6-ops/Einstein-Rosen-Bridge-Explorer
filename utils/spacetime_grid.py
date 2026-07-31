"""
spacetime_grid.py

Spacetime visualization utilities.

Contains:
- Cartesian spacetime grids
- Schwarzschild deformation
- gravitational wells
- coordinate transformations
"""

import numpy as np



############################################################
# FLAT SPACETIME GRID
############################################################

def create_flat_grid(
        size=20,
        resolution=100
):
    """
    Generate normal Cartesian grid.
    """


    x=np.linspace(

        -size,

        size,

        resolution

    )


    y=np.linspace(

        -size,

        size,

        resolution

    )


    X,Y=np.meshgrid(

        x,

        y

    )


    Z=np.zeros_like(X)


    return X,Y,Z



############################################################
# SCHWARZSCHILD GRAVITY WELL
############################################################

def schwarzschild_well(
        mass=1.0,
        size=20,
        resolution=200
):
    """
    Create a Schwarzschild gravity well.

    Z deformation:

    z = -M/r
    """


    x=np.linspace(

        -size,

        size,

        resolution

    )


    y=np.linspace(

        -size,

        size,

        resolution

    )


    X,Y=np.meshgrid(

        x,

        y

    )


    R=np.sqrt(

        X**2+

        Y**2

    )


    R=np.maximum(

        R,

        0.1

    )


    Z=-(

        mass/R

    )


    return X,Y,Z



############################################################
# WORMHOLE GRID DEFORMATION
############################################################

def wormhole_grid(
        throat_radius=2,
        size=20,
        resolution=200
):
    """
    Deform coordinate grid around wormhole throat.
    """


    x=np.linspace(

        -size,

        size,

        resolution

    )


    y=np.linspace(

        -size,

        size,

        resolution

    )


    X,Y=np.meshgrid(

        x,

        y

    )


    R=np.sqrt(

        X**2+

        Y**2

    )


    R=np.maximum(

        R,

        throat_radius

    )


    Z=np.sqrt(

        R-throat_radius

    )


    return X,Y,Z



############################################################
# RADIAL DISTORTION
############################################################

def radial_distortion(
        radius,
        strength=1
):
    """
    Calculate coordinate distortion.
    """


    return (

        radius

        /

        (

            1+

            strength/radius

        )

    )



############################################################
# GRID SPACING
############################################################

def grid_spacing(
        size,
        resolution
):
    """
    Calculate coordinate spacing.
    """


    return (

        2*size

        /

        (

            resolution-1

        )

    )



############################################################
# METRIC DEFORMED GRID
############################################################

def metric_deformed_grid(
        mass=1.0,
        size=20,
        resolution=200
):
    """
    Generate grid using Schwarzschild metric factor.

    Demonstrates spatial stretching near mass.
    """


    X,Y,Z=create_flat_grid(

        size,

        resolution

    )


    R=np.sqrt(

        X**2+

        Y**2

    )


    R=np.maximum(

        R,

        0.1

    )


    deformation=(

        1+

        mass/R

    )


    X_new=X*deformation

    Y_new=Y*deformation


    return X_new,Y_new,Z



############################################################
# SPACETIME LATTICE
############################################################

def spacetime_lattice(
        size=10,
        time_steps=50,
        resolution=100
):
    """
    Create 4D-style spacetime lattice.

    Returns spatial grid at different times.
    """


    times=np.linspace(

        0,

        time_steps,

        time_steps

    )


    grids=[]


    X,Y,Z=create_flat_grid(

        size,

        resolution

    )


    for t in times:

        grids.append(

            (

                X,

                Y,

                Z+t

            )

        )


    return grids



############################################################
# SLICE GRID
############################################################

def slice_grid(
        X,
        Y,
        Z,
        axis="z",
        value=0
):
    """
    Extract 2D slice from 3D grid.
    """


    if axis=="z":

        mask=np.abs(Z-value)<0.1


    elif axis=="x":

        mask=np.abs(X-value)<0.1


    elif axis=="y":

        mask=np.abs(Y-value)<0.1


    else:

        raise ValueError(

            "axis must be x,y,z"

        )


    return {

        "x":X[mask],

        "y":Y[mask],

        "z":Z[mask]

    }



############################################################
# GRAVITY CURVATURE MAP
############################################################

def curvature_field(
        X,
        Y,
        mass=1.0
):
    """
    Calculate gravitational strength map.
    """


    R=np.sqrt(

        X**2+

        Y**2

    )


    R=np.maximum(

        R,

        0.1

    )


    return (

        mass/R**3

    )



############################################################
# MESH CONVERSION
############################################################

def grid_to_points(
        X,
        Y,
        Z
):
    """
    Convert grid surface to points.
    """


    return np.column_stack(

        (

            X.flatten(),

            Y.flatten(),

            Z.flatten()

        )

    )



############################################################
# GRID STATISTICS
############################################################

def grid_statistics(
        X,
        Y,
        Z
):
    """
    Return grid information.
    """


    return {

        "points":

            X.size,


        "x_min":

            float(np.min(X)),


        "x_max":

            float(np.max(X)),


        "y_min":

            float(np.min(Y)),


        "y_max":

            float(np.max(Y)),


        "z_min":

            float(np.min(Z)),


        "z_max":

            float(np.max(Z))

    }



############################################################
# EXPORT GRID
############################################################

def export_grid(
        X,
        Y,
        Z,
        filename="spacetime_grid.csv"
):
    """
    Save grid coordinates.
    """


    data=grid_to_points(

        X,

        Y,

        Z

    )


    np.savetxt(

        filename,

        data,

        delimiter=",",

        header="x,y,z",

        comments=""

    )


    return filename
