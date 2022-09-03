import prompt


print('Welcome to the Brain Games!')


def start(game):
    print("Welcome to The Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.QUESTION)
    counter = 3
    for _ in range(counter):
        question, correct = game.round()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct:
            print('Correct!')
        else:
            print(f"'{correct}' is wrong answer ;(. Correct answer was '{correct}'.\nLet's try again, {name}!")
            break

    print(f'Congratulations, {name}!')
