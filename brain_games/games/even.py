import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_BOUND = 1
UPPER_BOUND = 100


def get_round():
    number = random.randint(LOWER_BOUND, UPPER_BOUND)
    question = number
    correct = 'yes' if is_even(number) else 'no'
    return str(question), correct


def is_even(number):
    return number % 2 == 0
