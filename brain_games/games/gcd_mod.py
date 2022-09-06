from random import randint
import math


GAME_RULE = 'Find the greatest common divisor of given numbers.'
min_number = 1
max_number = 100


def get_game():
    number1 = randint(min_number, max_number)
    number2 = randint(min_number, max_number)
    question = (f"{number1} {number2}")
    correct = math.gcd(number1, number2)
    correct = str(correct)
    return question, correct
