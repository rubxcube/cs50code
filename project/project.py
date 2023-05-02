import random
from collections import Counter
from tabulate import tabulate
import numpy as np
import sys


symbols = [
    {"name": "banana", "value": 1},
    {"name": "grapes", "value": 2},
    {"name": "cherries", "value": 3},
    {"name": "lucky_seven", "value": 7},
    {"name": "lemon", "value": 4},
    {"name": "bell", "value": 5},
    {"name": "orange", "value": 6},
]


MIN_BET = 1
MAX_BET = 100
JACKPOT = 100000


def main():
    print("Hello and welcome to the Slot Machine! 🎰")
    deposit_input = input("How much do you want to deposit? $")
    balance = get_deposit(deposit_input)

    while True:
        try:
            response = input(
                "If you wish to exit, press e\nIf you wish to continue, press c\n"
            ).lower()
        except:
            pass

        if response == "e":
            sys.exit("Thanks for playing. Come back soon!")
        elif response == "c":
            print("Great! Let's go!")
            balance += game(balance)

        if balance == 0:
            print(f"Your current balance is ${balance}.")
            sys.exit("You ran out of money, you cannot play anymore :(")
        print(f"Your current balance is ${balance}")


def game(balance):
    line_input = input("How many lines do you want to bet on? (1-3) ")
    lines = get_line(line_input)

    while True:
        bet_input = input("How much would you like to bet? $")
        bet = get_bet(bet_input)
        if bet > balance:
            print(f"You cannot bet more than your balance (${balance})")
        else:
            break

    reel = generate_slot_reels(lines)
    print(tabulate(reel, tablefmt="grid"))
    winning = combinations(reel, bet)

    if winning == JACKPOT:
        print(f"You won the jackpot - ${winning}!")
        sys.exit("Amazing game! See you soon!")
    elif winning == 0:
        print("You didn't win anything.")
    else:
        print(f"You won ${winning}!")

    return winning - bet


def get_deposit(deposit):
    while True:
        try:
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print("Deposit should be more than $0")
                deposit = input("Enter deposit: $")
        except ValueError:
            sys.exit("Invalid value")

    return deposit


def get_line(line):
    while True:
        try:
            line = int(line)
            if 1 <= line <= 3:
                break
            else:
                print("Number of lines should be between 1 and 3")
                line = input("Enter number of lines (1-3): ")
        except ValueError:
            sys.exit("Invalid value")

    return line


def get_bet(bet):
    while True:
        try:
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet amount should be between ${MIN_BET} and ${MAX_BET}.")
                bet = input("Enter bet amount: $")
        except ValueError:
            sys.exit("Invalid value")

    return bet


def generate_slot_reels(line):

    names = [symbol["name"] for symbol in symbols]

    chosen = random.choices(names, k=(3 * line))
    array = np.array(chosen).reshape(line, 3).tolist()

    return array


def combinations(sequence, bet):

    names = []
    freqs = []

    for arr in sequence:
        counter = Counter(arr)
        freq = counter.most_common(1)[0]
        names.append(freq[0])
        freqs.append(freq[1])

    max_name = max(names)
    max_freq = max(freqs)

    value = 0
    for symbol in symbols:
        if max_name == symbol["name"]:
            value += symbol["value"]

    if max_freq == 1:
        score = 0
    elif max_freq == 3 and max_name == "lucky_seven":
        score = JACKPOT
    else:
        score = value * bet * max_freq

    return score


if __name__ == "__main__":
    main()
