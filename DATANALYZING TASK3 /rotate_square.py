import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 1. Define the 4 corners of a square (Z is 0 because it's flat)
square_points = np.array([
    [-0.5, -0.5, 0.0],
    [ 0.5, -0.5, 0.0],
    [ 0.5,  0.5, 0.0],
    [-0.5,  0.5, 0.0]
])

# Which corners connect to form the outline of the square
lines = [[0, 1], [1, 2], [2, 3], [3, 0]]

# 2. Simple math functions to rotate around X, Y, and Z axes
def rotate_x(angle):
    rad = np.radians(angle)
    c, s = np.cos(rad), np.sin(rad)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])

def rotate_y(angle):
    rad = np.radians(angle)
    c, s = np.cos(rad), np.sin(rad)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])

def rotate_z(angle):
    rad = np.radians(angle)
    c, s = np.cos(rad), np.sin(rad)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

# 3. The function that draws the square every time you move a slider
def update_plot(val):
    ax.cla() # Clear the old drawing
    
    # Keep the grid box the same size (-1 to 1) so it doesn't zoom in/out
    ax.set_xlim([-1.0, 1.0])
    ax.set_ylim([-1.0, 1.0])
    ax.set_zlim([-1.0, 1.0])
    
    # Read the current angles from the sliders
    ang_x = slider_x.val
    ang_y = slider_y.val
    ang_z = slider_z.val
    
    # Combine all the rotations into one math step
    matrix = rotate_z(ang_z) @ rotate_y(ang_y) @ rotate_x(ang_x)
    
    # Apply the rotation to our original square points
    rotated_points = square_points @ matrix.T
    
    # Draw the green dots at the corners
    ax.scatter(rotated_points[:,0], rotated_points[:,1], rotated_points[:,2], color='green', s=60)
    
    # Draw the dashed lines connecting the dots
    for p1, p2 in lines:
        x_vals = [rotated_points[p1, 0], rotated_points[p2, 0]]
        y_vals = [rotated_points[p1, 1], rotated_points[p2, 1]]
        z_vals = [rotated_points[p1, 2], rotated_points[p2, 2]]
        ax.plot3D(x_vals, y_vals, z_vals, color='gray', linestyle='--')
        
    fig.canvas.draw_idle()

# 4. Setup the main window and UI
fig = plt.figure(figsize=(6, 7))
fig.canvas.manager.set_window_title('Rotate The Square')

# Create the 3D viewing box
ax = fig.add_axes([0.1, 0.35, 0.8, 0.6], projection='3d')

# Create spaces for the sliders at the bottom
ax_x = fig.add_axes([0.25, 0.20, 0.5, 0.03])
ax_y = fig.add_axes([0.25, 0.13, 0.5, 0.03])
ax_z = fig.add_axes([0.25, 0.06, 0.5, 0.03])

# Add the sliders (starting with the exact values from the assignment picture)
slider_x = Slider(ax_x, 'X°:', 0, 360, valinit=68.8)
slider_y = Slider(ax_y, 'Y°:', 0, 360, valinit=132.4)
slider_z = Slider(ax_z, 'Z°:', 0, 360, valinit=227.6)

# Tell the sliders to run the update_plot function whenever they are moved
slider_x.on_changed(update_plot)
slider_y.on_changed(update_plot)
slider_z.on_changed(update_plot)

# Draw it for the first time
update_plot(0)

# Show the window
plt.show()