import random


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def round():
    number = random.randint(1, 100)
    question = number
    correct = 'yes' if is_even(number) is True else 'no'
    return str(question), correct


def is_even(number):
    return True if number % 2 == 0 else False
