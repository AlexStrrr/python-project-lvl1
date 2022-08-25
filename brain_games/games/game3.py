from random import randint
import math
import prompt
from brain_games.cli import name


def game3():
    print('Find the greatest common divisor of given numbers.')
    index = 0
    counter = 3
    while index < counter:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        print(f"Question: {number1} {number2}")
        index += 1
        user_answer = prompt.string('Your answer: ')
        correct = math.gcd(number1, number2)
        correct = str(correct)
        if user_answer == correct:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
                Correct answer was '{correct}'.\nLet's try again, {name}!")
            break

    else:
        print(f"Congratulations, {name}!")