from tkinter import Tk, Frame, Canvas, BOTH, ARC
from numbers import Number
import math

from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_pine_tree(canvas, 240, 320)
    draw_pine_tree(canvas, 160, 280)
    draw_pine_tree(canvas, 100, 250)
    draw_pine_tree(canvas, 500, 350)
    draw_pine_tree(canvas, 600, 280)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def draw_pine_trees(canvas):
    """Draw three pine trees, each at a fixed location."""

    # Draw a tree.
    draw_rectangle(canvas, 300, 70, 320, 120, fill="brown")
    draw_polygon(canvas, 240, 110, 310, 320, 380, 110,
            fill="forestGreen")

    # Draw another tree.
    draw_rectangle(canvas, 200, 60, 220, 110, fill="brown")
    draw_polygon(canvas, 140, 100, 210, 310, 280, 100,
            fill="forestGreen")

    # Draw a third tree.
    draw_rectangle(canvas, 100, 50, 120, 100, fill="brown")
    draw_polygon(canvas, 40, 90, 110, 300, 180, 90,
            fill="forestGreen")

    # Compute the coordinates of the skirt and trunk.
    skirt_left  = peak_x - 70
    skirt_right = peak_x + 70
    skirt_bottom = peak_y - 210
    trunk_left  = peak_x - 10
    trunk_right = peak_x + 10
    trunk_bottom = peak_y - 260

    # Draw the tree trunk.
    draw_rectangle(canvas, trunk_left, trunk_bottom,
            trunk_right, skirt_bottom, fill="brown")

    # Draw the tree skirt.
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,
            skirt_right, skirt_bottom, fill="forestGreen")

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

main()