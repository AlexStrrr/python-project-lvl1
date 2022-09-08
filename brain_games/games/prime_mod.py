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
    prime_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                    37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    return True if number in prime_number else False
