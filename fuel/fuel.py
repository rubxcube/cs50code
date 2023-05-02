# Program that shows how much fuel is left in the tank
def main():
    percentage = fuel_left()

    # Printing based on percentage
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


def fuel_left():
    while True:
        try:
            # Getting int from input and dividing
            fraction = input("Fraction: ")
            int1, int2 = fraction.split("/")
            int1 = int(int1)
            int2 = int(int2)
            div = round(((int1 / int2) * 100))

        # Checking for exceptions and reprompting
        except (ValueError, ZeroDivisionError):
            pass
        else:
            # Checking for int1 > int2
            if div <= 100:
                break
    return div


if __name__ == "__main__":
    main()
