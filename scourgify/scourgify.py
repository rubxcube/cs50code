# Program that formats old csv and writes to new csv

import sys
import csv


def scourgifier():

    # Checking command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    students = []

    try:
        # Loading csv to read
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    else:
        # Writing formatted dicts to new csv
        with open(sys.argv[2], "w") as file:
            for student in students:
                last, first = student["name"].split(",")
                first = first.lstrip()
                student["first"] = first
                student["last"] = last
                del student["name"]

            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(students)


if __name__ == "__main__":
    scourgifier()
