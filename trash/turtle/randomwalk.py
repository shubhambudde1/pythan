import turtle as t
import random

tim = t.Turtle()
colors = ["medium slate blue", "red", "chartreuse", "blue", "yellow", "violet red", "orange"]
directions = [0, 90, 180, 270]
tim.pensize(4)
tim.speed("fastest")

for _ in range(100):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))