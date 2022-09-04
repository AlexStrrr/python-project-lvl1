import random


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def round():
    number = random.randint(1, 100)
    question = number
    correct = 'yes' if number % 2 == 0 else 'no'
    return str(question), correct
