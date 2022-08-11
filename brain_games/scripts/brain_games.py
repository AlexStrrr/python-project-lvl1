#!/usr/bin/env python3
from cli import welcome_user
from brain_even import game


def greet():
    print('Welcome to the Brain Games!')


def game_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def main():
    greet()
    welcome_user()
    game_rules()
    game()


if __name__ == '__main__':
    greet()
