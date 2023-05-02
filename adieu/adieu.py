# Program that sings adieu to people

import inflect

p = inflect.engine()


def goodbye():

    # Creating empty list for names
    names = []

    while True:
        try:
            # Appending names to list and joining them
            name = input("Name: ").strip()

            names.append(name)
            name_list = p.join(names)
        # If user inputs control-d, print output and break
        except EOFError:
            print()
            print(f"Adieu, adieu, to {name_list}")
            break


goodbye()
