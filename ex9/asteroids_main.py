######################################################################
# FILE : asteroids_main.py                                           #
# WRITERS : Snir Sharristh , snirsh , 305500001                      #
#           Aviv Feldman-Gur, avivf , 200687747                      #
# EXERCISE : intro2cs ex9 2015-2016                                  #
# DESCRIPTION: the code below is responsible for our game Asteroids! #
######################################################################
######################################################################
#                           Imports:                                 #
######################################################################
from ship import Ship
from screen import Screen
from asteroid import Asteroid
from torpedo import Torpedo
from copy import deepcopy
import math
import sys
######################################################################
#                Frequently Used Numbers:                            #
######################################################################

CHANGE_DIRECTION = -1
INITIAL_SCORE = 0
NO_LIFE = 0
ARG_VALUE = 1
NO_PARAMETERS = 1
LIFE_DECREASE = 1
SIZE_DECREASE = 1
SMALL_ASTEROID = 1
MID_ASTEROID = 2
POW = 2
BIG_ASTEROID = 3
AST_INIT_SIZE = 3
DEFAULT_ASTEROIDS_NUM = 5
MAX_TORPEDOS = 15
FIRST_HIT_SCORE = 20
SECOND_HIT_SCORE = 50
THIRD_HIT_SCORE = 100
######################################################################
#                       Output Messages:                             #
######################################################################
HIT_TITLE = "you've hit an asteroid..."
HIT_MESSAGE = " booooooooooooo.. "
SHOULD_END_TTL = " quitter alert!!"
SHOULD_END_MSG = "why?!?! why you pressed q?!"
LOSE_TITLE = "you are dead"
LOSE_MSG = "get a life"
WIN_TITLE = "YOU WIN!!"
WIN_MSG = "suddenly I see"


