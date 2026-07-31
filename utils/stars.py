"""
stars.py

Procedural astronomical star field generator.

Includes:
- 2D star fields
- 3D stellar distributions
- brightness models
- colour temperature approximation
"""

import numpy as np



############################################################
# STAR FIELD GENERATOR
############################################################

def generate_stars(
        count=5000,
        radius=100,
        seed=42
):
    """
    Generate random 3D stars.

    Returns:
        x,y,z,brightness
    """


    rng=np.random.default_rng(seed)


    x=rng.uniform(

        -radius,

        radius,

        count

    )


    y=rng.uniform(

        -radius,

        radius,

        count

    )


    z=rng.uniform(

        -radius,

        radius,

        count

    )


    brightness=rng.power(

        3,

        count

    )


    return {

        "x":x,

        "y":y,

        "z":z,

        "brightness":brightness

    }



############################################################
# SPHERICAL GALAXY DISTRIBUTION
############################################################

def galaxy_stars(
        count=10000,
        radius=50,
        arms=5,
        seed=10
):
    """
    Spiral galaxy style distribution.
    """


    rng=np.random.default_rng(seed)


    arm=rng.integers(

        0,

        arms,

        count

    )


    distance=rng.random(count)*radius


    angle=(

        arm *

        2*np.pi/arms

        +

        distance*0.15

        +

        rng.normal(

            0,

            0.2,

            count

        )

    )


    x=distance*np.cos(angle)

    y=distance*np.sin(angle)


    z=rng.normal(

        0,

        radius*0.05,

        count

    )


    brightness=np.exp(

        -distance/radius

    )


    return {

        "x":x,

        "y":y,

        "z":z,

        "brightness":brightness

    }



############################################################
# STAR TEMPERATURE
############################################################

def star_temperature(
        brightness
):
    """
    Approximate stellar temperature.

    Hotter stars:
    blue

    Cooler stars:
    red
    """


    return (

        3000

        +

        brightness*9000

    )



############################################################
# RGB STAR COLOUR
############################################################

def star_colour(
        temperature
):
    """
    Approximate RGB from temperature.
    """


    if temperature < 4000:

        return (

            1.0,

            0.6,

            0.4

        )


    elif temperature < 7000:

        return (

            1.0,

            1.0,

            0.8

        )


    else:

        return (

            0.7,

            0.8,

            1.0

        )



############################################################
# STAR SIZE
############################################################

def star_size(
        brightness,
        minimum=2,
        maximum=8
):
    """
    Convert brightness to point size.
    """


    return (

        minimum

        +

        brightness*(

            maximum-minimum

        )




  ############################################################
# MOVING STAR FIELD
############################################################

def move_stars(
        stars,
        velocity=(0,0,0),
        dt=1.0
):
    """
    Move stars through space.

    Used for camera fly-through effects.
    """


    x = stars["x"] + velocity[0]*dt

    y = stars["y"] + velocity[1]*dt

    z = stars["z"] + velocity[2]*dt


    return {

        "x":x,

        "y":y,

        "z":z,

        "brightness":
            stars["brightness"]

    }



############################################################
# NEBULA PARTICLES
############################################################

def generate_nebula(
        count=5000,
        radius=30,
        seed=20
):
    """
    Create cloud-like nebula particles.
    """


    rng=np.random.default_rng(seed)


    theta=rng.uniform(

        0,

        2*np.pi,

        count

    )


    r=rng.normal(

        radius,

        radius*0.25,

        count

    )


    x=r*np.cos(theta)

    y=r*np.sin(theta)


    z=rng.normal(

        0,

        radius*0.1,

        count

    )


    density=np.exp(

        -(r-radius)**2

        /

        (2*(radius*0.25)**2)

    )


    return {

        "x":x,

        "y":y,

        "z":z,

        "density":density

    }



############################################################
# STAR CLUSTER
############################################################

def globular_cluster(
        count=3000,
        radius=10,
        seed=5
):
    """
    Dense spherical star cluster.
    """


    rng=np.random.default_rng(seed)


    phi=rng.uniform(

        0,

        2*np.pi,

        count

    )


    costheta=rng.uniform(

        -1,

        1,

        count

    )


    theta=np.arccos(

        costheta

    )


    r=radius*(

        rng.random(count)**(1/3)

    )


    x=r*np.sin(theta)*np.cos(phi)

    y=r*np.sin(theta)*np.sin(phi)

    z=r*np.cos(theta)


    return {

        "x":x,

        "y":y,

        "z":z

    }



############################################################
# STAR FIELD STATISTICS
############################################################

def star_statistics(
        stars
):
    """
    Return star information.
    """


    return {

        "count":

            len(stars["x"]),


        "average_brightness":

            float(

                np.mean(

                    stars["brightness"]

                )

            ),


        "spatial_radius":

            float(

                np.max(

                    np.sqrt(

                        stars["x"]**2

                        +

                        stars["y"]**2

                        +

                        stars["z"]**2

                    )

                )

            )

    }



############################################################
# CAMERA DISTANCE FILTER
############################################################

def visible_stars(
        stars,
        camera_position,
        max_distance
):
    """
    Remove stars outside view range.
    """


    dx = stars["x"]-camera_position[0]

    dy = stars["y"]-camera_position[1]

    dz = stars["z"]-camera_position[2]


    distance=np.sqrt(

        dx**2+

        dy**2+

        dz**2

    )


    mask=distance < max_distance


    return {

        "x":stars["x"][mask],

        "y":stars["y"][mask],

        "z":stars["z"][mask],

        "brightness":
            stars["brightness"][mask]

    }



############################################################
# EXPORT STAR CATALOG
############################################################

def export_star_catalog(
        stars,
        filename="stars.csv"
):
    """
    Save generated stars.
    """


    import pandas as pd


    df=pd.DataFrame(

        {

        "x":stars["x"],

        "y":stars["y"],

        "z":stars["z"]

        }

    )


    df.to_csv(

        filename,

        index=False

    )


    return filename

    )
