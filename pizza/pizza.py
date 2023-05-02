# Program that formats csv into ASCII art tables

import sys
import csv
from tabulate import tabulate


def main():

    table = formatter()
    print(table)


def formatter():

    # Checking command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif (not sys.argv[1].endswith(".csv")):
        sys.exit("Not a CSV file")

    pizza_types = []

    try:
        # Reading csv file, iterating, returning as dicts
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizza_types.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    # Formatting as grid
    else:
        table = tabulate(pizza_types, headers="keys", tablefmt="grid")
        return table


if __name__ == "__main__":
    main()
