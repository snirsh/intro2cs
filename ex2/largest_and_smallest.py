######################################################################
# FILE : largest_and_smallest.py                                     #
# WRITER : Snir Sharristh , snirsh , 305500001                       #
# EXERCISE : intro2cs ex2 2015-2016                                  #
# DESCRIPTION: The code below calculates the maximum number and the  #
# minimum number using three numbers given to it                     #
######################################################################


# function receives three numbers and returns the biggest and the smallest one
def largest_and_smallest(n1, n2, n3):
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    # defines which one is the biggest considering that it may be equal to the
    # rest and mx is the biggest number
    if n1 >= n2 and n1 >= n3:
        mx = n1
    elif n2 >= n1 and n2 >= n3:
        mx = n2
    elif n3 >= n1 and n3 >= n2:
        mx = n3
    # defines which one is the smallest considering that it may be equal to the
    #  rest and mn is the smallest number
    if n1 <= n2 and n1 <= n3:
        mn = n1
    elif n2 <= n1 and n2 <= n3:
        mn = n2
    elif n3 <= n1 and n3 <= n2:
        mn = n3
    # returns the biggest number, and the smallest number
    return mx, mn

