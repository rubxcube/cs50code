# Program that rewards based on greeting

def main():

    greeting = input("Greeting: ").strip().lower()

    # Checking response
    if greeting.startswith("hello"):
        print("$0")
    elif (greeting.startswith("h")) and (greeting != "hello"):
        print("$20")
    else:
        print("$100")


main()
