######################################################################
# FILE : is_normal_bmi.py                                            #
# WRITER : Snir Sharristh , snirsh , 305500001                       #
# EXERCISE : intro2cs ex2 2015-2016                                  #
# DESCRIPTION: The code below  will calculate the bmi and returns a  #
# boolean value true or false                                        #
######################################################################


# the main function, gets two values sph will be spells per hour and
# wand will be the wands length
def is_normal_bmi(sph, wand):
    # bmi will store the bmi value and is calculated by sph divided
    # by wand times two
    sph = float(sph)
    wand = float(wand)
    bmi = sph/(wand**2)
    # here the function will take the bmi value it calculated and
    # if the value is between 18.5 and 24.9 it will return true
    # else it will return false
    if 18.5 <= bmi <= 24.9:
        return True
    else:
        return False

