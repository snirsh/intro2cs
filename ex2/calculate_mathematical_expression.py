######################################################################
# FILE : calculate_mathematical_expression.py                        #
# WRITER : Snir Sharristh , snirsh , 305500001                       #
# EXERCISE : intro2cs ex2 2015-2016                                  #
# DESCRIPTION: The code below  has two functions that the first one  #
# calculates a mathematical expression using n1, n2, and a           #
# the second function calculates the same thing using a string input #
######################################################################


# Function will calculate n1 and n2 using a mathematical notation given in a
# (str)
def calculate_mathematical_expression(n1, n2, a):
    # checks the char given in a (if its a mathematical notation)
    n1 = float(n1)
    n2 = float(n2)
    if a == '+':
        return n1 + n2
    if a == "-":
        return n1 - n2
    if a == "*":
        return n1 * n2
    if a == "/" and n2 != 0:
        return n1 / n2

    return None


# Will calculate given string 'n1 char(mathematical notation) n2' using the
# last function
def calculate_from_string(st):
    # Checks if the string has a mathematical notation
    # also converts the string into two floats containing the numbers
    if '+' in st:
        a = "+"
        n1, n2 = st.split('+')
    elif '-' in st:
        a = "-"
        n1, n2 = st.split('-')
    elif '*' in st:
        a = "*"
        n1, n2 = st.split('*')
    elif '/' in st:
        a = "/"
        n1, n2 = st.split('/')
    else:
        return None
    # Turns the two strings that contains the numbers into floats
    n1 = float(n1)
    n2 = float(n2)
    # returns an equation using the last function
    return calculate_mathematical_expression(n1, n2, a)

