from unittest import result
import prompt
import random
from cli import name


def game():
    index = 0
    winscore = 3
    number = random.randint(1, 100)
    user_answer = prompt.string()
    while index < winscore:
        print(number)
        index += 1
        if user_answer == 'yes' and number % 2 == 0 or user_answer == 'no' and number % 2 != 0:
            print('Correct!')
    else:
        print("'" + user_answer + '"' + "is wrong answer. Correct answer was 'no'.\nLet's try again," + name + "!")
    