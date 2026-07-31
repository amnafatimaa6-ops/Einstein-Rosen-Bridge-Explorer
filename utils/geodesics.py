"""
geodesics.py

General Relativity trajectory utilities.

Contains:
- Schwarzschild geodesics
- Particle orbits
- Photon paths
- RK4 numerical integration
"""

import numpy as np



############################################################
# CONSTANTS
############################################################

G = 6.67430e-11
c = 299792458



############################################################
# SCHWARZSCHILD RADIUS
############################################################

def schwarzschild_radius(
        mass
):
    """
    Calculate Schwarzschild radius.

    mass:
        SI kilograms
    """

    return (

        2*G*mass

    )/(c**2)



############################################################
# EFFECTIVE POTENTIAL
############################################################

def effective_potential(
        r,
        mass,
        angular_momentum
):
    """
    Schwarzschild effective potential.

    Used for orbital analysis.
    """


    rs=schwarzschild_radius(mass)


    V = (

        -G*mass/r

        +

        angular_momentum**2/(2*r**2)

        -

        G*mass*
        angular_momentum**2
        /

        (c**2*r**3)

    )


    return V



############################################################
# RADIAL ACCELERATION
############################################################

def radial_acceleration(
        r,
        mass,
        angular_momentum
):
    """
    Approximate radial acceleration.
    """


    return (

        -G*mass/r**2

        +

        angular_momentum**2/r**3

        -

        3*G*mass*
        angular_momentum**2
        /

        (c**2*r**4)

    )



############################################################
# STATE DERIVATIVE
############################################################

def geodesic_derivative(
        state,
        mass,
        angular_momentum
):
    """
    Differential equations.

    State:

    [r, radial_velocity]

    """

    r,v = state


    drdt = v


    dvdt = radial_acceleration(

        r,

        mass,

        angular_momentum

    )


    return np.array(

        [

            drdt,

            dvdt

        ]

    )



############################################################
# RK4 STEP
############################################################

def rk4_step(
        state,
        dt,
        mass,
        angular_momentum
):
    """
    Fourth-order Runge Kutta integration.
    """


    k1 = geodesic_derivative(

        state,

        mass,

        angular_momentum

    )


    k2 = geodesic_derivative(

        state + dt*k1/2,

        mass,

        angular_momentum

    )


    k3 = geodesic_derivative(

        state + dt*k2/2,

        mass,

        angular_momentum

    )


    k4 = geodesic_derivative(

        state + dt*k3,

        mass,

        angular_momentum

    )


    return (

        state

        +

        dt/6 *

        (

            k1+

            2*k2+

            2*k3+

            k4

        )






############################################################
# GENERATE RADIAL TRAJECTORY
############################################################

def integrate_geodesic(
        initial_state,
        steps,
        dt,
        mass,
        angular_momentum
):
    """
    Integrate a geodesic using RK4.

    Returns trajectory array.
    """


    state=np.array(

        initial_state,

        dtype=float

    )


    trajectory=[]


    for _ in range(steps):

        trajectory.append(

            state.copy()

        )


        state=rk4_step(

            state,

            dt,

            mass,

            angular_momentum

        )


        # prevent numerical collapse

        if state[0] <= 0:

            break



    return np.array(trajectory)



############################################################
# CIRCULAR ORBIT VELOCITY
############################################################

def circular_orbit_velocity(
        radius,
        mass
):
    """
    Newtonian approximation for circular orbit.
    """


    return np.sqrt(

        G*mass/radius

    )



############################################################
# ISCO RADIUS
############################################################

def isco_radius(
        mass
):
    """
    Schwarzschild ISCO.

    r = 6GM/c²
    """


    return (

        6*G*mass/c**2

    )



############################################################
# PHOTON SPHERE
############################################################

def photon_sphere_radius(
        mass
):
    """
    Radius where photons can orbit.
    """


    return (

        3*G*mass/c**2

    )



############################################################
# PHOTON DEFLECTION
############################################################

def photon_deflection_angle(
        mass,
        impact_parameter
):
    """
    Weak field gravitational lensing.

    alpha = 4GM/(bc²)
    """


    return (

        4*G*mass

        /

        (

            impact_parameter*c**2

        )

    )



############################################################
# PHOTON TRAJECTORY
############################################################

def photon_path(
        impact_parameter,
        length=100,
        points=1000
):
    """
    Simple photon bending trajectory.

    Used for visualization.
    """


    x=np.linspace(

        -length,

        length,

        points

    )


    y=(

        impact_parameter

        /

        (

            1+

            (x/impact_parameter)**2

        )

    )


    return x,y



############################################################
# ORBIT GENERATOR
############################################################

def generate_orbit(
        radius,
        mass,
        revolutions=3,
        points=1000
):
    """
    Generate circular orbit.
    """


    theta=np.linspace(

        0,

        2*np.pi*revolutions,

        points

    )


    x=radius*np.cos(theta)

    y=radius*np.sin(theta)


    return x,y



############################################################
# TRAJECTORY TO 3D
############################################################

def trajectory_3d(
        x,
        y,
        z_value=0
):
    """
    Convert 2D path into 3D.
    """


    z=np.ones_like(x)*z_value


    return x,y,z



############################################################
# ORBIT STABILITY
############################################################

def orbit_stability(
        radius,
        mass
):
    """
    Determine approximate stability.

    Stable:
        r > ISCO

    """

    isco=isco_radius(mass)


    if radius > isco:

        return "Stable Orbit"

    elif radius == isco:

        return "Marginal Stability"

    else:

        return "Unstable Orbit"



############################################################
# TRAJECTORY STATISTICS
############################################################

def trajectory_statistics(
        trajectory
):
    """
    Return simulation information.
    """


    return {

        "steps":

            len(trajectory),


        "initial_radius":

            float(trajectory[0][0]),


        "final_radius":

            float(trajectory[-1][0]),


        "minimum_radius":

            float(
                np.min(
                    trajectory[:,0]
                )
            )

    }

    )
