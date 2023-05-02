# Program that validates vanity plates


def main():
    # Print whether plate is valid or not
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Check length
    if not (2 <= len(s) <= 6):
        return False

    # Check if starts with 2 letters
    if s[:2].isalpha() != True:
        return False

    # Check if numbers in correct format
    for i in range(len(s)):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break

    for i in range(len(s)):
        if s[i].isdigit():
            if s[i:].isdigit() == False:
                return False

    # Check for punctuation marks
    if s.isalnum() != True:
        return False

    return True


main()
