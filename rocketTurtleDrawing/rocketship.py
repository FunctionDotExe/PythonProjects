import turtle
rocket = turtle.Turtle()
rocket.ht()

#Allow the user to choose if they want the text to match the criteria or the provided drawing
print("\033[1;30;43mThe criteria \n \"Draw Text: “We’re Going to the Moon!” /3\" \ndoesn't match the text shown in the provided drawing, which reads\n \"We're blasting to the moon!\" \033[0m\nWhich one should this program follow? \nA. Follow criteria/rubric \nB. Follow provided drawing")

text_choice = input("Type the letter corresponding to your choice and press ENTER: ")
text_choice = text_choice .strip().capitalize()

#Text options
criteria = "We’re Going \nto the Moon!"
provided_drawing = "We're blasting \nto the moon!"

if text_choice == "":
  print("No answer was provided. The program will follow the provided drawing.")
  text = provided_drawing 

elif text_choice in "1A.":
  print("The text will follow the criteria/rubric.")
  text = criteria

elif text_choice in "2B.":
  print("The text will follow the provided drawing.")
  text = provided_drawing

else:
  print("No valid answer was provided. The program will follow the provided drawing.")
  text = provided_drawing

#Black background (Outer space)
background = turtle.Screen()
background.bgcolor("black")

#White circle (Moon)
rocket.goto(-120, 100)
rocket.pencolor("white")
rocket.fillcolor("white")
rocket.begin_fill()
rocket.pendown()
rocket.circle(30)
rocket.end_fill()
rocket.penup()

#Red equilateral triangle (Cone)
rocket.goto(-35, 130)
rocket.fillcolor("red")
rocket.pencolor("red")
rocket.begin_fill()
rocket.pendown()
a = 3
while a > 0:
  rocket.forward(70)
  rocket.left(120)
  a -= 1
rocket.end_fill()
rocket.penup()

#Light grey rectangle (Rocket body)
rocket.goto(-35, -90)
rocket.fillcolor("lightgrey")
rocket.pencolor("lightgrey")
rocket.begin_fill()
rocket.pendown()
b = 2
while b > 0:
  rocket.forward(70)
  rocket.left(90)
  rocket.forward(220)
  rocket.left(90)
  b -= 1
rocket.end_fill()
rocket.penup()

#Dark grey rectangle (Rocket base)
rocket.goto(-35,-90)
rocket.fillcolor("#808080")
rocket.pencolor("#808080")
rocket.begin_fill()
rocket.pendown()
c = 2
while c > 0:
  rocket.forward(70)
  rocket.left(90)
  rocket.forward(10)
  rocket.left(90)
  c -= 1
rocket.end_fill()
rocket.penup()

#Dark grey circle (Rocket window frame)
rocket.goto(0, 40)
rocket.fillcolor("#808080")
rocket.pencolor("#808080")
rocket.begin_fill()
rocket.pendown()
rocket.circle(30)
rocket.end_fill()
rocket.penup()

#Cyan circle (Rocket window)
rocket.goto(0,50.5)
rocket.fillcolor("cyan")
rocket.pencolor("cyan")
rocket.begin_fill()
rocket.pendown()
rocket.circle(19)
rocket.end_fill()
rocket.penup()

#Large red isoceles triangle (Left fin)
rocket.goto(-50, -50)
rocket.fillcolor("red")
rocket.pencolor("red")
rocket.begin_fill()
rocket.pendown()
rocket.forward(30)
rocket.right(110)
rocket.forward(87.71413)
rocket.right(160)
rocket.end_fill()
rocket.penup()

#Small red isoceles triangle (Right fin)
rocket.goto(50, -50)
rocket.begin_fill()
rocket.pendown()
rocket.left(90)
rocket.forward(28)
rocket.left(110)
rocket.forward(81.86652)
rocket.left(70)
rocket.end_fill()
rocket.penup()

#Orange irregular heptagon (Rocket fuel)
flame_length = 58
rocket.goto(-25, -90)
rocket.fillcolor("orange")
rocket.pencolor("orange")
rocket.begin_fill()
rocket.forward(60)
rocket.right(90)
rocket.forward(flame_length)
rocket.right(45)
d = 2
while d > 0:
  rocket.right(90)
  rocket.forward(24)
  rocket.left(90)
  rocket.forward(24)
  d -= 1
rocket.right(135)
rocket.forward(flame_length)
rocket.end_fill()
rocket.penup()

#Text
rocket.goto(100, 50)
rocket.pencolor("white")
rocket.write(text, align="center", font=("sans-serif", 8, "normal"))