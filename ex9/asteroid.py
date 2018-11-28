######################################################################
# FILE : asteroid.py                                                 #
# WRITERS : Snir Sharristh , snirsh , 305500001                      #
#           Aviv Feldman-Gur, avivf , 200687747                      #
# EXERCISE : intro2cs ex9 2015-2016                                  #
# DESCRIPTION: the code below is responsible for our ship in the game#
# Asteroids!                                                         #
######################################################################
######################################################################
#                           Imports:                                 #
######################################################################
from screen import Screen
import random
import math
######################################################################
#                Frequently Used Numbers:                            #
######################################################################
norm_num = 10
size_num = 5
defualt_ast_size = 3
acceleration_const = 2
random_speed_min_val = 1
random_speed_max_val = 3
delta_x = Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X
delta_y = Screen.SCREEN_MAX_Y - Screen.SCREEN_MIN_Y


class Asteroid:
    def __init__(self):
        """

        this is our asteroid initializer
        will initialize asterpod with:
        a size from [1,2,3]
        radius by using _radius function
        and random coordinates using _init_randoms
        """
        self._init_randoms()
        self.size = defualt_ast_size
        self.radius = self._radius()

    def _radius(self):
        """

        this method will calculate the radius of the asteroid using a
        given function:
        the size of the asteroid (1,2,3) *10 - 5
        """
        return self.size * norm_num - size_num

    def _init_randoms(self):
        """

        generating random coordinates for our asteroid
        """
        # generating random range between x axis of the screen
        x_coord = \
            random.randrange(Screen.SCREEN_MIN_X,
                             Screen.SCREEN_MAX_X)
        # generating random range between y axis of the screen
        y_coord = \
            random.randrange(Screen.SCREEN_MIN_Y,
                             Screen.SCREEN_MAX_Y)
        # generating a random speed between 1 to 3
        x_speed = random.randrange(random_speed_min_val, random_speed_max_val)
        y_speed = random.randrange(random_speed_min_val, random_speed_max_val)
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):
        """

        this function is responsible for the movement of the asteroids
        the movement is calculated by given formula
        """
        # using a formula of axis coordinates and speed modulus delta of the
        # screen axis plus the minimal screen size
        self.x_coord = (self.x_speed + self.x_coord -
                        Screen.SCREEN_MIN_X) % delta_x + Screen.SCREEN_MIN_X
        self.y_coord = (self.y_speed + self.y_coord -
                        Screen.SCREEN_MIN_Y) % delta_y + Screen.SCREEN_MIN_Y

    def has_intersection(self, obj):
        """

        this function will calculate if the given object has collided with
        our asteroid by calculating the distance between them (given formula)
        :input:
         obj - the object we want to check if has collided with our asteroid
        :return:
        True - has collided
        or
        False - hasn't
        """
        # using the formula of square root of:
        # (distance of objects(x axis)^2 + distance of objects(y axis)^2
        distance = math.sqrt((obj.x_coord - self.x_coord) ** acceleration_const
                             + (obj.y_coord - self.y_coord) **
                             acceleration_const)
        # checking if its smaller or equal to the size of the objects
        if distance <= self.radius + obj.radius:
            return True
        return False
