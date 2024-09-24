from turtle import Turtle,Screen

MyScreen = Screen()
Turtelu = Turtle()


print(MyScreen.canvwidth)

Turtelu.shape('turtle')
Turtelu.color('#285078')

Turtelu.forward(100)
Turtelu.right(90)
Turtelu.forward(50)
Turtelu.home()

Raphelo = Turtle()
Raphelo.shape("turtle")
Raphelo.color("red")
Raphelo.penup()
Raphelo.goto(-150,150)
Raphelo.pendown()
Raphelo.pencolor("blue")

x=15

while x<50:
    Raphelo.circle(x)
    Turtelu.circle(x+5)
    x+=3

MyScreen.exitonclick()
