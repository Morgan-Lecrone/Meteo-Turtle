"""
    meteo.py
    assignment: lab 4
    language: python3
    author: Morgan Lecrone
"""
import turtle as t


def background():
    """
    load the background for the meteo weather map and
    set up the turtle window size and position in the screen's upper left.
    """
    screen = t.Screen()
    screen.bgpic("simland.png")
    t.setup(1100, 650, 0, 0)


def draw_rectangle(length, width):
    """
    draws a rectangle with the given length and width

    :param length: the length of the rectangle
    :param width: the width of the rectangle

    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    t.down()
    for value in range(2):
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)
    t.up()


def snowflake(length=8):
    """
    draws a 6-arms snowflake

    :param length: the length of the arm of the snowflake

    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    t.down()
    t.pencolor("blue")
    for value in range(3):
        t.forward(length)
        t.back(length * 2)
        t.forward(length)
        t.left(60)
    t.left(180)
    t.up()


def draw_sun(r=16):
    """
    This function draws a yellow circle to represent a sun.

    :param r: The radius of the sun; defaults to 16
    """
    t.down()
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.up()

def draw_rain(size=16):
    """
    This function draws a cloud and slanted lines to represent rain.

    :param size: The size of the rain; defaults to 16
    """
    draw_cloud()
    t.pencolor("blue")
    for value in range(3):
        t.right(90)
        t.forward(size / 3)
        t.right(20)
        t.down()
        t.forward(size * 1.5)
        t.up()
        t.right(70)
        t.forward(size / 2)
        t.right(110)
        t.forward(size / 2)
        t.down()
        t.forward(size)
        t.up()
        t.left(20)
        t.forward(size / 3)
        t.right(90)
        t.back(size / 2)
    t.pencolor("black")



def draw_cloud(r=16):
    """
    draws a pretty cloud as a combination of: 1 circle of radius r,
    2 circles of radius r/2 and a rectangle 2r x r

    :param r: the relative radius of the circles in the cloud; defaults to 16

    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up, pencolor black
    """
    t.down()
    t.pencolor("blue")
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(r / 2)
    t.end_fill()
    t.begin_fill()
    draw_rectangle(2.2 * r, r)
    t.end_fill()
    t.begin_fill()
    t.forward(1.2 * r)
    t.circle(r)
    t.forward(1.2 * r)
    t.circle(r / 2)
    t.end_fill()
    t.pencolor("black")
    t.up()


def draw_snow(size=8):
    """
    draws 3 snowflakes and a cloud

    :param size: The size of the snowflakes; defaults to 8

    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    draw_cloud(2 * size)
    t.up()
    t.backward(4 * size)
    t.right(90)
    t.forward(size)
    t.left(90)
    snowflake(size)
    t.right(45)
    t.forward(2 * size)
    t.left(45)
    snowflake(size)
    t.left(45)
    t.forward(2 * size)
    t.right(45)
    snowflake(size)


if __name__ == "__main__":
    background()
