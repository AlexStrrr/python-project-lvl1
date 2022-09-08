from random import randint
import math


RULES = 'Find the greatest common divisor of given numbers.'
LOWER_BOUND = 1
UPPER_BOUND = 100


def get_round():
    number1 = randint(LOWER_BOUND, UPPER_BOUND)
    number2 = randint(LOWER_BOUND, UPPER_BOUND)
    question = (f"{number1} {number2}")
    correct = math.gcd(number1, number2)
    correct = str(correct)
    return question, correct
