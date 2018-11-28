def plot_func(x0, x1, num_of_segments):
    """
    plot f between x0 and x1 using num_of_segments straight lines.
    use the plot_line function in the graph object.
    f will be plotted to the screen with color c.
    """
    list_of_x = [x for x in range(x0, x1, num_of_segments)]
    list_of_y = [x**2 for x in list_of_x]
    return list_of_x, list_of_y

print(plot_func(0,10,2))