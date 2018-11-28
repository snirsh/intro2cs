########################################################################################################################
# FILE : hello_turtle.py
# WRITER : Snir Sharristh, snirsh , 305500001
# EXERCISE : intro2cs ex1 2015-2016
# DESCRIPTION: A program that prints a petal a flower an advanced flower and a garden of three flowers to
# the standard output (screen).
########################################################################################################################
import turtle
#a function that draws a petal
def draw_petal():
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(135)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(135)
#a function that draws a flower
def draw_flower():
    turtle.right(45)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(135)
    turtle.forward(150)
#a function that draws an advanced flower
def draw_flower_advanced():
    draw_flower()
    turtle.left(90)
    turtle.up()
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.down()
#a function that draws a flower bed or garden
def draw_flower_bed():
    turtle.up()
    turtle.left(180)
    turtle.forward(200)
    turtle.right(180)
    turtle.down()
    draw_flower_advanced()
    draw_flower_advanced()
    draw_flower_advanced()

turtle.done



