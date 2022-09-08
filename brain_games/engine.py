import prompt


ROUNDS_COUNT = 3


def run(game):
    print("Welcome to The Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.RULES)
    for _ in range(ROUNDS_COUNT):
        question, correct = game.get_round()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct:
            print('Correct!')
        else:
            print(f"'{correct}' is wrong answer ;(. Correct answer was \
                '{correct}'.\nLet's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
