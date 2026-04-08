import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Cube ke 8 corners (vertices) define kiye hain
cube_points = np.array([
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
])

# Cube ka size bada karne ke liye 10 se multiply kiya
cube_points = cube_points * 10

# Lines jo corners ko milayengi
lines = [
    [0, 1], [1, 2], [2, 3], [3, 0], # Base
    [4, 5], [5, 6], [6, 7], [7, 4], # Top
    [0, 4], [1, 5], [2, 6], [3, 7]  # Sides
]

def rotation_x(angle_deg):
    # X-axis par ghumane ka math
    angle_rad = np.radians(angle_deg)
    c, s = np.cos(angle_rad), np.sin(angle_rad)
    return np.array([
        [1, 0, 0],
        [0, c, -s],
        [0, s, c]
    ])

def rotation_y(angle_deg):
    # Y-axis par ghumane ka math
    angle_rad = np.radians(angle_deg)
    c, s = np.cos(angle_rad), np.sin(angle_rad)
    return np.array([
        [c, 0, s],
        [0, 1, 0],
        [-s, 0, c]
    ])

def rotation_z(angle_deg):
    # Z-axis par ghumane ka math
    angle_rad = np.radians(angle_deg)
    c, s = np.cos(angle_rad), np.sin(angle_rad)
    return np.array([
        [c, -s, 0],
        [s, c, 0],
        [0, 0, 1]
    ])

def draw_cube(val):
    # Purana cube clear karo
    ax.cla()
    
    # Limits set karna (Screen par fit rakhne ke liye)
    ax.set_xlim([-30, 30])
    ax.set_ylim([-30, 30])
    ax.set_zlim([-30, 30])
    
    # Sliders se current angle lena
    angle_x = slider_x.val
    angle_y = slider_y.val
    angle_z = slider_z.val
    
    # Rotation matrices calculate karna
    mat_x = rotation_x(angle_x)
    mat_y = rotation_y(angle_y)
    mat_z = rotation_z(angle_z)
    
    # Teeno rotations ko combine karna
    combined_matrix = mat_z @ mat_y @ mat_x
    
    # Har point ko ghumana
    rotated_points = cube_points @ combined_matrix.T
    
    # Naye points par lines draw karna
    for p1_idx, p2_idx in lines:
        x_coords = [rotated_points[p1_idx, 0], rotated_points[p2_idx, 0]]
        y_coords = [rotated_points[p1_idx, 1], rotated_points[p2_idx, 1]]
        z_coords = [rotated_points[p1_idx, 2], rotated_points[p2_idx, 2]]
        ax.plot3D(x_coords, y_coords, z_coords, color='blue')
        
    fig.canvas.draw_idle()

# Main application window setup
fig = plt.figure(figsize=(7, 8))
fig.canvas.manager.set_window_title('Cube Rotator')

# 3D plot area
ax = fig.add_axes([0.1, 0.35, 0.8, 0.6], projection='3d')

# Sliders banane ki jagah
ax_x = fig.add_axes([0.25, 0.20, 0.5, 0.03])
ax_y = fig.add_axes([0.25, 0.13, 0.5, 0.03])
ax_z = fig.add_axes([0.25, 0.06, 0.5, 0.03])

# Sliders initialize karna 
slider_x = Slider(ax_x, 'X°:', 0, 360, valinit=74.1)
slider_y = Slider(ax_y, 'Y°:', 0, 360, valinit=15.9)
slider_z = Slider(ax_z, 'Z°:', 0, 360, valinit=105.9)

# Jab slider move ho toh draw_cube function call ho
slider_x.on_changed(draw_cube)
slider_y.on_changed(draw_cube)
slider_z.on_changed(draw_cube)

# Pehli baar draw karne ke liye call kiya
draw_cube(0)

plt.show()