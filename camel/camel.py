# Program that turns camelCase into snake_case

def converter():
    name = input("camelCase: ")

    print("snake_case: ", end="")
    # Printing _lowercase instead of uppercase
    for letter in name:
        if letter.isupper():
            print(f"_{letter.lower()}", end="")
            # Skipping over the uppercase letter
            continue
        print(letter, end="")
    print()


converter()
