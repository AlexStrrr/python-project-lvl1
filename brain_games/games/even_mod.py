import random


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
min_number = 1
max_number = 100


def get_game():
    number = random.randint(min_number, max_number)
    question = number
    correct = 'yes' if is_even(number) is True else 'no'
    return str(question), correct


def is_even(number):
    return True if number % 2 == 0 else False
