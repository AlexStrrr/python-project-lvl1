#!/usr/bin/env python3
from random import random
from random import randint
from random import choice
from webbrowser import Opera
import prompt


def greet():
    print('Welcome to the Brain Games!')


def game2():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('What is the result of the expression?')
    index = 0
    counter = 3
    while index < counter:
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        operator = ["+","-","*"]
        operator = choice(operator)
        print(f"Question: {number1}{operator}{number2}")
        index += 1
        user_answer = prompt.string('Your answer: ')
        correct = eval(f'{number1}{operator}{number2}')
        correct = str(correct)
        if user_answer == correct:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'.\nLet's try again, {name}!")
            break
        print(f"Congratulations, {name}!")


def main():
    greet()
    game2()


if __name__ == '__main__':
    greet()
