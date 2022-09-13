from random import randint


RULES = 'What number is missing in the progression?'


MIN_COM_DIFF = 1
MAX_COM_DIFF = 8
MIN_INIT = 0
MAX_INIT = 50
MIN_QUESTION_LEN = 5
MAX_QUESTION_LEN = 10


def get_progression(init, length, diff):
    progression_len = diff * length + init
    progression = list(range(init, progression_len, diff))
    return progression[:length]


def get_question(progression, index):
    progression[index] = '..'
    return ' '.join(map(str, progression))


def get_round():
    common_difference = randint(MIN_COM_DIFF, MAX_COM_DIFF)
    initial_term = randint(MIN_INIT, MAX_INIT)
    len_of_question = randint(MIN_QUESTION_LEN, MAX_QUESTION_LEN)
    index = randint(0, len_of_question - 1)
    progression = \
        get_progression(initial_term, len_of_question, common_difference)
    x = progression[index]
    question = get_question(progression, index)
    correct = str(x)
    return question, correct
