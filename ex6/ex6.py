######################################################################
# FILE : ex6.py                                                      #
# WRITER : Snir Sharristh , snirsh , 305500001                       #
# EXERCISE : intro2cs ex6 2015-2016                                  #
# DESCRIPTION: The code below will eventually create a mosaic image  #
# from a given image using smaller tiles and will show and save it.  #
######################################################################
# importing math for use of fabs function
import math
# importing sys to get sys.argvs (script parameters)
import sys
# using copy library for deepcopy on the make mosaic function
import copy
import mosaic


def compare_pixel(pixel1, pixel2):
    """
    this function gets two pixels which are tuple's of [R,G,B]
    and returns the distance of R + distance of G + Distance of B
    meaning, distance = |r1-r2| + |g1-g2| + |b1-b2|
    """
    # here we save the list length which is r,g,b or 3 and distance will be
    # the integer that we'll calculate the distance into
    rgb = 3
    distance = 0
    # running for each item in the pixel (r,g, and b)
    for i in range(rgb):
        # using math library we use the absolute value to calculate the
        # range between each of the colors of the pixel
        distance += math.fabs(pixel1[i] - pixel2[i])
    return distance


def compare(image1, image2):
    """
    this function will compare the pixels of two given images and will
    return the compared distance between them using the compare pixel function
    """
    # in order to know what rows and columns both images have in common i'm
    # using the minimum feature in which the rows is the minimum range of a
    # list and the minimum colums is the length of a list's row
    rows = min(len(image1), len(image2))
    cols = min(len(image1[0]), len(image2[0]))
    # this float will be used to make the comparison
    compared_distance = 0
    for i in range(rows):
        for j in range(cols):
            # each time we'll add a comparison of image1 and image2 in row i
            #  and column j and add it to our float compared_distance
            compared_distance += compare_pixel(image1[i][j], image2[i][j])
    return compared_distance


def get_piece(image, upper_left, size):
    """
    this function will create a piece from the original image. the piece
    size is given and the corner which we start at from the original image.
    at the end of the function it will return the piece we created from the
    original picture.
    """
    # we create from each tuple two constants so we can use each individually
    row_position, col_position = upper_left
    height, width = size
    # new_piece will be our output list and piece_row will contain each row
    # in it
    new_piece = []
    piece_row = []
    # here i'm creating two constants that will contain the max rows and
    # columns in image so we can see the size isn't bigger then the image
    max_rows = len(image)
    max_cols = len(image[0])
    # here we check that the size from the input isn't too big for the given
    #  image if it is we'll reduce it to the maximum possible size
    # first if checks rows and second checks columns
    if row_position + height > max_rows:
        height = max_rows - row_position
    if col_position + width > max_cols:
        width = max_cols - col_position
    # running for every row and column in the given size
    for rows in range(height):
        for cols in range(width):
            # creating a row from the image row_position + size height and
            # col_position + size width
            piece_row.append(image[rows + row_position][cols + col_position])
        # appending the row into the piece and clearing the row list each
        # time because in the next loop we'll create a new row
        new_piece.append(piece_row)
        piece_row = []
    return new_piece


def set_piece(image, upper_left, piece):
    """
    this function gets an image, upper_left which is the startihg position
    where we set the piece and piece which is the piece we'll set for the image
    and the function will insert thepiece into the image from upperleft
    position.
    this function doesn't return anything! just changes the image from her
    input
    """
    # here we set row and col that will be our upper left positions so we
    # can change them.
    # and we set two counters that will increase as we insert the piece into
    #  the image.
    row, col = upper_left
    counter_row = 0
    counter_col = 0
    # we run two whiles. the first while runs until we are over the image
    # row limits and the second while runs until we are over the image col
    # limits.
    while row + counter_row < len(image) and counter_row < len(piece):
        while col + counter_col < len(image[0]) and counter_col < len(
                piece[0]):
            # setting image from upper_left position to be the same as the
            # piece at it beginning position and we raise the counters to
            # move a pixel at a time
            image[row + counter_row][col + counter_col] = piece[counter_row][
                counter_col]
            counter_col += 1
        counter_row += 1
        counter_col = 0


def average(image):
    """
    this function receives an image which is a list of lists and returns the
    average of the colors of the image

    """
    # creating a sum that will be image rows times image columns (will give
    # us how many pixels we have so we can calculate the average of every
    # color by i.e all the red summation divided by the times of pixels for
    # the average
    sum_of_colors = len(image) * len(image[0])
    # creating the output tuple that will have the value of each color's
    # average
    red, green, blue = (0, 0, 0)
    for rows in image:
        for pixels in rows:
            # here we sum each color by calling the color in each pixel
            # using its index
            red += pixels[0]
            green += pixels[1]
            blue += pixels[2]
    # here we create the average of each color by dividing the sum of each
    # color by the number of pixels
    red /= sum_of_colors
    green /= sum_of_colors
    blue /= sum_of_colors
    return red, green, blue


def preprocess_tiles(tiles):
    """
    this function receives a list of lists each list is an image(tile) and
    it will return a list of the average color of each tile.

    """
    # our output list
    average_tile = []
    # running on every tile and appending to our list its average using
    # average function from above
    for tile in tiles:
        average_tile.append(average(tile))
    return average_tile


