"""
trajectories.py

Trajectory generation utilities.

Contains:
- orbital trajectories
- photon paths
- spacecraft paths
- interpolation helpers
"""

import numpy as np



############################################################
# CIRCULAR ORBIT
############################################################

def circular_trajectory(
        radius=10,
        revolutions=5,
        points=2000
):
    """
    Generate circular orbital path.
    """


    theta=np.linspace(

        0,

        2*np.pi*revolutions,

        points

    )


    x=radius*np.cos(theta)

    y=radius*np.sin(theta)

    z=np.zeros_like(theta)


    return x,y,z



############################################################
# SPIRAL TRAJECTORY
############################################################

def spiral_trajectory(
        start_radius=20,
        end_radius=2,
        turns=5,
        points=2000
):
    """
    Generate inward spiral motion.

    Useful for accretion disk particles.
    """


    theta=np.linspace(

        0,

        2*np.pi*turns,

        points

    )


    radius=np.linspace(

        start_radius,

        end_radius,

        points

    )


    x=radius*np.cos(theta)

    y=radius*np.sin(theta)

    z=np.zeros_like(theta)


    return x,y,z



############################################################
# FREE FALL PATH
############################################################

def free_fall_trajectory(
        initial_radius=20,
        final_radius=2,
        points=500
):
    """
    Radial infall trajectory.
    """


    r=np.linspace(

        initial_radius,

        final_radius,

        points

    )


    theta=np.zeros(points)


    x=r

    y=theta

    z=np.zeros(points)


    return x,y,z



############################################################
# HELICAL PATH
############################################################

def helical_trajectory(
        radius=5,
        height=20,
        turns=4,
        points=1000
):
    """
    Camera-style fly through trajectory.
    """


    theta=np.linspace(

        0,

        2*np.pi*turns,

        points

    )


    x=radius*np.cos(theta)

    y=radius*np.sin(theta)


    z=np.linspace(

        -height/2,

        height/2,

        points

    )


    return x,y,z



############################################################
# RANDOM PARTICLE PATH
############################################################

def random_trajectory(
        length=1000,
        scale=1,
        seed=42
):
    """
    Random walk particle trajectory.
    """


    rng=np.random.default_rng(seed)


    steps=rng.normal(

        0,

        scale,

        (

            length,

            3

        )

    )


    position=np.cumsum(

        steps,

        axis=0

    )


    return (

        position[:,0],

        position[:,1],

        position[:,2]

    )





############################################################
# VELOCITY CALCULATION
############################################################

def velocity(
        x,
        y,
        z,
        dt=1.0
):
    """
    Calculate numerical velocity.
    """


    vx=np.gradient(

        x,

        dt

    )


    vy=np.gradient(

        y,

        dt

    )


    vz=np.gradient(

        z,

        dt

    )


    return vx,vy,vz



############################################################
# ACCELERATION CALCULATION
############################################################

def acceleration(
        x,
        y,
        z,
        dt=1.0
):
    """
    Calculate numerical acceleration.
    """


    vx,vy,vz=velocity(

        x,

        y,

        z,

        dt

    )


    ax=np.gradient(

        vx,

        dt

    )


    ay=np.gradient(

        vy,

        dt

    )


    az=np.gradient(

        vz,

        dt

    )


    return ax,ay,az



############################################################
# TRAJECTORY LENGTH
############################################################

def path_length(
        x,
        y,
        z
):
    """
    Calculate total distance travelled.
    """


    dx=np.diff(x)

    dy=np.diff(y)

    dz=np.diff(z)


    distance=np.sqrt(

        dx**2+

        dy**2+

        dz**2

    )


    return np.sum(distance)



############################################################
# INTERPOLATION
############################################################

def interpolate_path(
        x,
        y,
        z,
        samples=1000
):
    """
    Resample trajectory evenly.
    """


    old=np.linspace(

        0,

        1,

        len(x)

    )


    new=np.linspace(

        0,

        1,

        samples

    )


    return (

        np.interp(new,old,x),

        np.interp(new,old,y),

        np.interp(new,old,z)

    )



############################################################
# CAMERA FLIGHT PATH
############################################################

def wormhole_flythrough(
        distance=30,
        points=1500
):
    """
    Generate cinematic camera path
    through a wormhole.
    """


    t=np.linspace(

        -1,

        1,

        points

    )


    radius=5*(1-t**2)+1


    angle=8*np.pi*t


    x=radius*np.cos(angle)

    y=radius*np.sin(angle)

    z=distance*t


    return x,y,z



############################################################
# ORBIT TRAIL
############################################################

def orbit_trail(
        radius,
        inclination=0,
        points=1000
):
    """
    Inclined orbital trajectory.
    """


    theta=np.linspace(

        0,

        2*np.pi,

        points

    )


    x=radius*np.cos(theta)


    y=radius*np.sin(theta)*np.cos(

        inclination

    )


    z=radius*np.sin(theta)*np.sin(

        inclination

    )


    return x,y,z



############################################################
# TRAJECTORY SUMMARY
############################################################

def trajectory_summary(
        x,
        y,
        z
):
    """
    Return trajectory statistics.
    """


    return {

        "points":

            len(x),


        "length":

            float(

                path_length(

                    x,

                    y,

                    z

                )

            ),


        "max_radius":

            float(

                np.max(

                    np.sqrt(

                        x**2+

                        y**2+

                        z**2

                    )

                )

            )

    }



############################################################
# EXPORT TRAJECTORY
############################################################

def export_trajectory(
        x,
        y,
        z,
        filename="trajectory.csv"
):
    """
    Save trajectory coordinates.
    """


    import pandas as pd


    df=pd.DataFrame(

        {

        "x":x,

        "y":y,

        "z":z

        }

    )


    df.to_csv(

        filename,

        index=False

    )


    return filename
