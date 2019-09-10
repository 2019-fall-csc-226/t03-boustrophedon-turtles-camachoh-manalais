import turtle

def square0(square):
    square.penup()
    square.pensize(5)
    square.setpos(30, 47)
    square.color('yellow')
    square.pendown()
    for side in range(2):
        square.forward(200)
        square.right(90)
        square.forward(200)
        square.right(90)
def fill0 (fill):
    fill.penup()
    fill.pensize(5)
    fill.setpos(35, 42)
    fill.color('blue')
    fill.pendown()
    for i in range(19):
        fill.right(90)
        fill.forward(190)
        fill.left(90)
        fill.forward(5)
        fill.left(90)
        fill.forward(190)
        fill.right(90)
        fill.forward(5)


def main():
    wn = turtle.Screen()
    square = turtle.Turtle()
    fill = turtle.Turtle()
    square0(square)
    fill0(fill)
    fill.right(90)
    fill.forward(190)
    wn.exitonclick()
main()

