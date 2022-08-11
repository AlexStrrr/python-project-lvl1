#!/usr/bin/env python3
import prompt
import random


name = prompt.string('May I have your name? ')


def greeting():
    print('Welcome to the Brain Games!')


def welcome_user():
    print("Hello, " + name + '!')


def game_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


user_answer = prompt.string()

def correct_answer():
    if user_answer == 'yes':
        print('no')
    else:
        print('yes')


def game():
    index = 0
    winscore = 3
    number = random.randint(1, 100)
    while index < winscore:
        print(number)
        index += 1
        if user_answer == 'yes' and number % 2 == 0 or user_answer == 'no' and number % 2 != 0:
            print('Correct!')
    else:
        print("'" + user_answer + '"' + "is wrong answer. Correct answer was" + "'" + correct_answer + "'" + "Let's try again," + name + "!")
    

def main():
    greeting()
    welcome_user()
    game_rules()
    game()


if __name__ == '__main__':
    greeting()
