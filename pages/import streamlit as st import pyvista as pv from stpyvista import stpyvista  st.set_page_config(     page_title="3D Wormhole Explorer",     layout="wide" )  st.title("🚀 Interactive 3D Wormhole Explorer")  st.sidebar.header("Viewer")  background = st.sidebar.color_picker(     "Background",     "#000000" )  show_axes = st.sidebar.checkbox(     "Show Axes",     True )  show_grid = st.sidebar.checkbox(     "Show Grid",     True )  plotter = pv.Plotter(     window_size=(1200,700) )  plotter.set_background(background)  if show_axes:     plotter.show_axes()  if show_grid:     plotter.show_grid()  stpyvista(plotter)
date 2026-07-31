import streamlit as st
import numpy as np
import pyvista as pv
from stpyvista import stpyvista

st.set_page_config(
    page_title="3D Wormhole Explorer",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Interactive 3D Wormhole Explorer")

st.markdown("""
Explore an Einstein-Rosen Bridge in true 3D.

Rotate

Zoom

Pan

Inspect

Modify parameters live.
""")

########################################################
# SIDEBAR
########################################################

st.sidebar.header("Geometry")

mass = st.sidebar.slider(
    "Black Hole Mass",
    1.0,
    10.0,
    2.0,
    0.1
)

radius = st.sidebar.slider(
    "Maximum Radius",
    8.0,
    25.0,
    15.0,
    0.5
)

resolution = st.sidebar.slider(
    "Mesh Resolution",
    80,
    300,
    180,
    10
)

########################################################

st.sidebar.header("Appearance")

surface_colour = st.sidebar.selectbox(

    "Surface",

    [

        "viridis",

        "plasma",

        "inferno",

        "turbo",

        "coolwarm",

        "cividis"

    ]

)

opacity = st.sidebar.slider(

    "Opacity",

    0.2,

    1.0,

    1.0,

    0.05

)

wireframe = st.sidebar.checkbox(

    "Wireframe",

    False

)

show_axes = st.sidebar.checkbox(

    "Show Axes",

    True

)

show_grid = st.sidebar.checkbox(

    "Show Grid",

    True

)

########################################################

st.sidebar.header("Environment")

background = st.sidebar.color_picker(

    "Background",

    "#000000"

)

stars = st.sidebar.checkbox(

    "Stars",

    True

)

event_horizon = st.sidebar.checkbox(

    "Event Horizon",

    True

)

lighting = st.sidebar.checkbox(

    "Lighting",

    True

)

########################################################
# CREATE PLOTTER
########################################################

plotter = pv.Plotter(
    window_size=(1300,800)
)

plotter.set_background(background)

if show_axes:
    plotter.show_axes()

if show_grid:
    plotter.show_grid()

########################################################
# GEOMETRY
########################################################

rs = 2 * mass

r = np.linspace(
    rs + 0.01,
    radius,
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

upper = pv.StructuredGrid(
    X,
    Y,
    Z
)

lower = pv.StructuredGrid(
    X,
    Y,
    -Z
)

########################################################
# SURFACES
########################################################

plotter.add_mesh(

    upper,

    cmap=surface_colour,

    opacity=opacity,

    smooth_shading=True,

    show_edges=wireframe

)

plotter.add_mesh(

    lower,

    cmap=surface_colour,

    opacity=opacity,

    smooth_shading=True,

    show_edges=wireframe

)

########################################################
# EVENT HORIZON
########################################################

if event_horizon:

    horizon = pv.Sphere(

        radius=rs,

        theta_resolution=120,

        phi_resolution=120

    )

    plotter.add_mesh(

        horizon,

        color="black",

        opacity=0.7,

        smooth_shading=True

    )

########################################################
# STAR FIELD
########################################################

if stars:

    pts = np.random.uniform(

        -120,

        120,

        (7000,3)

    )

    cloud = pv.PolyData(pts)

    plotter.add_mesh(

        cloud,

        color="white",

        point_size=2,

        render_points_as_spheres=True

    )

########################################################
# LIGHTING
########################################################

if lighting:

    light = pv.Light(

        position=(25,25,35),

        focal_point=(0,0,0),

        intensity=2.5

    )

    plotter.add_light(light)

    light2 = pv.Light(

        position=(-25,-25,20),

        focal_point=(0,0,0),

        intensity=1.3

    )
########################################################
# CAMERA CONTROLS
########################################################

st.sidebar.header("Camera")

camera_distance = st.sidebar.slider(
    "Camera Distance",
    5.0,
    40.0,
    18.0,
    0.5
)

camera_height = st.sidebar.slider(
    "Camera Height",
    -20.0,
    20.0,
    8.0,
    0.5
)

camera_angle = st.sidebar.slider(
    "Camera Angle",
    0,
    360,
    45
)

orbit = st.sidebar.checkbox(
    "Orbit Camera",
    False
)

orbit_speed = st.sidebar.slider(
    "Orbit Speed",
    1,
    20,
    5
)

########################################################
# CLIPPING PLANE
########################################################

st.sidebar.header("Cross Section")

enable_clip = st.sidebar.checkbox(
    "Enable Clipping Plane",
    False
)

clip_axis = st.sidebar.selectbox(
    "Axis",
    ["X", "Y", "Z"]
)

clip_value = st.sidebar.slider(
    "Plane Position",
    -20.0,
    20.0,
    0.0,
    0.25
)

########################################################
# THROAT GLOW
########################################################

throat_glow = st.sidebar.checkbox(
    "Glow at Throat",
    True
)

if throat_glow:

    glow = pv.Sphere(
        radius=rs*1.1,
        theta_resolution=100,
        phi_resolution=100
    )

    plotter.add_mesh(
        glow,
        color="cyan",
        opacity=0.12,
        smooth_shading=True
    )

########################################################
# CLIPPING
########################################################

if enable_clip:

    origin = (0,0,0)

    if clip_axis == "X":
        normal = (1,0,0)

    elif clip_axis == "Y":
        normal = (0,1,0)

    else:
        normal = (0,0,1)

    upper_clip = upper.clip(
        normal=normal,
        origin=origin,
        invert=False
    )

    lower_clip = lower.clip(
        normal=normal,
        origin=origin,
        invert=False
    )

    plotter.clear()

    plotter.set_background(background)

    if show_axes:
        plotter.show_axes()

    if show_grid:
        plotter.show_grid()

    plotter.add_mesh(
        upper_clip,
        cmap=surface_colour,
        opacity=opacity,
        smooth_shading=True,
        show_edges=wireframe
    )

    plotter.add_mesh(
        lower_clip,
        cmap=surface_colour,
        opacity=opacity,
        smooth_shading=True,
        show_edges=wireframe
    )

########################################################
# CAMERA POSITION
########################################################

angle = np.radians(camera_angle)

cam_x = camera_distance*np.cos(angle)
cam_y = camera_distance*np.sin(angle)
cam_z = camera_height

plotter.camera.position = (
    cam_x,
    cam_y,
    cam_z
)

plotter.camera.focal_point = (
    0,
    0,
    0
)

plotter.camera.up = (
    0,
    0,
    1
)

########################################################
# AUTO ORBIT
########################################################

if orbit:

    new_angle = np.radians(
        camera_angle + orbit_speed
    )

    plotter.camera.position = (

        camera_distance*np.cos(new_angle),

        camera_distance*np.sin(new_angle),

        camera_height

    )

########################################################
# RENDER EFFECTS
########################################################

plotter.enable_anti_aliasing()

plotter.enable_eye_dome_lighting()

plotter.enable_parallel_projection(False)

########################################################
# DISPLAY VIEWER
########################################################

stpyvista(
    plotter,
    key="wormhole_viewer"
)

########################################################
# INFORMATION PANEL
########################################################

st.divider()

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "Mass",
        f"{mass:.2f}"
    )

with c2:
    st.metric(
        "Schwarzschild Radius",
        f"{rs:.2f}"
    )

with c3:
    st.metric(
        "Resolution",
        resolution
    )

with c4:
    st.metric(
        "Vertices",
        f"{resolution*resolution:,}"
    )

########################################################
# LIVE COORDINATES
########################################################

st.subheader("Current Camera")

st.write(
    {
        "x":round(cam_x,2),
        "y":round(cam_y,2),
        "z":round(cam_z,2)
    }
)

########################################################
# EXPORT PLACEHOLDER
########################################################

if st.button("Export Screenshot"):

    st.info(
        "Screenshot export will be implemented in the next version."
    )

########################################################
# ABOUT
########################################################

with st.expander("About this Explorer"):

    st.markdown("""

This explorer renders an **Einstein-Rosen Bridge**
using PyVista and VTK.

Features

- Interactive GPU rendering
- True 3D geometry
- Orbit camera
- Clipping planes
- Event horizon
- Procedural star field
- Adjustable geometry
- Smooth lighting
- Scientific visualization

Future versions will include

- Photon trajectories

- Geodesics

- Fly-through animation

- Curvature heat map

- Gravitational lensing

- White hole mode

- Morris-Thorne comparison

- Spacecraft simulation

""")
    plotter.add_light(light2)
