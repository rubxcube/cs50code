# Program validating user response

from validator_collection import validators


def main():
    email = validator(input("What's your email address? "))
    print(email)


def validator(email):
    try:
        validators.email(email)
        return "Valid"
    except:
        return "Invalid"



if __name__ == "__main__":
    main()
