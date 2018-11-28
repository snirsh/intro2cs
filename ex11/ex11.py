######################################################################
# FILE : ex11.py                                                     #
# WRITER : Snir Sharristh , snirsh , 305500001                       #
# EXERCISE : intro2cs ex11 2015-2016                                 #
# DESCRIPTION: this program creates many functions and draws them on #
# screen                                                             #
######################################################################

######################################################################
#                                  Imports                           #
######################################################################
import math

######################################################################
#                   Frequently Used Numbers                          #
######################################################################
STEP = 1
EPSILON = 1e-5
DELTA = 1e-3
SEGMENTS = 100
TEN_K = 10000
HALF = 1 / 2
ONE_K = 1000
NOTHING = 0  # else matters


def plot_func(graph, f, x0, x1, num_of_segments=SEGMENTS, c='black'):
    """
    plot f between x0 and x1 using num_of_segments straight lines.
    use the plot_line function in the graph object. 
    f will be plotted to the screen with color c.
    """
    len_of_segments = abs(x1 - x0) / num_of_segments
    # creating all the x's in range from x0 to x1 with steps of segments
    dots = [(x0 + x * len_of_segments) for x in range(num_of_segments)]
    # appending the last x1
    dots.append(x1)
    for i in range(len(dots) - STEP):  # STEP = 1 running n-1 steps for graph
        # creating the graph from x1,y1 to x1+1,y1+1
        graph.plot_line((dots[i], f(dots[i])),
                        (dots[i + STEP], f(dots[i + STEP])), c)
    return


def const_function(c):
    """
    return the mathematical constant function f such that f(x) = c
    """
    f = lambda x: c
    return f


def identity():
    """
    return the mathematical function f such that f(x) = x
    """
    f = lambda x: x
    return f


def sin_function():
    """return the mathematical function f such that f(x) = sin(x)
    #>>> sinF()(math.pi/2)
    1.0
    """
    f = lambda x: math.sin(x)
    return f


def sum_functions(g, h):
    """return f s.t. f(x) = g(x)+h(x)"""
    f = lambda x: g(x) + h(x)
    return f


def sub_functions(g, h):
    """return f s.t. f(x) = g(x)-h(x)"""
    f = lambda x: g(x) - h(x)
    return f


def mul_functions(g, h):
    """return f s.t. f(x) = g(x)*h(x)"""
    f = lambda x: g(x) * h(x)
    return f


def div_functions(g, h):
    """return f s.t. f(x) = g(x)/h(x)"""
    f = lambda x: g(x) / h(x)
    return f


# The function solve assumes that f is continuous.
# solve return None in case of no solution
def solve(f, x0=-TEN_K, x1=TEN_K, epsilon=EPSILON):
    """return the solution to f in the range between x0 and x1
    by recursively dividing the function to two sides and going for each
    side that is not None
    if the function returns None then it's not a monotonic function
    thus our rule for None is if f(x0) * f(x1) >= 0"""
    mid = abs(x1 - x0) * HALF  # the middle of the function from x1 to x0
    # we check if the edges of our function smaller than epsilon if so we
    # return them
    if abs(f(x0)) < epsilon:
        return x0
    if abs(f(x1)) < epsilon:
        return x1
    if f(x0) * f(x1) >= NOTHING:  # checking if the function is not mon'
        return None
    # running recursively on each side from x0 to the middle point or from
    # middle point to x1
    return solve(f, x0, x1 - mid, epsilon) or solve(f, x0 + mid, x1, epsilon)


def inverse(g, epsilon=EPSILON):
    """return f s.t. f(g(x)) = x
    to do so we run in range -1000 -> 1000 and we use the last function to
    create the height of the wanted inverse function by subtracting the
    original function by every x in our range and decreasing the size of
    epsilon to create maximum accuracy.
    thus our epsilon here is like a delta = epsilon/2 and what we do is:
    solve(g-x).
    """
    RANGE = ONE_K  # our range = 1000
    f = lambda x: solve(sub_functions(g, const_function(x)), -RANGE, RANGE,
                        epsilon * HALF)
    return f


def compose(g, h):
    """return the f which is the compose of g and h """
    f = lambda x: g(h(x))
    return f


