# Program that prints grocery list items in quantity

def grocery_list():

    groceries = {}

    while True:
        try:
            item = input().lower().strip()

            # Incrementing/setting item count
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1

        # Reprompting until ctrl-d
        except EOFError:
            print()

            # Printing items in alphabetical order
            for key in sorted(groceries.keys()):
                print(f"{groceries[key]} {key.upper()}")
            break
        except KeyError:
            pass


grocery_list()
