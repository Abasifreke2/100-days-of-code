import turtle
from turtle import Screen
import random

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (125, 36, 24), (187, 158, 51), (170, 104, 56),
              (5, 57, 83), (222, 223, 226), (200, 216, 204), (108, 67, 85), (39, 36, 35), (86, 142, 59), (20, 122, 176),
              (110, 161, 175), (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186),
              (209, 200, 115), (179, 174, 177), (151, 176, 165), (93, 142, 156), (28, 80, 59), (194, 190, 192),
              (17, 78, 99), (212, 184, 174), (142, 117, 123), (175, 198, 204)]
screen = Screen()
screen.colormode(255)
turtle.penup()
turtle.setpos(-250, -250)
turtle.speed("fastest")
def create_dots():
    random_color = random.choice(color_list)
    turtle.dot(20,random_color)
    turtle.penup()
    turtle.fd(50)


y = -250
for row in range(10):
    for circle in range(10):
        create_dots()
    y += 50
    turtle.teleport(x=-250,y=y)



screen.exitonclick()
