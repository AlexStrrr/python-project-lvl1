#!/usr/bin/env python3
from brain_games.scripts.brain_games import greet
from brain_games.games.game4 import game4
from brain_games.cli import welcome_user


def main():
    greet()
    welcome_user()
    game4()


if __name__ == '__main__':
    main()
