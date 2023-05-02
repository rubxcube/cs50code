# Program that tells meal time

def main():

    # Getting time from user
    time = input("What time is it? ").strip()

    time = convert(time)

    # Meal based on time
    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")


def convert(time):

    # Converting str time into float format
    hour, mins = time.split(":")

    if mins.startswith("0"):
        mins.strip("0")

    hour = float(hour)
    mins = (float(mins) / 60)

    return hour + mins


if __name__ == "__main__":
    main()
