import turtle
import random


def isonscreen(Screen_object, Turtle_object):
    left_bound = -Screen_object.window_width() / 3
    right_bound = Screen_object.window_width() / 3
    top_bound = Screen_object.window_height() / 3
    bottom_bound = -Screen_object.window_height() / 3

    tx = Turtle_object.xcor()
    ty = Turtle_object.ycor()

    if tx > right_bound or tx < left_bound:
        return False
    if ty > top_bound or ty < bottom_bound:
        return False

    return True


def samepos(player1, player2):
    if player1.pos() == player2.pos():
        return False
    else:
        return True


def main():
    s = turtle.Screen()
    s.bgcolor("magenta")

    player1 = turtle.Turtle()
    player2 = turtle.Turtle()

    player1.pencolor("black")
    player1.pensize(5)
    player1.shape("turtle")
    pos = player1.pos()

    player2.pencolor("brown")
    player2.pensize(5)
    player2.shape("turtle")
    player2.hideturtle()
    player2.penup()
    player2.goto(pos[0] + 50, pos[1])
    player2.showturtle()
    player2.pendown()

    move1 = True
    move2 = True

    while move1 and move2 and samepos(player1, player2):
        coinplay1 = random.randrange(0, 2)
        angle = 90

        if coinplay1 == 0:
            player1.left(angle)
        else:
            player1.right(angle)

        coinplay2 = random.randrange(0, 2)

        if coinplay2 == 0:
            player2.left(angle)
        else:
            player2.right(angle)

        player1.forward(50)
        player2.forward(50)

        move1 = isonscreen(s, player1)
        move2 = isonscreen(s, player2)

    player1.pencolor("grey")
    player2.pencolor("grey")

    if move1 == True and move2 == False:
        player1.write("PLAYER1 WINS[BLACK]", True, align="center", font=("Times New Roman", 25, "bold"))

    elif move1 == False and move2 == True:
        player2.write("PLAYER2 WINS[BROWN]", True, align="center", font=("Times New Roman", 25, "bold"))

    else:
        player1.write("GAME DRAW", True, align="center", font=("Times New Roman", 35, "bold"))
        player2.write("GAME DRAW ", True, align="center", font=("Times New Roman", 35, "bold"))
    # When move is True, the turtle will move to a new line after writing the text.
    # When move is False, the turtle will stay at the same position after writing the text.

    s.exitonclick()
#Once the user clicks anywhere inside the window, the program will exit and close the window.

main()
turtle.mainloop()