#!/usr/bin/env python3
from random import randint, choice
import prompt

def greet():
    print('Welcome to the Brain Games!')


def game5():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('What number is missing in the progression?')
    index = 0
    counter = 3
    while index < counter:
        number = randint(1, 100)
        prime_number = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        print(f"Question: {number}")
        index += 1
        user_answer = prompt.string('Your answer: ')
        correct = 'yes' if number == prime_number else 'no'
        if user_answer == 'yes' and number  == prime_number or user_answer == 'no' and number != prime_number:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'.\nLet's try again, {name}!")
            break

    else:
        print(f"Congratulations, {name}!")
        

def main():
    greet()
    game5()


if __name__ == '__main__':
    main()
