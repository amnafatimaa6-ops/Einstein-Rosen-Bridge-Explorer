"""
lensing.py

Gravitational lensing utilities.

Includes:
- Einstein ring calculations
- Light deflection
- Star field distortion
- Magnification estimates
"""

import numpy as np



############################################################
# CONSTANTS
############################################################

G = 6.67430e-11

c = 299792458



############################################################
# EINSTEIN RADIUS
############################################################

def einstein_radius(
        mass,
        distances
):
    """
    Calculate angular Einstein radius.

    θE =
    sqrt(
        4GM/c² *
        Dls/(Dl Ds)
    )

    Parameters
    ----------
    mass:
        lens mass kg

    distances:
        tuple(Dl,Dls,Ds)

    """


    Dl,Dls,Ds = distances


    theta = np.sqrt(

        (

            4*G*mass

            /

            c**2

        )

        *

        (

            Dls

            /

            (Dl*Ds)

        )

    )


    return theta



############################################################
# DEFLECTION ANGLE
############################################################

def deflection_angle(
        mass,
        impact_parameter
):
    """
    Weak-field light bending.

    α = 4GM/(bc²)
    """


    return (

        4*G*mass

        /

        (

            impact_parameter*c**2

        )

    )



############################################################
# POINT MASS LENS
############################################################

def point_lens_mapping(
        x,
        y,
        strength=1.0
):
    """
    Map source position through
    simplified lens equation.
    """


    r=np.sqrt(

        x**2+y**2

    )


    r=np.maximum(

        r,

        1e-6

    )


    dx = strength*x/r**2

    dy = strength*y/r**2


    return (

        x+dx,

        y+dy

    )



############################################################
# STAR FIELD GENERATOR
############################################################

def generate_star_field(
        count=1000,
        size=10,
        seed=42
):
    """
    Create random background stars.
    """


    rng=np.random.default_rng(seed)


    x=rng.uniform(

        -size,

        size,

        count

    )


    y=rng.uniform(

        -size,

        size,

        count

    )


    brightness=rng.uniform(

        0.5,

        1.0,

        count

    )


    return {

        "x":x,

        "y":y,

        "brightness":brightness

    }



############################################################
# APPLY LENSING
############################################################

def apply_lensing(
        stars,
        strength=1.0
):
    """
    Distort star positions.
    """


    x=stars["x"]

    y=stars["y"]


    xl,yl = point_lens_mapping(

        x,

        y,

        strength

    )


    return {

        "x":xl,

        "y":yl,

        "brightness":

            stars["brightness"]




############################################################
# EINSTEIN RING GENERATOR
############################################################

def einstein_ring(
        radius=1.0,
        points=500
):
    """
    Generate Einstein ring coordinates.
    """


    theta=np.linspace(

        0,

        2*np.pi,

        points

    )


    x=radius*np.cos(theta)

    y=radius*np.sin(theta)


    return x,y



############################################################
# CRITICAL CURVE
############################################################

def critical_curve(
        radius=1.0,
        points=500
):
    """
    Critical curve where magnification
    theoretically diverges.
    """


    return einstein_ring(

        radius,

        points

    )



############################################################
# CAUSTIC POINTS
############################################################

def caustic_curve(
        size=0.5,
        points=500
):
    """
    Simplified point lens caustic.

    A point mass creates a point caustic.
    """

    theta=np.linspace(

        0,

        2*np.pi,

        points

    )


    x=np.zeros(points)

    y=np.zeros(points)


    return x,y



############################################################
# MAGNIFICATION
############################################################

def magnification(
        x,
        y,
        strength=1.0
):
    """
    Estimate lensing magnification.

    Simplified approximation.
    """


    r=np.sqrt(

        x**2+y**2

    )


    r=np.maximum(

        r,

        1e-6

    )


    mu = np.abs(

        1 +

        strength/r**2

    )


    return mu



############################################################
# LENSING MAP
############################################################

def create_lensing_map(
        size=10,
        resolution=300,
        strength=1.0
):
    """
    Create 2D distortion field.
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


    XL,YL=point_lens_mapping(

        X,

        Y,

        strength

    )


    return {

        "X":X,

        "Y":Y,

        "XL":XL,

        "YL":YL

    }



############################################################
# LIGHT RAY PATH
############################################################

def light_ray(
        impact_parameter,
        distance=20,
        points=500
):
    """
    Approximate curved light ray.
    """


    x=np.linspace(

        -distance,

        distance,

        points

    )


    curvature = (

        impact_parameter /

        (

            1+(x**2)

        )

    )


    y=curvature


    return x,y



############################################################
# MULTIPLE IMAGE POSITIONS
############################################################

def multiple_images(
        source_x,
        source_y,
        strength=1.0
):
    """
    Approximate two image positions
    from a point lens.
    """


    r=np.sqrt(

        source_x**2+

        source_y**2

    )


    if r == 0:

        return [

            (strength,0),

            (-strength,0)

        ]


    factor=strength/r


    return [

        (

            source_x*(1+factor),

            source_y*(1+factor)

        ),

        (

            source_x*(1-factor),

            source_y*(1-factor)

        )

    ]



############################################################
# SIMULATION STEP
############################################################

def lensing_step(
        stars,
        strength,
        frame
):
    """
    Generate animation frame.
    """


    changing_strength = (

        strength *

        (0.5+0.5*np.sin(frame))

    )


    return apply_lensing(

        stars,

        changing_strength

    )



############################################################
# LENSING STATISTICS
############################################################

def lensing_statistics(
        original,
        distorted
):
    """
    Compare image distortion.
    """


    displacement=np.sqrt(

        (

            distorted["x"]

            -

            original["x"]

        )**2

        +

        (

            distorted["y"]

            -

            original["y"]

        )**2

    )


    return {

        "average_shift":

            float(np.mean(displacement)),


        "maximum_shift":

            float(np.max(displacement)),


        "stars":

            len(displacement)

    }

    }
