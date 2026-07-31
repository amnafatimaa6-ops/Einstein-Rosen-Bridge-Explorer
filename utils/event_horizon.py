"""
event_horizon.py

Black hole event horizon utilities.

Includes:
- Schwarzschild radius
- Photon sphere
- ISCO
- Relativistic effects
- Horizon geometry generation
"""

import numpy as np



############################################################
# CONSTANTS
############################################################

G = 6.67430e-11

c = 299792458

hbar = 1.054571817e-34

kB = 1.380649e-23



############################################################
# SCHWARZSCHILD RADIUS
############################################################

def schwarzschild_radius(
        mass
):
    """
    Event horizon radius.

    mass in kilograms
    """


    return (

        2*G*mass

        /

        c**2

    )



############################################################
# PHOTON SPHERE
############################################################

def photon_sphere(
        mass
):
    """
    Radius where photons can orbit.

    r = 3GM/c²
    """


    return (

        3*G*mass

        /

        c**2

    )



############################################################
# ISCO
############################################################

def isco_radius(
        mass
):
    """
    Innermost stable circular orbit.

    r = 6GM/c²
    """


    return (

        6*G*mass

        /

        c**2

    )



############################################################
# ESCAPE VELOCITY
############################################################

def escape_velocity(
        mass,
        radius
):
    """
    Classical escape velocity.
    """


    return np.sqrt(

        2*G*mass/radius

    )



############################################################
# TIME DILATION
############################################################

def gravitational_time_dilation(
        mass,
        radius
):
    """
    Schwarzschild time dilation.

    Returns fraction of distant time.
    """


    rs=schwarzschild_radius(

        mass

    )


    if radius <= rs:

        return 0


    return np.sqrt(

        1-rs/radius

    )



############################################################
# REDSHIFT
############################################################

def gravitational_redshift(
        mass,
        radius
):
    """
    Gravitational redshift.
    """


    dilation=gravitational_time_dilation(

        mass,

        radius

    )


    if dilation==0:

        return np.inf


    return (

        1/dilation

        -

        1

    )



############################################################
# HAWKING TEMPERATURE
############################################################

def hawking_temperature(
        mass
):
    """
    Hawking radiation temperature.
    """


    return (

        hbar*c**3

        /

        (

            8*np.pi*G*mass*kB

        )



############################################################
# EVENT HORIZON SPHERE
############################################################

def event_horizon_mesh(
        mass,
        resolution=100
):
    """
    Generate 3D event horizon sphere.

    Returns X,Y,Z mesh.
    """


    radius = schwarzschild_radius(

        mass

    )


    theta=np.linspace(

        0,

        2*np.pi,

        resolution

    )


    phi=np.linspace(

        0,

        np.pi,

        resolution

    )


    T,P=np.meshgrid(

        theta,

        phi

    )


    X=radius*np.sin(P)*np.cos(T)

    Y=radius*np.sin(P)*np.sin(T)

    Z=radius*np.cos(P)


    return X,Y,Z



############################################################
# PHOTON SPHERE MESH
############################################################

def photon_sphere_mesh(
        mass,
        resolution=100
):
    """
    Generate photon sphere surface.
    """


    radius=photon_sphere(

        mass

    )


    theta=np.linspace(

        0,

        2*np.pi,

        resolution

    )


    phi=np.linspace(

        0,

        np.pi,

        resolution

    )


    T,P=np.meshgrid(

        theta,

        phi

    )


    X=radius*np.sin(P)*np.cos(T)

    Y=radius*np.sin(P)*np.sin(T)

    Z=radius*np.cos(P)


    return X,Y,Z



############################################################
# ISCO RING
############################################################

def isco_ring(
        mass,
        points=500
):
    """
    Generate ISCO circular orbit.
    """


    radius=isco_radius(

        mass

    )


    theta=np.linspace(

        0,

        2*np.pi,

        points

    )


    X=radius*np.cos(theta)

    Y=radius*np.sin(theta)

    Z=np.zeros_like(theta)


    return X,Y,Z



############################################################
# ACCRETION DISK
############################################################

def accretion_disk(
        inner_radius,
        outer_radius,
        particles=3000
):
    """
    Create simple accretion disk particles.
    """


    rng=np.random.default_rng(42)


    radius=rng.uniform(

        inner_radius,

        outer_radius,

        particles

    )


    angle=rng.uniform(

        0,

        2*np.pi,

        particles

    )


    X=radius*np.cos(angle)

    Y=radius*np.sin(angle)


    thickness=rng.normal(

        0,

        0.05,

        particles

    )


    return X,Y,thickness



############################################################
# BLACK HOLE PARAMETERS
############################################################

def black_hole_summary(
        mass
):
    """
    Return important black hole values.
    """


    rs=schwarzschild_radius(

        mass

    )


    return {

        "event_horizon_km":

            rs/1000,


        "photon_sphere_km":

            photon_sphere(mass)/1000,


        "isco_km":

            isco_radius(mass)/1000,


        "hawking_temperature":

            hawking_temperature(mass)

    }



############################################################
# HORIZON CHECK
############################################################

def inside_horizon(
        radius,
        mass
):
    """
    Check if point lies inside horizon.
    """


    return radius <= schwarzschild_radius(

        mass

    )



############################################################
# GRAVITY STRENGTH
############################################################

def gravitational_field(
        mass,
        radius
):
    """
    Newtonian gravitational acceleration.
    """


    return (

        G*mass

        /

        radius**2

    )



############################################################
# RELATIVISTIC FACTOR
############################################################

def schwarzschild_factor(
        mass,
        radius
):
    """
    Metric time component.

    g_tt = -(1-rs/r)
    """


    rs=schwarzschild_radius(

        mass

    )


    return -(

        1-rs/r

    )



############################################################
# EXPORT DATA
############################################################

def horizon_data(
        mass,
        filename="black_hole_data.csv"
):
    """
    Save black hole parameters.
    """


    data=black_hole_summary(

        mass

    )


    import pandas as pd


    df=pd.DataFrame(

        [data]

    )


    df.to_csv(

        filename,

        index=False

    )


    return filename
    )
