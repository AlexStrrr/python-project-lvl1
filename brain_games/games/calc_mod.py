from random import randint
from random import choice


GAME_RULE = 'What is the result of the expression?'
min_number = 1
max_number = 10


def get_game():
    number1 = randint(min_number, max_number)
    number2 = randint(min_number, max_number)
    operator = ["+", "-", "*"]
    operator = choice(operator)
    question = (f"{number1} {operator} {number2}")
    correct = eval(f'{number1}{operator}{number2}')
    correct = str(correct)
    return question, correct
