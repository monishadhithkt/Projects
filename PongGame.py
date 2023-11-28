import turtle

s = turtle.Screen()
s.title("Pong Game")
s.setup(1050, 650)
s.bgcolor("black")

leftpaddle = turtle.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=7, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-507, 0)

rightpaddle = turtle.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=7, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(500, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("gold")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

Player1 = 0
Player2 = 0

score = turtle.Turtle()
score.speed(0)
score.color("blue")
score.hideturtle()
score.penup()
score.goto(0, 270)
score.write("Player1=0 Player2=0", align="center", font=("Times New Roman", 35, "bold"))

score2 = turtle.Turtle()
score2.speed(0)
score2.color("green")
score2.hideturtle()


def moveLeftPadUp():
    y = leftpaddle.ycor()
    y += 15
    leftpaddle.sety(y)


def moveRightPadUp():
    y = rightpaddle.ycor()
    y += 15
    rightpaddle.sety(y)


def moveLeftPadDown():
    y = leftpaddle.ycor()
    y -= 15
    leftpaddle.sety(y)


def moveRightPadDown():
    y = rightpaddle.ycor()
    y -= 15
    rightpaddle.sety(y)


s.listen()
s.onkeypress(moveLeftPadUp, "a")
s.onkeypress(moveRightPadUp, "b")
s.onkeypress(moveLeftPadDown, "c")
s.onkeypress(moveRightPadDown, "d")

while True:
    s.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if rightpaddle.ycor() > 250:
        rightpaddle.sety(250)

    if rightpaddle.ycor() < -250:
        rightpaddle.sety(-250)

    if leftpaddle.ycor() > 250:
        leftpaddle.sety(250)

    if leftpaddle.ycor() < -250:
        leftpaddle.sety(-250)

    if ball.ycor() > 313:
        ball.sety(313)
        ball.dy *= -1

    if ball.ycor() < -307:
        ball.sety(-307)
        ball.dy *= -1

    if ball.xcor() > 500 or ball.xcor() < -510:
        if ball.xcor() > 500:
            Player1 += 1
        else:
            Player2 += 1

        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= -1
        score.clear()
        score.write("Player1={} Player2={}".format(Player1, Player2), align="center",
                    font=("Times New Roman", 35, "bold"))

    # Default size of square is 20 * 20 units,Calculations as width[in this program] =7,20 * 7 as 140, 140/2 =7 because all turtles takes the center  value as y[Y CENTER VALUE]
    if ball.xcor() > 478 and rightpaddle.ycor() + 70 > ball.ycor() > rightpaddle.ycor() - 70:
        ball.dx *= -1

    if ball.xcor() < -483 and leftpaddle.ycor() + 70 > ball.ycor() > leftpaddle.ycor() - 70:
        ball.dx *= -1

    if Player1 == 5 or Player2 == 5:
        ball.hideturtle()
        score2.penup()
        score2.goto(0, 0)

    if Player1 == 5:
        score2.write("Player1 Wins", align="center", font=("Times New Roman", 35, "bold"))
        break
    elif Player2 == 5:
        score2.write("Player2 Wins", align="center", font=("Times New Roman", 35, "bold"))
        break

    if ball.dy > 0 and ball.dy < 7:
        ball.dy += 1
    elif ball.dy < 0 and ball.dy > -7:
        ball.dy -= 1
    if ball.dx > 0 and ball.dx < 7:
        ball.dx += 1
    elif ball.dx < 0 and ball.dx > -7:
        ball.dx -= 1



turtle.mainloop()
