#!/usr/bin/env python3
from brain_games.scripts.brain_games import greet
from brain_games.games.game5 import game5
from brain_games.cli import welcome_user


def main():
    greet()
    welcome_user()
    game5()


if __name__ == '__main__':
    main()
