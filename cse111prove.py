from tkinter import Tk, Frame, Canvas, BOTH, ARC
from numbers import Number
import math

from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500

    canvas = start_drawing("Scene", scene_width, scene_height)

    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_pine_tree(canvas, 550, 150, 250)
    draw_pine_tree(canvas, 250, 50, 200)
    draw_pine_tree(canvas, 450, 50, 200)
    draw_grid(canvas, scene_width, scene_height, 50)

    finish_drawing(canvas)

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="blue4")
    draw_oval(canvas, 350, 450, 500, 400, fill="slateGray4")
    draw_oval(canvas, 350, 450, 250, 500, fill="slateGray4")
    draw_oval(canvas, 150, 250, 250, 200, fill="slateGray4")
    draw_oval(canvas, 650, 450, 450, 250, fill="azure2")

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")

def draw_pine_tree(canvas, center_x, bottom, height):
    draw_rectangle(canvas, 100, 50, 120, 100, fill="saddleBrown")
    draw_polygon(canvas, 40, 90, 110, 300, 180, 90, fill="forestGreen")

    trunk_width = height / 10
    trunk_height = height / 8
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill="saddleBrown")

    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    skirt_center = center_x
    skirt_top = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, skirt_center, skirt_top, skirt_right, skirt_bottom, fill="forestGreen")

def draw_grid(canvas, width, height, interval):
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")
    
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")

main()