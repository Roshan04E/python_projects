import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(235, 243, 239), (194, 166, 108), (135, 167, 193), (49, 102, 145), (145, 90, 43),
              (10, 21, 54), (188, 156, 34), (224, 208, 115), (62, 23, 10), (184, 141, 165), (69, 119, 79)]

tim.penup()
tim.speed("fastest")
tim.setheading(225)
tim.forward(340)
tim.setheading(0)
tim.hideturtle()

dots_no = 100
for dots_count in range(1, dots_no + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dots_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
