import cs50


def main():

    # Getting the dollars owed
    cents = get_dollars()

    # Calculate the number of quarters
    quarters = calculate_quarters(cents)
    cents = float(cents - quarters * 25)

    # Calculate the number of dimes
    dimes = calculate_dimes(cents)
    cents = float(cents - dimes * 10)

    # Calculate the number of nickels
    nickels = calculate_nickels(cents)
    cents = float(cents - nickels * 5)

    # Calculate the number of pennies
    pennies = calculate_pennies(cents)
    cents = float(cents - pennies * 1)

    # Adding coins
    coins = quarters + dimes + nickels + pennies

    # Print total number of coins to give the customer
    print(f"{coins}")


# Prompting user for dollars owed
def get_dollars():

    dollars = cs50.get_float("Change owed: ")

    if dollars < 0:
        get_dollars()

    # Turning dollars into cents
    whole_part = int(dollars) * 100
    dec_part = (dollars - int(dollars)) * 100

    cents = whole_part + dec_part

    return cents


# Function for quarters
def calculate_quarters(cents):
    n = cents / 25
    return int(n)


# Function for dimes
def calculate_dimes(cents):
    n = cents / 10
    return int(n)


# Function for nickels
def calculate_nickels(cents):
    n = cents / 5
    return int(n)


# Function for pennies
def calculate_pennies(cents):
    n = cents / 1
    return int(n)


main()
