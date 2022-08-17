#!/usr/bin/env python3
from random import randint
import math
import prompt


def greet():
    print('Welcome to the Brain Games!')


def game3():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
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
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'.\nLet's try again, {name}!")
            break

    else:
        print(f"Congratulations, {name}!")
        

def main():
    greet()
    game3()


if __name__ == '__main__':
    main()
