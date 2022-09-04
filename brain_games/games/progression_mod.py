from random import randint, choice


GAME_RULE = 'What number is missing in the progression?'


def round():
    step = randint(1, 8)
    start = randint(0, 50)
    progression = list(range(start, 100, step))
    length = randint(5, 10)
    progression = progression[:length]
    x = choice(progression)
    index_x = progression.index(x)
    progression[index_x] = '..'
    progression = ' '.join(map(str, progression))
    question = progression
    correct = str(x)
    return question, correct
