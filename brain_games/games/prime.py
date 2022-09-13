from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


LOWER_BOUND = 1
UPPER_BOUND = 100


def get_round():
    number = randint(LOWER_BOUND, UPPER_BOUND)
    question = number
    correct = 'yes' if is_prime(number) else 'no'
    return question, correct


def is_prime(number):
    divider = 2
    while divider ** 2 <= number and number % divider != 0:
        divider += 1
    return divider ** 2 > number
