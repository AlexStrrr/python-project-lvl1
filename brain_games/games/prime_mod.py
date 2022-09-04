from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def round():
    number = randint(1, 100)
    question = number
    correct = 'yes' if is_prime(number) is True else 'no'
    return question, correct


def is_prime(number):
    prime_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                    37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    return True if number in prime_number else False
