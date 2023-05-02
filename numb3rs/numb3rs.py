# Program that validates IP addresses

import re


def main():
    # Printing result
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):

    # Matching IP with the specified form
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        nums = ip.split(".")
        for num in nums:
            if int(num) < 0 or int(num) > 255:
                return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    main()
