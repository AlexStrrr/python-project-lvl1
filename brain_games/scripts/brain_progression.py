#!/usr/bin/env python3
from random import randint
import prompt
import random


def greet():
    print('Welcome to the Brain Games!')


def game3():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('What number is missing in the progression?')
    index = 0
    counter = 3
    while index < counter:
        step = randint(1, 9)
        prog_len = (5, 10)
        change_number = randint(0, prog_len)
        progression = list(range(0, 100, step))
        ser = progression[:prog_len]
        correct_answer = ser[change_number]
        

        print(f"Question: {progression}")