def get_best_tiles(objective, tiles, averages, num_candidates):
    """
    this function will return a list of tiles which their color average is
    the closest to the average color of the destination image

    """
    objective_average = average(objective)
    comparisons = []
    best_tiles = []
    minimum = None
    for avg in range(len(averages)):
        comparisons.append([compare_pixel(objective_average, averages[avg]),
                            avg])
    for i in range(num_candidates):
        for comparison in comparisons:
            if minimum is None:
                minimum = comparison
            elif comparison[0] < minimum[0]:
                minimum = comparison
        if tiles[minimum[1]] not in best_tiles:
            best_tiles.append(tiles[minimum[1]])
            comparisons.remove(minimum)
    return best_tiles


print(get_best_tiles([[(20, 40, 60), (25, 47, 69), (10, 20, 30)], [(10, 50, 60), (30, 40, 50), (20, 30, 70)]], [[[(20, 40, 60), (20, 40, 60), (20, 40, 60)], [(20, 40, 60), (20, 40, 60), (20, 40, 60)]], [[(20, 40, 60), (20, 40, 60), (20, 40, 60)], [(60, 41, 20), (60, 41, 20), (60, 41, 20)]], [[(20, 40, 60), (20, 40, 60), (20, 40, 60)], [(20, 40, 60), (20, 40, 60), (20, 40, 60)]], [[(20, 40, 60), (20, 40, 60), (20, 40, 60)], [(60, 41, 20), (60, 41, 20), (60, 41, 20)]]], [(20.0, 40.0, 60.0), (40.0, 40.5, 40.0), (20.0, 40.0, 60.0), (40.0, 40.5, 40.0)], 2))
def choose_tile(piece, tiles):
    """
    this function gets a piece that we want to change and chooses the best
    tile to put there (the tile with the minimal average of colors between
    them)

    """
    averages = []
    # we run for each tile in the tiles list and we'll append the comparison
    #  between this tile and the new piece.
    for tile in tiles:
        averages.append(compare(piece, tile))
    # here we set minimum to be the index of the most minimal average and
    # return the best tile (the one with the minimal average value)
    minimum = averages.index(min(averages))
    return tiles[minimum]


def make_mosaic(image, tiles, num_candidates):
    """
    this function will create a mosaic image from the given image and tiles.
    this function will user num_candidates tiles to create the mosaic

    """
    # first we create a deepcopy of image so we wont change it during the
    # process
    mosaic_img = copy.deepcopy(image)
    # here we preprocess the tiles and save it into averages
    averages = preprocess_tiles(tiles)
    # we create a size that will be the size of each piece (which needs to
    # be the size of each tile)
    size = len(tiles[0]), len(tiles[0][0])
    # we create a beginning position that will be upper_left and we'll
    # divide it into height and width so we can change their values later
    upper_left = (0, 0)
    height, width = upper_left
    # running as long as we don't pass the image height and width
    while height < len(mosaic_img):
        while width < len(mosaic_img[0]):
            # at first we get a piece from our destination image
            piece = get_piece(mosaic_img, upper_left, size)
            # here we get all the number of candidate tiles using
            # get_best_tiles
            candidates = get_best_tiles(piece, tiles, averages, num_candidates)
            # getting the best tile for our current piece using choose tile
            # function
            new_piece = choose_tile(piece, candidates)
            # setting the best tile into the mosaic image using set_piece
            set_piece(mosaic_img, upper_left, new_piece)
            # we increase the width and save our upper_left position so we
            # can move to the next piece
            width += size[1]
            upper_left = height, width
        # here we reached the max width of the image so we start over from
        # the next row so we'll clear width and increase the height we run
        # from next time. we'll again save our upper_left position with the
        # new values
        width = 0
        height += size[0]
        upper_left = height, width
    return mosaic_img


def main():
    """
    main function that will load the image, the tiles and use make mosaic to
    create a mosaic image from out source image. at the end this function
    will show the mosaic image and save it.

    """
    # loading the image named image name
    image = mosaic.load_image(image_name)
    # loading tiles in the image destination folder with the given height
    tiles = mosaic.build_tile_base(image_src, tile_height)
    # creating a mosaic_image using make_mosaic function on image and tiles
    mosaic_image = make_mosaic(image, tiles, num_candidates)
    # showing the new mosaic image and saving it with the given output_name
    mosaic.show(mosaic_image)
    mosaic.save(mosaic_image, output_name)


if __name__ == "__main__":
    # here we set the max arguments to be 6 to check if the user inserted
    # enough arguments
    MAX_ARGUMENTS = 6
    if len(sys.argv) == 6:
        # first argument will be the given image
        image_name = sys.argv[1]
        # second argument will be the destination folder of tiles
        image_src = sys.argv[2]
        # third argument is the output name for the mosaic image
        output_name = sys.argv[3]
        # fourth argument is the height we want for each chosen tile
        tile_height = int(sys.argv[4])
        # fifth argument is the number of tiles the user wants to work with
        num_candidates = int(sys.argv[5])
        main()
    # if the user didn't insert the arguments right it'll print it on the
    # screen
    else:
        print("Wrong number of parameters. the correct usage is:\nex6.py "
              "<image_source><images_dir><output_name><tile_height"
              "><num_candidates> ")
