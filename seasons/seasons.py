# Program that calculates time difference in text

from datetime import date, timedelta
import sys
import inflect

p = inflect.engine()


def main():
    birthday = input("Date of Birth: ")
    print(convert(birthday))


def convert(bdate):
    try:
        year, month, day = bdate.split("-")
        birth = date(int(year), int(month), int(day))
    except:
        sys.exit("Invalid date")

    difference = date.today() - birth
    total = int(difference.total_seconds() / 60)
    letters = p.number_to_words(total, andword="")

    return f"{letters.capitalize()} minutes"


if __name__ == "__main__":
    main()
