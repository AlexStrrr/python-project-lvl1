from random import randint
import prompt


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def round():
    number = randint(1, 100)
    prime_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                    37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    question = number
    correct = 'yes' if number in prime_number else 'no'
    return question, correct
