"""
metrics.py

Physics and simulation metrics.

Contains:
- Black hole measurements
- Wormhole geometry metrics
- Simulation statistics
- Performance calculations
"""

import numpy as np



############################################################
# CONSTANTS
############################################################

G = 6.67430e-11

c = 299792458

M_sun = 1.98847e30



############################################################
# SCHWARZSCHILD RADIUS
############################################################

def schwarzschild_radius(
        solar_mass
):
    """
    Schwarzschild radius in meters.

    Input:
        solar masses
    """


    mass = solar_mass*M_sun


    return (

        2*G*mass/c**2

    )



############################################################
# BLACK HOLE DENSITY
############################################################

def black_hole_density(
        solar_mass
):
    """
    Average density inside
    Schwarzschild radius.
    """


    mass=solar_mass*M_sun


    radius=schwarzschild_radius(

        solar_mass

    )


    volume=(

        4/3*np.pi*radius**3

    )


    return mass/volume



############################################################
# SURFACE GRAVITY
############################################################

def surface_gravity(
        solar_mass
):
    """
    Surface gravity at event horizon.
    """


    mass=solar_mass*M_sun


    radius=schwarzschild_radius(

        solar_mass

    )


    return (

        G*mass/radius**2

    )



############################################################
# ESCAPE VELOCITY FRACTION
############################################################

def escape_velocity_fraction(
        solar_mass,
        radius_factor=1
):
    """
    Escape velocity as fraction of c.

    radius_factor:
        multiples of Schwarzschild radius
    """


    radius=(

        schwarzschild_radius(

            solar_mass

        )

        *

        radius_factor

    )


    mass=solar_mass*M_sun


    velocity=np.sqrt(

        2*G*mass/radius

    )
############################################################
# WORMHOLE THROAT METRICS
############################################################

def throat_metrics(
        radius,
        curvature
):
    """
    Analyse wormhole throat geometry.
    """


    return {

        "throat_radius":

            float(radius),


        "curvature":

            float(curvature),


        "flare_out":

            radius > 0

    }



############################################################
# EMBEDDING SURFACE METRICS
############################################################

def embedding_metrics(
        X,
        Y,
        Z
):
    """
    Calculate embedding surface properties.
    """


    radius=np.sqrt(

        X**2+

        Y**2

    )


    return {

        "surface_points":

            X.size,


        "maximum_height":

            float(np.max(Z)),


        "minimum_height":

            float(np.min(Z)),


        "maximum_radius":

            float(np.max(radius)),


        "minimum_radius":

            float(np.min(radius))

    }



############################################################
# CURVATURE ESTIMATION
############################################################

def curvature_metric(
        X,
        Y,
        Z
):
    """
    Approximate curvature strength.
    """


    dx=np.gradient(

        Z,

        axis=0

    )


    dy=np.gradient(

        Z,

        axis=1

    )


    curvature=np.sqrt(

        dx**2+

        dy**2

    )


    return {

        "mean_curvature":

            float(np.mean(curvature)),


        "maximum_curvature":

            float(np.max(curvature))

    }



############################################################
# TRAJECTORY METRICS
############################################################

def trajectory_metrics(
        x,
        y,
        z
):
    """
    Analyse particle trajectory.
    """


    radius=np.sqrt(

        x**2+

        y**2+

        z**2

    )


    distance=np.sqrt(

        np.diff(x)**2+

        np.diff(y)**2+

        np.diff(z)**2

    )


    return {

        "points":

            len(x),


        "travel_distance":

            float(np.sum(distance)),


        "closest_approach":

            float(np.min(radius)),


        "maximum_distance":

            float(np.max(radius))

    }



############################################################
# SIMULATION PERFORMANCE
############################################################

def simulation_metrics(
        frames,
        points
):
    """
    Estimate simulation complexity.
    """


    return {

        "frames":

            frames,


        "objects_per_frame":

            points,


        "total_render_points":

            frames*points

    }



############################################################
# WORMHOLE COMPARISON
############################################################

def compare_wormholes(
        einstein_rosen,
        morris_thorne
):
    """
    Compare two wormhole models.
    """


    return {

        "ER_points":

            len(einstein_rosen),


        "MT_points":

            len(morris_thorne),


        "difference":

            abs(

                len(einstein_rosen)

                -

                len(morris_thorne)

            )

    }



############################################################
# REPORT GENERATOR
############################################################

def generate_report(
        name,
        metrics,
        filename="simulation_report.txt"
):
    """
    Save simulation summary.
    """


    with open(

        filename,

        "w"

    ) as file:


        file.write(

            f"{name}\n"

        )


        file.write(

            "="*40+"\n"

        )


        for key,value in metrics.items():

            file.write(

                f"{key}: {value}\n"

            )


    return filename



############################################################
# DATA QUALITY CHECK
############################################################

def validate_geometry(
        X,
        Y,
        Z
):
    """
    Check geometry arrays.
    """


    return {

        "valid":

            (

                X.shape==Y.shape

                and

                Y.shape==Z.shape

            ),


        "nan_values":

            int(

                np.isnan(Z).sum()

            )

    }


    return velocity/c
