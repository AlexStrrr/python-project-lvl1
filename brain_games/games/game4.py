from random import randint, choice
import prompt
from brain_games.cli import name


def game4():
    print('What number is missing in the progression?')
    index = 0
    counter = 3
    while index < counter:
        step = randint(1, 8)
        start = randint(0, 50)
        progression = list(range(start, 100, step))
        length = randint(5, 10)
        progression = progression[:length]
        x = choice(progression)
        index_x = progression.index(x)
        progression[index_x] = '..'
        progression = ' '.join(map(str, progression))
        print(f"Question: {progression}")
        index += 1
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(x):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
                Correct answer was '{x}'.\nLet's try again, {name}!")
            break

    else:
        print(f"Congratulations, {name}!")