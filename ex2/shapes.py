######################################################################
# FILE : shapes.py                                                   #
# WRITER : Snir Sharristh , snirsh , 305500001                       #
# EXERCISE : intro2cs ex2 2015-2016                                  #
# DESCRIPTION: The code below  has four functions that the first one #
# calculates the area of a circle by given radius.                   #
# the second function calculates the area of a rectangle by two given#
# edges.                                                             #
# the third function calculates the area of a trapezoid by two given #
# edges and a given height.                                          #
# the fourth function asks the user what area he chooses to calculate#
# and by the given input calls the right function above              #
######################################################################
# importing math library to use pi later
import math


# the function below will calculate the area of a circle with the user
# inputting the radius value
def circle():
        # r is the radius the user inputs and is converted to float
        inp = input()
        r = float(inp)
        # prints the circle area using pi from math function and r
        # that the user inserted
        return math.pi * r ** 2


# the function below will calculate the area of a rectangle with the
# user inputting the value of the two edges of the rectangle
def rectangle():
        # a is the first edge and b is the second one and are both
        # converted into float
        inp1 = input()
        inp2 = input()
        a = float(inp1)
        b = float(inp2)
        # prints out a times b (the area of the rectangle)
        return a * b


# the function below will calculate the area of a trapezoid with the
# user inputting the value of the two edges and the height of it
def trapezoid():
        # a is the first edge b is the second and h is the height of
        # the trapezoid and are all converted into floats in order
        # to calculate the area
        inp1 = input()
        inp2 = input()
        inp3 = input()
        a = float(inp1)
        b = float(inp2)
        h = float(inp3)
        # prints out the area of the trapezoid which is the sum of the
        # two edges divided by two times the height
        return ((a + b) / 2) * h


# this is the main function that asks the user which shape he wants to
# calculate.
# if the input is 1 it will calculate the circle's area using the circle
# function.
# if the input is 2 it will calculate the rectangle area using the rectangle
# function.
# and if the input is 3 it will calculate the trapezoid area using the
# trapezoid function.
def shape_area():
    # prints out a sentence that describes what the input will do
    # shape will store the input and is converted to an int so it'll be easier
    # to use its value
    shape = input("Choose shape (1=circle, 2=rectangle, 3=trapezoid): ")
    # if the input is 1 it will call the circle function if the input is 2 it
    # will
    # call the rectangle function and if the input is 3 it will call the
    # trapezoid
    # function.
    if shape == "1":
        return circle()
    if shape == "2":
        return rectangle()
    if shape == "3":
        return trapezoid()
    # just in case input is bad it will result in returning none
    return None