def derivative(g, delta=DELTA):
    """return f s.t. f(x) = g'(x)"""
    f = lambda x: (g(x + delta) - g(x)) / delta
    return f


def definite_integral(f, x0, x1, num_of_segments=SEGMENTS):
    """
    return a float - the definite_integral of f between x0 and x1
    #>>>definite_integral(const_function(3),-2,3)
    15
    """
    # checking first that we don't divide by zero! if so we return
    # num_of_segments to it's default value
    if num_of_segments == NOTHING:  # = 0
        num_of_segments = SEGMENTS  # = 100
    len_of_segment = abs(x1 - x0) / num_of_segments
    # here we create a list of all the x's from x0 to x1 that are in the
    # segment size
    x_dots = [(x0 + x * len_of_segment) for x in range(num_of_segments)]
    x_dots.append(x1)  # appending the last x which is x1
    s = NOTHING  # = 0 our return value, sigma thus we reset it to 0.
    for i in range(STEP, len(x_dots)):
        # so here what we actually do is run from 1 to n and each time do:
        # SIGMA((f(xi-1 + xi)/2) * (xi-xi-1))
        s += f((x_dots[i - STEP] + x_dots[i]) * HALF) * \
             (x_dots[i] - x_dots[i - STEP])
    return s


def integral_function(f, delta=0.01):
    """return F such that F'(x) = f(x)
    returns the integral for f using the definitive integral
    what we do is calculate the difinitive_integral(lets call it DI) of
    every segment when segments are absolute value of (x)/delta (in this
    case 0.01). we do that by creating a function such that:
     if x>0:
        DI(f(x),from 0 to x with the number of segments)
     else when x<=0
        DI(f(x),from x to 0 with the number of segments)
    """
    g = lambda x: definite_integral(f, NOTHING, x, math.ceil(
        abs(x) / delta)) if x > NOTHING else definite_integral(
        mul_functions(f, const_function(-STEP)), x, NOTHING,
        math.ceil(abs(x) / delta))
    return g


def ex11_func_list():
    """return a list of functions as a solution to q.12"""
    function_list = list()
    x = identity()  # defined as x so that we wont use identity() every time
    #  cos = integral(-sin(x))
    cos = integral_function(mul_functions(const_function(-STEP),sin_function()))
    # q.0 f(x) = 4
    function_list.append(const_function(4))
    # q.1 sin(x) + 4
    function_list.append(sum_functions(sin_function(), const_function(4)))
    # q.2 sin(x+4)
    function_list.append(
        compose(sin_function(), sum_functions(x, const_function(4))))
    # q.3 sin(x)*(x^2)/100
    function_list.append(mul_functions(sin_function(),
                                       div_functions(mul_functions(x, x),
                                                     const_function(100))))
    # q.4 sin(x)/(cos(x) + 2)
    function_list.append(
        div_functions(sin_function(), sum_functions(cos, const_function(2))))
    # q.4 integral(x^2+x-3)
    function_list.append(integral_function(
        sub_functions(sum_functions(mul_functions(x, x), x),
                      const_function(3))))
    # q.6 5*(sin(cos(x)) - cos(x))
    function_list.append(mul_functions(const_function(5), sub_functions(
        compose(sin_function(), cos), cos)))
    # q.7 inverse function of x^3
    function_list.append(inverse(mul_functions(mul_functions(x, x), x)))
    return function_list


# function that generate the figure in the ex description
def example_func(x):
    return (x / 5) ** 3


if __name__ == "__main__":
    import tkinter as tk
    from ex11helper import Graph

    master = tk.Tk()
    graph = Graph(master, -10, -10, 10, 10)
    # un-tag the line below after implementation of plot_func
    color_arr = ['black', 'blue', 'red', 'green', 'brown', 'purple',
                 'dodger blue', 'orange']
    # plot_func(graph, example_func, -10, 10, SEGMENTS, 'red')
    # un-tag the lines below after implementation of ex11_func_list
    list_f = ex11_func_list()
    plot_func(graph, list_f[0], -10, 10, SEGMENTS * 2, color_arr[3])
    master.mainloop()
