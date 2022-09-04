#!/usr/bin/env python3
from brain_games.engine import start
from brain_games.games import even_mod


def main():
    start(even_mod)


if __name__ == '__main__':
    main()
