"""
    meteo_turtle.py
    assignment: lab 4
    language: python3
    author: Morgan Lecrone

    This program will ask for a series of meteo-turtle commands and
    interpret it to draw weather symbols on a map of Simland.
    The meteo-turtle commands are:
    S - Draw a sun
    P - Draw a sun partially covered by a cloud
    C - Draw a cloud
    R - Draw a cloud with rain
    W - Draw a cloud with snow
    T# - Draw a white box with the temperature # on it
    A# - Draw a red alert circle with radius #
    G#,# - Send the turtle to the coordinates (#,#)
"""
import turtle
import meteo

def get_number(string):
    """
    This function extracts a number from the beginning of the string.

    :param string: the string to extract the number from

    :preconditions: string has a positive or negative number at the beginning
    :postconditions:  the string is unchanged and the number has been returned

    :return number: the number that has been extracted from the string
    """
    n = 0
    number = ''
    if string[0] == "-":
        number += "-"
        n += 1
    if not string[n].isdigit():
        return None
    while len(string) > n and string[n].isdigit():
        number += string[n]
        n += 1
    return number

def interpret(string):
    """
    This function will interpret the meteo-turtle commands and will loop until all commands have been interpreted.
    Each command will be removed from the string after being executed.

    :param string: The user inputted string of meteo-turtle commands

    Preconditions:  The user has inputted a meteo-turtle command string
    Postconditions:  The meteo-turtle command string has been executed

    :return: None if there is an error
    """
    while len(string) > 0:
        turtle.up()
        letter = string[0]
        str = string
        if letter == "S":
            process_S()
        elif letter == "P":
            process_P()
        elif letter == "C":
            process_C()
        elif letter == "R":
            process_R()
        elif letter == "W":
            process_W()
        elif letter == "T":
            str = process_T(string)
        elif letter == "A":
            str = process_A(string)
        elif letter == "G":
            str = process_G(string)
        else:
            str = None
        if str == None:
            print("There was an error with " + string)
            return None
        string = str[1:]

def process_S():
    """
    This function calls the function to draw a sun from meteo.py.
    """
    meteo.draw_sun()

def process_P():
    """
    This function calls the function to draw a sun and then the function to draw a cloud from meteo.py.
    """
    meteo.draw_sun()
    meteo.draw_cloud()

def process_C():
    """
    This function calls the function to draw a cloud from meteo.py.
    """
    meteo.draw_cloud()

def process_R():
    """
    This function calls the function to draw rain from meteo.py.
    """
    meteo.draw_rain()

def process_W():
    """
    This function calls the function to draw a snow from meteo.py.
    """
    meteo.draw_snow()

def process_T(string):
    """
    This function will print the user input temperature on a white box.

    :param string: the string of meteo-turtle commands

    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up

    :return string: string without temperature numbers; None if there was an error reading the string
    """
    length = 36
    width = 16
    string = string[1:]
    temperature = get_number(string)
    if temperature == None:
        return None
    turtle.pencolor("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    meteo.draw_rectangle(length, width)
    turtle.end_fill()
    turtle.forward(length/4)
    turtle.pencolor("black")
    turtle.write(temperature + " F", font=("Arial", 9, "bold"))
    if string[0] == '-':
        string = string[1:]
    while len(string) > 0 and string[0].isdigit():
        string = string[1:]
    string = 'T' + string
    return string


def process_A(string):
    """
    This function draws a red alert circle of user input radius.

    :param string: the string of meteo-turtle commands

    :return string: the string without the alert numbers.
    """
    string = string[1:]
    radius = get_number(string)
    if radius == None:
        return None
    radius = int(radius)
    turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.down()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()
    if string[0] == '-':
        string = string[1:]
    while len(string) > 0 and string[0].isdigit():
        string = string[1:]
    string = 'A' + string
    return string

def process_G(string):
    """
    This function creates a goto command from the string that sends the turtle to the coordinates provided by the user.

    :param string: the string of meteo-turtle commands

    :preconditions: The turtle's pen is up
    :postconditions: The turtle's pen is up

    :return string: the string without the goto numbers and comma
    """
    string = string[1:]
    x = get_number(string)
    if x == None:
        return None
    if string[0] == '-':
        string = string[1:]
    while len(string) > 0 and string[0].isdigit():
        string = string[1:]
    if string[0] != ',':
        return None
    string = string[1:]
    y = get_number(string)
    if y == None:
        return None
    turtle.goto(int(x), int(y))
    if string[0] == '-':
        string = string[1:]
    while len(string) > 0 and string[0].isdigit():
        string = string[1:]
    string = 'G' + string
    return string

def main():
    """
    This function displays the background by calling the background function from meteo.py.
    Then, it prompts the user for a string containing MeteoTurtle commands.
    Then, it calls the interpret function to interpret the commands and call the appropriate functions.
    """
    meteo.background()
    string = input("Input a string containing MeteoTurtle commands:")
    interpret(string)
    turtle.done()


if __name__ == "__main__":
    main()