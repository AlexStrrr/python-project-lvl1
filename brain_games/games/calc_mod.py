from random import randint
from random import choice


QUESTION = 'What is the result of the expression?'


def round():
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    operator = ["+", "-", "*"]
    operator = choice(operator)
    question = (f"{number1} {operator} {number2}")
    correct = eval(f'{number1}{operator}{number2}')
    correct = str(correct)
    return question, correct
