# Program that outputs correct date format

# List of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():

    # Printing correct date format
    month, day, year = date_formatter()
    print(f"{year}-{month:02}-{day:02}")


def date_formatter():
    while True:

        date = input("Date: ").strip()

        try:
            # Trying to split by " " unless ValueError
            month, day, year = date.split(" ")
        except ValueError:
            try:
                # Trying to split by "/" unless ValueError
                month, day, year = date.split("/")
            except ValueError:
                pass
            else:
                # Checking for (mm/dd/yyyy) form
                if month.isnumeric():
                    if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
                        month, day, year = int(month), int(day), int(year)
                        return month, day, year
        else:
            # Checking for (mm dd, yyyy) form
            day = day.strip(",")
            if (month.isalpha()) and (1 <= int(day) <= 31) and ("," in date):
                month = months.index(month) + 1
                day = int(day)
                year = int(year)
                return month, day, year


main()
