from random import randint, choice


RULES = 'What number is missing in the progression?'


MIN_COM_DIFF = 1
MAX_COM_DIFF = 8
MIN_INIT = 0
MAX_INIT = 50
PROGRESSION_LEN = 100
MIN_QUESTION_LEN = 5
MAX_QUESTION_LEN = 10


def get_progression(init, length, diff):
    progression = list(range(init, PROGRESSION_LEN, diff))
    progression = progression[:length]
    return progression


def get_question(progression, x):
    index_x = progression.index(x)
    progression[index_x] = '..'
    progression = ' '.join(map(str, progression))
    return progression


def get_round():
    common_difference = randint(MIN_COM_DIFF, MAX_COM_DIFF)
    initial_term = randint(MIN_INIT, MAX_INIT)
    len_of_question = randint(MIN_QUESTION_LEN, MAX_QUESTION_LEN)
    progression = \
        get_progression(initial_term, len_of_question, common_difference)
    x = choice(progression)
    question = get_question(progression, x)
    correct = str(x)
    return question, correct