class GameRunner:
    def __init__(self, asteroids_amnt):
        """

        this is our ship initializer
        will initialize a game with:
        screen -   the GUI and helper of our game
        ship -     a Ship object of the fighter ship!
        torpedoes -a list of our merciless torpedoes
        asteroids -a list of all the asteroids currently in space
        score -    user's score based on hits initial score is 0
        """
        self._screen = Screen()
        self.ship = Ship()
        self.torpedos = []
        self.asteroids = []
        self.asteroids_maker(asteroids_amnt)
        self.score = INITIAL_SCORE

    def asteroids_maker(self, asteroids_amnt):
        """

        this function will create the asteroids for us. the function runs in
        range of given amount of asteroids the user wants and creates an
        asteroid that will be in a different random position than the ship's
        random position, a different speed from the ship's speed and a default
        size.
        asteroids_amnt DEFAULT is 5
        AST_INIT_SIZE is 3 (asteroid initializing size)
        """
        for asteroid_num in range(asteroids_amnt):
            new_ast = Asteroid() # creating a new asteroid object
            # this makes sure the position of the asteroid is different than
            #  the ship's position and that their speed is also different
            while (new_ast.x_coord == self.ship.x_coord and
                           new_ast.y_coord == self.ship.y_coord) \
                    or (new_ast.x_speed == self.ship.x_speed and
                                new_ast.y_speed == self.ship.y_speed):
                # initializing a new coordinate for the new asteroid(see
                # Asteroid class)
                new_ast._init_random_coord()
            self.asteroids.append(new_ast) # apeending to our asteroid list
            # registering it to the GUI so it'll be displayed
            self._screen.register_asteroid(new_ast, AST_INIT_SIZE)

    def run(self):
        # not mine
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        # I do wat i want
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """
        My code goes here!

        this is the main method of our game.
        the algorithm of this method is:
         1. checks if the user used any action key (UP LEFT RIGHT SPACE)
         2. moves our Ship. (see Ship class within ship.py)
         3. Displays the ship on the screen using the GUI helper
         4. running a loop on all the torpedoes:
            4.1 drawing the torpedo on the screen
            4.2 decreasing the torpedo lifespan by 1 (LIFE_DECREASE)
            4.3 removing the torpedoes with no life (NO_LIFE = 0)
            4.4 moving all the live torpedoes
         5. updating all the asteroids in our space:
            (checking collisions with the ship or the torpedoes)
         6. checking if the game ended by any of the cases on check_if_end
            method and ending the game if needed
        """

        self.keys_press()  # step 1
        self.ship.move()  # step 2
        self._screen.draw_ship(self.ship.x_coord, self.ship.y_coord,
                               self.ship.degrees) # step 3
        for torpedo in self.torpedos:  # step 4
            self._screen.draw_torpedo(torpedo, torpedo.x_coord,
                                      torpedo.y_coord, torpedo.degree)  # 4.1
            torpedo.life_span -= LIFE_DECREASE  # 4.2
            if torpedo.life_span == NO_LIFE:  # 4.3
                self._screen.unregister_torpedo(torpedo)
                self.torpedos.remove(torpedo)
            torpedo._move()  # 4.4
        self.asteroids_update()  # 5
        if self.check_if_end():  # 6
            self._screen.end_game()
            sys.exit()

    def asteroids_update(self):
        """
        this function will update our asteroids private list of this class.
        this function's algorithm is:
         a. running on all of the asteroids
            1. showing them on the screen using the GUI helper
            2. moving all the asteroids on the screen
            3. checking collisions with asteroids:
                3.1 sending a message if you've been hit by an asteroid
                3.2 removing 1 life from the ship's life (DEFAULT 3)
                3.3 Removing the asteroid from the screen and the private list
            4. checking collisions with torpedoes:
                4.1 giving score based on the size of the hit asteroid
                4.2 showing the score on the screen
                4.3 splitting the hit asteroids or removing them if they
                    were size of 1.

        """
        for asteroid in self.asteroids:  # step a
            # step 1
            self._screen.draw_asteroid(asteroid, asteroid.x_coord,
                                       asteroid.y_coord)
            asteroid.move()  # step 2
            if asteroid.has_intersection(self.ship):  # step 3
                self._screen.show_message(HIT_TITLE, HIT_MESSAGE)  # 3.1
                self._screen.remove_life()  # 3.2
                # step 3.3
                self._screen.unregister_asteroid(asteroid)
                self.asteroids.remove(asteroid)
            # step 4
            for torpedo in self.torpedos:
                if torpedo.get_intersection(asteroid):
                    # step 4.1:
                    # BIG_ASTEROID = 3, MID_ASTEROID = 2 SMALL_ASTEROID = 1
                    # FIRST_HIT_SCORE = 20, SECOND_HIT_SCORE = 50 ,
                    # THIRD_HIT_SCORE = 100
                    if asteroid.size == BIG_ASTEROID:
                        self.score += FIRST_HIT_SCORE
                    elif asteroid.size == MID_ASTEROID:
                        self.score += SECOND_HIT_SCORE
                    elif asteroid.size == SMALL_ASTEROID:
                        self.score += THIRD_HIT_SCORE
                    self._screen.set_score(self.score)  # 4.2
                    self.asteroid_spliter(asteroid, torpedo)  # 4.3

    def keys_press(self):
        """

        this method will check if any action keys we're pressed and will
        assign the right action to it.
        is_left_pressed():moving the ship to the left using it's private method
        is_right_pressed(): - " - right using it's private method
        is_up_pressed(): accelerating the ship
        self._screen.is_space_pressed(): SHOOTING TORPEDOES!
        """
        if self._screen.is_left_pressed():
            self.ship.turn_ship_left()
        elif self._screen.is_right_pressed():
            self.ship.turn_ship_right()
        elif self._screen.is_up_pressed():
            self.ship.acceleration()
        elif self._screen.is_space_pressed():  # here we shoot TORPEDOES
            # checking if the ship is out of torpedoes by using the
            # torpedoes list length (MAX_TORPEDOS = 15)
            if len(self.torpedos) < MAX_TORPEDOS:
                # creating a new torpedo using the ship coordinates and heading
                new_torpedo = Torpedo(self.ship.x_coord, self.ship.y_coord,
                                      self.ship.degrees)
                # generating the torpedoes speed using the ship's speed
                new_torpedo._speed(self.ship.x_speed, self.ship.y_speed)
                # showing the torpedo on screen using the GUI and appending
                # it to our list
                self._screen.register_torpedo(new_torpedo)
                self.torpedos.append(new_torpedo)

    def check_if_end(self):
        """
        this method will check if any of the game is suppose to end
        according to one of the following situations:
        1st is if the user pressed 'q' key
        2nd if the ship is out of lives
        3rd if there are no more asteroids (WIN!)
        :return:
        True - if any of the situations happened
        False - Game continues.
        !MESSAGE AND TITLE VALUES ON TOP OF THE FILE!
        """
        if self._screen.should_end():  # if user pressed 'q'
            self._screen.show_message(SHOULD_END_TTL, SHOULD_END_MSG)
            return True
        elif not self._screen._lives:  # if the ship died
            self._screen.show_message(LOSE_TITLE, LOSE_MSG)
            return True
        elif not self.asteroids:  # if there are no more asteroids to destroy
            self._screen.show_message(WIN_TITLE, WIN_MSG)
            return True
        return False

    def asteroid_spliter(self, asteroid, torpedo):
        """

        this function splits the asteroid after it was hit.
        it will split it into two smaller asteroids with opposite directions.
        but if the hit asteroid was the size of 1 it will remove it from the
        game.
        """
        if asteroid.size > SMALL_ASTEROID:  # SMALL_ASTEROID = 1
            # here we deep copy the original asteroid so we can use it's values
            first_new_ast = deepcopy(asteroid)
            second_new_ast = deepcopy(asteroid)
            # decreasing the original size of each new asteroid by 1
            # (SIZE_DECREASE = 1)
            first_new_ast.size = asteroid.size - SIZE_DECREASE
            second_new_ast.size = asteroid.size - SIZE_DECREASE
            # square root of squared value of the asteroid's x and y speed
            sqrt_pita = \
                math.sqrt(asteroid.x_speed ** POW + asteroid.y_speed ** POW)
            # creating new speeds for the new asteroids:
            first_new_ast.x_speed = \
                (torpedo.x_speed + asteroid.x_speed) / sqrt_pita
            first_new_ast.y_speed = \
                (torpedo.y_speed + asteroid.y_speed) / sqrt_pita
            # CHANGE_DIRECTION = -1 (used to change direction...)
            second_new_ast.x_speed = first_new_ast.x_speed * CHANGE_DIRECTION
            second_new_ast.y_speed = first_new_ast.y_speed * CHANGE_DIRECTION
            # appending the new asteroids to the asteroids list and showing
            # them on the screen using the GUI helper
            self.asteroids.append(first_new_ast)
            self.asteroids.append(second_new_ast)
            self._screen.register_asteroid(first_new_ast, first_new_ast.size)
            self._screen.register_asteroid(second_new_ast, second_new_ast.size)
        # here we remove the hit asteroid and the torpedo that shot him
        self._screen.unregister_asteroid(asteroid)
        self.asteroids.remove(asteroid)
        self.torpedos.remove(torpedo)
        self._screen.unregister_torpedo(torpedo)


def main(amnt):
    runner = GameRunner(amnt)
    runner.run()


if __name__ == "__main__":
    # ARG_VALUE = 1
    # NO_PARAMETERS = 1
    if len(sys.argv) > NO_PARAMETERS:
        main(int(sys.argv[ARG_VALUE]))
    else:
        # DEFAULT_ASTEROIDS_NUM = 5
        main(DEFAULT_ASTEROIDS_NUM)
