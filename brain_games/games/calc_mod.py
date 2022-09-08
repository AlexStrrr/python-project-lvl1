from random import randint
from random import choice


RULES = 'What is the result of the expression?'
LOWER_BOUND = 1
UPPER_BOUND = 10


def get_round():
    number1 = randint(LOWER_BOUND, UPPER_BOUND)
    number2 = randint(LOWER_BOUND, UPPER_BOUND)
    operator = ["+", "-", "*"]
    operator = choice(operator)
    question = (f"{number1} {operator} {number2}")
    correct = eval(f'{number1}{operator}{number2}')
    correct = str(correct)
    return question, correct
