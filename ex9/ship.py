######################################################################
# FILE : ship.py                                                     #
# WRITERS : Snir Sharristh , snirsh , 305500001                      #
#           Aviv Feldman-Gur, avivf , 200687747                      #
# EXERCISE : intro2cs ex9 2015-2016                                  #
# DESCRIPTION: the code below is responsible for our ship in the game#
# Asteroids!                                                         #
######################################################################
######################################################################
#                           Imports:                                 #
######################################################################
import random
import math
from screen import Screen
######################################################################
#                Frequently Used Numbers:                            #
######################################################################
ship_def_radius = 1
default_init = 0
movement = 7
delta_x = Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X
delta_y = Screen.SCREEN_MAX_Y - Screen.SCREEN_MIN_Y


class Ship:
    def __init__(self):
        """

        this is our ship initializer
        will initialize ship with:
        x axis, y axis coordinates default values are 0 and 0
        x axis, y axis speed default values are 0 and 0
        degrees the heading of our ship default value is 0
        radius - this is the "size" of the ship default value is 1
        """
        self.x_coord = default_init
        self.y_coord = default_init
        self._init_random_coord()  # generating random coordinates
        self.x_speed = default_init
        self.y_speed = default_init
        self.degrees = default_init
        self.radius = ship_def_radius

    def _init_random_coord(self):
        """

        this function will generate the random starting coordinates of the ship
        the function is based on random of the screen size by axis sizes(x,y)
        at the end of the function it will save it to the private values of
        ship.
        """
        x_coord = \
            random.randrange(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
        y_coord = \
            random.randrange(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)
        self.x_coord = x_coord
        self.y_coord = y_coord

    def move(self):
        """

        this function will move our ship by using a given formula.
        the function will change the private values of the coordinates of the
        ship using the formula
        """
        # using a formula of axis coordinates and speed modulus delta of the
        # screen axis plus the minimal screen size
        self.x_coord = \
            (self.x_speed + self.x_coord - Screen.SCREEN_MIN_X) % delta_x + \
            Screen.SCREEN_MIN_X
        self.y_coord = \
            (self.y_speed + self.y_coord - Screen.SCREEN_MIN_Y) % delta_y + \
            Screen.SCREEN_MIN_Y

    def acceleration(self):
        """

        this function will create the speed and acceleration by changing the
        private values of the ship's x axis speed and y axis speed.
        """
        # speed is by formula: x axis speed: by cos of the heading and y
        # axis by sine of the heading
        self.x_speed += math.cos(math.radians(self.degrees))
        self.y_speed += math.sin(math.radians(self.degrees))

    def turn_ship_left(self):
        """

        movement is 7 degrees.
        will turn the ship to the left by increasing it's heading by  7
        degrees.
        """
        self.degrees += movement

    def turn_ship_right(self):
        """

        movement is 7 degrees.
        will turn the ship to the right by decreasing it's heading by  7
        degrees.
        """
        self.degrees -= movement




