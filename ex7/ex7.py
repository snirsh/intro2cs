######################################################################
# FILE : ex7.py                                                      #
# WRITER : Snir Sharristh , snirsh , 305500001                       #
# EXERCISE : intro2cs ex7 2015-2016                                  #
# DESCRIPTION:                                                       #
######################################################################
global zero, one, two
one = 1
zero = 0
two = 2

def print_to_n(n):
    '''
    this function prints every number from 1 to n
    '''
    if n > zero:
        print_to_n(n-one)
        print(n)
    else:
        return


def print_reversed_n(n):
    '''
    this function prints every number from n to 1
    '''
    if n > zero:
        print(n)
        print_reversed_n(n-one)
    else:
        return


def is_prime(n):
    """
    this function checks if a given number is a prime number using has
    divisor smaller than function.

    """
    if n > one:
        return has_divisor_smaller_than(n, n-one)
    else:
        return False


def has_divisor_smaller_than(n, i):
    if i == one or n == one:
        return True
    elif n % i == zero:
        return False
    else:
        return has_divisor_smaller_than(n, i - one)


def is_a_divisor(n, i):
    if n == i:
        return []
    elif n % i == zero:
        return [i] + is_a_divisor(n, i+one)
    else:
        return is_a_divisor(n, i+one)


def divisors(n):
    if abs(n) > one:
        return [one] + is_a_divisor(abs(n), two) + [abs(n)]
    if abs(n) == one:
        return [abs(n)]
    else:
        return []


def factorial_n(n):
    if n == one:
        return one
    return n*factorial_n(n-one)


def exp_n_x(n, x):
    if n == zero:
        return one
    return x**n/factorial_n(n) + exp_n_x(n-one, x)


def play_hanoi(hanoi, n, src, dest, temp):
    if n > zero:
        if n == one:
            hanoi.move(src, dest)
            return
        else:
            play_hanoi(hanoi, n-one, src, temp, dest)
            play_hanoi(hanoi, one, src, dest, temp)
            play_hanoi(hanoi, n-one, temp, dest, src)


def print_binary_sequences(n):
    if n == zero:
        print("")
    print_binary_sequences_with_prefix(str(one), n)
    print_binary_sequences_with_prefix(str(zero), n)


def print_binary_sequences_with_prefix(prefix, n):
    if n == one:
        print(prefix)
    elif n > one:
        print_binary_sequences_with_prefix(prefix + str(zero), n-one)
        print_binary_sequences_with_prefix(prefix + str(one), n-one)


def print_sequences(char_list, n):
    if n > len(char_list):
        return
    for i in range(n):
        print(char_list[i])

def print_sequences_by_index(char_list, n, i):
    




print(print_sequences([0, 2, 3], 2))