#!/usr/bin/env python3
import prompt
import random


def greet():
    print('Welcome to the Brain Games!')


def game():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    counter = 3
    while index < counter:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        index += 1
        user_answer = prompt.string('Your answer: ')
        correct = 'yes' if number % 2 == 0 else 'no'
        if user_answer == 'yes' and number % 2 == 0 or user_answer == 'no' and number % 2 != 0:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'.\nLet's try again, {name}!")
            break
        print(f"Congratulations, {name}!")


def main():
    greet()
    game()


if __name__ == '__main__':
    main()
