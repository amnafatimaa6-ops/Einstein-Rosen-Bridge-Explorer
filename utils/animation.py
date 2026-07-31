"""
animation.py

Animation utilities for the
Einstein-Rosen Bridge Explorer.

Contains:
- mesh rotation animation
- trajectory frames
- camera movement
- time evolution helpers
"""

import numpy as np



############################################################
# FRAME GENERATOR
############################################################

def generate_frames(
        total_frames=100
):
    """
    Generate normalized animation time.
    """


    return np.linspace(

        0,

        1,

        total_frames

    )



############################################################
# ROTATION ANGLES
############################################################

def rotation_animation(
        frames,
        speed=2
):
    """
    Generate rotating angles.
    """


    angles=[]


    for frame in frames:

        angles.append(

            frame *

            360 *

            speed

        )


    return np.array(angles)



############################################################
# ROTATE POINTS
############################################################

def rotate_points(
        x,
        y,
        z,
        angle
):
    """
    Rotate 3D points around z-axis.
    """


    theta=np.radians(angle)


    xr=(

        x*np.cos(theta)

        -

        y*np.sin(theta)

    )


    yr=(

        x*np.sin(theta)

        +

        y*np.cos(theta)

    )


    return xr,y,z



############################################################
# TRAJECTORY FRAMES
############################################################

def trajectory_frames(
        x,
        y,
        z,
        frame_count=100
):
    """
    Split trajectory into animation frames.
    """


    frames=[]


    length=len(x)


    step=max(

        1,

        length//frame_count

    )


    for i in range(

        0,

        length,

        step

    ):

        frames.append(

            (

                x[:i],

                y[:i],

                z[:i]

            )

        )


    return frames



############################################################
# CAMERA MOTION
############################################################

def camera_motion(
        radius=20,
        height=5,
        frames=200
):
    """
    Circular camera movement.
    """


    theta=np.linspace(

        0,

        2*np.pi,

        frames

    )


    x=radius*np.cos(theta)

    y=radius*np.sin(theta)

    z=np.ones_like(theta)*height


    return x,y,z



############################################################
# PULSE EFFECT
############################################################

def pulse(
        frame,
        frequency=2,
        amplitude=0.1
):
    """
    Smooth pulsating effect.
    """


    return (

        1+

        amplitude*np.sin(

            frequency*frame*2*np.pi

        )








############################################################
# ORBITING PARTICLES
############################################################

def orbit_particles(
        radius=10,
        count=500,
        frame=0,
        speed=1
):
    """
    Generate moving particles around
    a black hole or wormhole.
    """


    theta=np.linspace(

        0,

        2*np.pi,

        count

    )


    theta += frame*speed


    x=radius*np.cos(theta)

    y=radius*np.sin(theta)


    z=np.zeros_like(theta)


    return x,y,z



############################################################
# WORMHOLE THROAT GLOW
############################################################

def throat_glow(
        frame,
        base_intensity=1.0
):
    """
    Pulsating wormhole throat illumination.
    """


    return (

        base_intensity *

        (

            0.5

            +

            0.5*np.sin(

                frame*2*np.pi

            )

        )

    )



############################################################
# SCALE ANIMATION
############################################################

def scale_animation(
        frames,
        minimum=0.9,
        maximum=1.1
):
    """
    Create breathing/expansion animation.
    """


    return (

        minimum

        +

        (

            maximum-minimum

        )

        *

        (

            0.5

            +

            0.5*np.sin(

                frames*2*np.pi

            )

        )

    )



############################################################
# PLOTLY FRAME CREATOR
############################################################

def create_plotly_frames(
        x,
        y,
        z,
        frame_count=50
):
    """
    Create Plotly animation frame data.
    """


    frames=[]


    length=len(x)


    step=max(

        1,

        length//frame_count

    )


    for i in range(

        step,

        length,

        step

    ):


        frames.append(

            {

            "x":x[:i],

            "y":y[:i],

            "z":z[:i]

            }

        )


    return frames



############################################################
# PYVISTA ROTATION HELPER
############################################################

def pyvista_rotation(
        mesh,
        angle,
        axis="z"
):
    """
    Rotate PyVista mesh.

    Requires pyvista object.
    """


    if axis=="x":

        mesh.rotate_x(

            angle,

            inplace=True

        )


    elif axis=="y":

        mesh.rotate_y(

            angle,

            inplace=True

        )


    elif axis=="z":

        mesh.rotate_z(

            angle,

            inplace=True

        )


    return mesh



############################################################
# ANIMATION TIMER
############################################################

class AnimationController:

    """
    Simple animation controller.
    """


    def __init__(
            self,
            fps=30
    ):

        self.fps=fps

        self.frame=0



    def update(self):

        self.frame += 1


        return self.frame



    def reset(self):

        self.frame=0



    def time(self):

        return (

            self.frame/self.fps

        )



############################################################
# LOOP GENERATOR
############################################################

def animation_loop(
        frames
):
    """
    Infinite animation iterator.
    """


    while True:

        for frame in frames:

            yield frame



############################################################
# EXPORT ANIMATION DATA
############################################################

def save_animation_data(
        frames,
        filename="animation.npy"
):
    """
    Save animation frames.
    """


    np.save(

        filename,

        frames

    )


    return filename

    )
