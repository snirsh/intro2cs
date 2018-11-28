######################################################################
# FILE : quadratic_equation.py                                       #
# WRITER : Snir Sharristh , snirsh , 305500001                       #
# EXERCISE : intro2cs ex2 2015-2016                                  #
# DESCRIPTION: The code below  has two functions that the first one  #
# calculates the quadratic equation using three numbers give to it   #
# the second function calculates the same thing using the users input#
######################################################################


# importing math.py for the square root function
import math


# function that takes three numbers 1, 2, 3 and creates the quadratic equation
# using them.
def quadratic_equation(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    # sqr is the value that is in the square root.
    sqr = ((b ** 2) - (4 * a * c))
    x1 = None
    x2 = None
    # if the sqr value is less than 0 than it will return None for there is no
    # square root for negative numbers.
    if sqr < 0:
        return None, None
    # if the sqr value is bigger or equal to 0 than it will create two numbers
    # x1 and x2 out of it.
    else:
        if sqr > 0:
            x1 = (-b + (math.sqrt(sqr))) / (2 * a)
            x2 = (-b - (math.sqrt(sqr))) / (2 * a)
            return x1, x2

        if sqr == 0:
            x1 = (-b + (math.sqrt(sqr))) / (2 * a)
            return x1, None

    return x1, x2


# function will use three variables that the user inputs and uses the last
# function to calculate the quadratic
# equation using them.
def quadratic_equation_user_input():
    # prints out a message for the user to understand what he needs to input.
    # print("Insert coefficients a, b, and c:", end=' ')
    # gets 3 inputs from the user and converts them to float after he inserts
    # them.
    st = input('Insert coefficients a, b, and c: ')
    a, b, c = st.split()
    # tupsie will be the tuple object that contains the tuple that the last
    # function created.
    tupsie = quadratic_equation(a, b, c)
    # if tupsie the tuple has no values therefor the function has no solutions
    # and the function will write
    # that the equation has no solutions.
    if tupsie[0] is None:
        print("The equation has no solutions.")
    # else if tupsie the tuple has only 1 value (his 2nd value [1] is None) the
    #  function will write on screen
    # that the equation has only one solution and the solution.
    if tupsie[1] is None and tupsie[0] is not None:
        print("The equation has 1 solution: " + str(tupsie[0]))
    # else if tupsie the tuple has 2 values (meaning tupsie[0] and tupsie[1]
    # are not None) the function will
    # write on screen that the equation has two solutions the first solution
    # the string "and" and then the second
    # solution.
    if tupsie[1] is not None and tupsie[0] is not None:
        print("The equation has 2 solutions: " + str(tupsie[0]) + " and " +
              str(tupsie[1]))

    return
