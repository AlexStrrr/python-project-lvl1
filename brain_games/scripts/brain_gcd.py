#!/usr/bin/env python3
from brain_games.scripts.brain_games import greet
from brain_games.games.game3 import game3
from brain_games.cli import welcome_user


def main():
    greet()
    welcome_user()
    game3()


if __name__ == '__main__':
    main()
