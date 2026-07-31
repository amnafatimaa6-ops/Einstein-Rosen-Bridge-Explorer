"""
embedding.py

Embedding diagram utilities for
black holes and wormholes.

Contains:
- Flamm's paraboloid
- Einstein-Rosen embedding
- Morris-Thorne embedding
- Curvature profiles
"""

import numpy as np



############################################################
# SCHWARZSCHILD FLAMM PARABOLOID
############################################################

def flamm_paraboloid(
        mass=1.0,
        r_max=20,
        resolution=300
):
    """
    Generate Flamm's paraboloid.

    z(r)=2*sqrt(rs*(r-rs))

    Parameters
    ----------
    mass:
        Schwarzschild mass parameter

    """

    rs = 2 * mass


    r = np.linspace(

        rs + 0.01,

        r_max,

        resolution

    )


    z = 2*np.sqrt(

        rs*(r-rs)

    )


    return r,z



############################################################
# TWO SIDED EINSTEIN-ROSEN EMBEDDING
############################################################

def einstein_rosen_embedding(
        mass=1.0,
        r_max=20,
        resolution=300
):
    """
    Create two sides of the Einstein-Rosen bridge.
    """


    r,z = flamm_paraboloid(

        mass,

        r_max,

        resolution

    )


    return {

        "r":r,

        "upper":z,

        "lower":-z

    }



############################################################
# MORRIS-THORNE EMBEDDING
############################################################

def morris_thorne_embedding(
        throat_radius=2.0,
        r_max=20,
        resolution=300
):
    """
    Morris-Thorne embedding:

    z(r)=r0 arccosh(r/r0)
    """


    r=np.linspace(

        throat_radius,

        r_max,

        resolution

    )


    z=(

        throat_radius *

        np.arccosh(

            r/throat_radius

        )

    )


    return {

        "r":r,

        "upper":z,

        "lower":-z

    }



############################################################
# RADIAL SLOPE
############################################################

def embedding_slope(
        r,
        throat_radius
):
    """
    dz/dr for Morris-Thorne style geometry.
    """


    return (

        throat_radius /

        np.sqrt(

            r**2 -

            throat_radius**2

        )

    )



############################################################
# CURVATURE PROFILE
############################################################

def curvature_profile(
        r,
        mass=1.0
):
    """
    Approximate curvature strength.

    Based on inverse radial dependence.
    """

    rs = 2*mass


    return (

        rs /

        r**3

    )



############################################################
# EMBEDDING GRID
############################################################

def embedding_surface(
        r_values,
        z_values,
        resolution=200
):
    """
    Convert 2D embedding curve
    into 3D rotational surface.
    """


    theta=np.linspace(

        0,

        2*np.pi,

        resolution

    )


    R,T=np.meshgrid(

        r_values,

        theta

    )


    Z=np.tile(

        z_values,

        (

            resolution,

            1

        )

    )


    X=R*np.cos(T)

    Y=R*np.sin(T)



############################################################
# THROAT DETECTION
############################################################

def find_throat(
        r,
        z
):
    """
    Find minimum radius point.

    The throat is the narrowest
    point of the embedding surface.
    """


    index=np.argmin(r)


    return {

        "index":index,

        "radius":float(r[index]),

        "height":float(z[index])

    }



############################################################
# PROPER DISTANCE
############################################################

def proper_distance(
        r,
        z
):
    """
    Calculate proper radial distance.

    dl = sqrt(1+(dz/dr)^2) dr
    """


    dz=np.gradient(z,r)


    integrand=np.sqrt(

        1+dz**2

    )


    distance=np.zeros_like(r)


    for i in range(1,len(r)):

        distance[i]=(

            distance[i-1]

            +

            integrand[i]*(r[i]-r[i-1])

        )


    return distance



############################################################
# EMBEDDING COMPARISON
############################################################

def compare_embeddings(
        mass=1.0,
        throat=2.0,
        r_max=20,
        resolution=300
):
    """
    Generate Einstein-Rosen and
    Morris-Thorne profiles together.
    """


    er=einstein_rosen_embedding(

        mass,

        r_max,

        resolution

    )


    mt=morris_thorne_embedding(

        throat,

        r_max,

        resolution

    )


    return {

        "einstein_rosen":er,

        "morris_thorne":mt

    }



############################################################
# SURFACE NORMALS
############################################################

def surface_normals(
        X,
        Y,
        Z
):
    """
    Estimate normals for a mesh.
    """


    dx=np.gradient(X)

    dy=np.gradient(Y)

    dz=np.gradient(Z)


    nx=dy[0]*dz[1]-dz[0]*dy[1]

    ny=dz[0]*dx[1]-dx[0]*dz[1]

    nz=dx[0]*dy[1]-dy[0]*dx[1]


    magnitude=np.sqrt(

        nx**2+

        ny**2+

        nz**2

    )


    magnitude=np.maximum(

        magnitude,

        1e-10

    )


    return (

        nx/magnitude,

        ny/magnitude,

        nz/magnitude

    )



############################################################
# EMBEDDING HEATMAP DATA
############################################################

def curvature_map(
        X,
        Y,
        Z
):
    """
    Create a simple curvature intensity map.
    """


    radius=np.sqrt(

        X**2+

        Y**2

    )


    curvature=1/(

        radius**2+1e-8

    )


    return curvature



############################################################
# CONVERT TO POINT CLOUD
############################################################

def surface_points(
        X,
        Y,
        Z
):
    """
    Convert mesh to xyz points.
    """


    points=np.column_stack(

        (

            X.flatten(),

            Y.flatten(),

            Z.flatten()

        )

    )


    return points



############################################################
# MESH BOUNDS
############################################################

def mesh_bounds(
        X,
        Y,
        Z
):
    """
    Return spatial limits.
    """


    return {

        "xmin":float(np.min(X)),

        "xmax":float(np.max(X)),

        "ymin":float(np.min(Y)),

        "ymax":float(np.max(Y)),

        "zmin":float(np.min(Z)),

        "zmax":float(np.max(Z))

    }



############################################################
# EMBEDDING EXPORT
############################################################

def export_embedding(
        X,
        Y,
        Z,
        filename="embedding.csv"
):
    """
    Export mesh coordinates.
    """


    data=np.column_stack(

        (

            X.flatten(),

            Y.flatten(),

            Z.flatten()

        )

    )


    np.savetxt(

        filename,

        data,

        delimiter=",",

        header="x,y,z",

        comments=""

    )


    return filename



############################################################
# EMBEDDING SUMMARY
############################################################

def embedding_summary(
        r,
        z
):
    """
    Return important geometry information.
    """


    return {

        "minimum_radius":
            float(np.min(r)),


        "maximum_radius":
            float(np.max(r)),


        "maximum_curvature":
            float(np.max(
                curvature_profile(r)
            )),


        "height_difference":
            float(
                np.max(z)-np.min(z)
            )

    }

    return X,Y,Z
