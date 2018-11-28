######################################################################
# FILE : torpedo.py                                                  #
# WRITERS : Snir Sharristh , snirsh , 305500001                      #
#           Aviv Feldman-Gur, avivf , 200687747                      #
# EXERCISE : intro2cs ex9 2015-2016                                  #
# DESCRIPTION: the code below is responsible for our Torpedo in the  #
# game Asteroids!                                                    #
######################################################################
######################################################################
#                           Imports:                                 #
######################################################################
import math
from screen import Screen
######################################################################
#                Frequently Used Numbers:                            #
######################################################################
default_radius = 4
defualt_lifespan = 200
delta_x = Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X
delta_y = Screen.SCREEN_MAX_Y - Screen.SCREEN_MIN_Y
acceleration_factor = 2


class Torpedo:
    def __init__(self, x_coord, y_coord, degree):
        """

        initializer of torpedo will create
        x_coord y_coord: the starting position on the x axis and y axis
        degree: the heading of the torpedo
        radius: the size of the torpedo
        life_span: the torpedo has a starting life span of 200 which will
        decrease on every run of the game.
        """
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.degree = degree
        self.radius = default_radius
        self.life_span = defualt_lifespan
        # checking if its smaller or equal to the size of the objects

    def _speed(self, ships_x_speed, ships_y_speed):
        """

        this will initiate the speed of the torpedo considering the ships
        speed (the shooting ship of course)
        acceleration_factor is 2
        """
        # the formula is the ships x axis speed + 2*cos(torpedo heading)
        # and the ships y axis speed + 2*sin(torpedo heading)
        self.x_speed = ships_x_speed + acceleration_factor * math.cos(
            math.radians(self.degree))
        self.y_speed = ships_y_speed + acceleration_factor * math.sin(
            math.radians(self.degree))

    def _move(self):
        """

        this function will generate the movement of the torpedo using a
        given formula
        acceleration_factor is 2
        """
        # using a formula of axis coordinates and speed modulus delta of the
        # screen axis plus the minimal screen size
        self.x_coord = (self.x_speed + self.x_coord -
                        Screen.SCREEN_MIN_X) % delta_x + Screen.SCREEN_MIN_X
        self.y_coord = (self.y_speed + self.y_coord -
                        Screen.SCREEN_MIN_Y) % delta_y + Screen.SCREEN_MIN_Y

    def get_intersection(self, obj):
        """

        this function will calculate if the given object has collided with
        the torpedo by calculating the distance between them (given formula)
        :input:
         obj - the object we want to check if has collided with our torpedo
        :return:
        True - has collided
        or
        False - hasn't
        """
        # using the formula of square root of:
        # (distance of objects(x axis)^2 + distance of objects(y axis)^2
        distance = math.sqrt(
            (obj.x_coord - self.x_coord) ** acceleration_factor +
            (obj.y_coord - self.y_coord) ** acceleration_factor)
        # checking if its smaller or equal to the size of the objects
        if distance <= self.radius + obj.radius:
            return True
        return False
