import turtle
import random

t = turtle.Turtle()
turtle.bgcolor("black")
t.color("white")
t.speed(0)
t.penup()
t.goto(-140,140)
# turtle.tracer(0)#ANIMATION DELAY
for i in range(16):
    t.write(i, align="center")
    t.right(90)

    for j in range(10):
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)

    t.penup()
    t.backward(200)
    t.left(90)
    t.forward(20)

t.hideturtle()

player1 = turtle.Turtle()
player1.color("blue")
player1.shape("turtle")

player1.penup()
player1.goto(-160,100)
player1.pendown()

for i in range(72):
    player1.left(5)

player2 = turtle.Turtle()
player2.color("red")
player2.shape("turtle")

player2.penup()
player2.goto(-160,70)
player2.pendown()

for i in range(10):
    player2.right(36)
    
player3 = turtle.Turtle()
player3.color("orange")
player3.shape("turtle")

player3.penup()
player3.goto(-160,40)
player3.pendown()

for i in range(60):
    player3.right(6)
    
player4 = turtle.Turtle()
player4.color("brown")
player4.shape("turtle")

player4.penup()
player4.goto(-160,10)
player4.pendown()

for i in range(30):
    player4.right(12)
    
player5 = turtle.Turtle()
player5.color("green")
player5.shape("turtle")

player5.penup()
player5.goto(-160,-20)
player5.pendown()

for i in range(20):
    player5.right(18)

player1.penup()
player2.penup()
player3.penup()
player4.penup()
player5.penup()

t.color("silver")

for i in range(120):
    player1.forward(random.randint(1,5))
    player2.forward(random.randint(1, 5))
    player3.forward(random.randint(1, 5))
    player4.forward(random.randint(1, 5))
    player5.forward(random.randint(1, 5))

    if player1.xcor() >= 169:
        t.goto(15, 200)
        t.write("Player1 Wins", align="CENTER", font=("ARIAL", 35, "BoLd"))
        break

    elif player2.xcor() >= 169:
        t.goto(15, 200)
        t.write("Player2 Wins", align="CENTER", font=("ARIAL", 35, "bold"))
        break

    elif player3.xcor() >= 169:
        t.goto(15, 200)
        t.write("Player3 Wins", align="CENTER", font=("ARIAL", 35, "bold"))
        break

    elif player4.xcor() >= 169:
        t.goto(15, 200)
        t.write("Player4 Wins", align="CENTER", font=("ARIAL", 35, "bold"))
        break

    elif player5.xcor() >= 169:
        t.goto(15, 200)
        t.write("Player5 Wins", align="CENTER", font=("ARIAL", 35, "bold"))
        break


turtle.mainloop()