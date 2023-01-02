
import turtle
(0,-200)

wn = turtle.Screen()
wn.bgcolor("black")

ball = turtle.Turtle()
ball.speed(1000)
ball.color("green")
ball.shape("circle")
ball.penup()
ball.goto(0,100)
ball.goto(0,200)

ball.speed(0)
ball.dy = -1
ball.dx = 2

gravity = 1

while True:
  ball.dy-= gravity
  ball.sety(ball.ycor()+ ball.dy)
  ball.setx(ball.xcor()+ ball.dx)

  if ball.ycor() < -200:
    ball.dy *= -1

  if ball.xcor() > 310:
    ball.dx *= -1

  if ball.xcor() < -310:
    ball.dx *= -1

wn.mainloop()