import turtle as t
import random


colors = ["medium slate blue", "red", "chartreuse", "blue", "yellow", "violet red", "orange"]
num_sides = 10;
tim = t.Turtle()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
for shape_side_n in range(3, 10):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)