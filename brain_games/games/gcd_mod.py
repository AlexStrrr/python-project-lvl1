from random import randint
import math


QUESTION = 'Find the greatest common divisor of given numbers.'


def round():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = (f"{number1} {number2}")
    correct = math.gcd(number1, number2)
    correct = str(correct)
    return question, correct
