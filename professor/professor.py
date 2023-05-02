# Little Professor Game

import random


def main():

    # Getting level, setting count/score to 0
    level = get_level()
    count = 0
    score = 0

    # Looping 10 times for 10 problems
    while count < 10:

        # Generating numbers
        num1, num2 = generate_integer(level)
        correct = num1 + num2

        # Looping 3 times for wrong answer/Error unless correct answer given
        for _ in range(3):
            try:
                ans = int(input(f"{num1} + {num2} = "))
            except ValueError:
                print("EEE")
                pass
            else:
                if ans == correct:
                    score += 1
                    break
                else:
                    print("EEE")

        # Printing correct answer if failed 3 times
        if ans != correct:
            print(f"{num1} + {num2} = {correct}")

        count += 1

    # Printing score
    print(f"Score: {score}")


def get_level():
    # Getting level unless non-numeric or not 1/2/3
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in [1, 2, 3]:
                return level


def generate_integer(level):
    # Generating numbers based on level
    if level == 1:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    elif level == 2:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    elif level == 3:
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)

    return num1, num2


if __name__ == "__main__":
    main()
