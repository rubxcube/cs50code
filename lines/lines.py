# Program that reads number of lines of code in file
import sys


def counter():

    # Checking command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif (not sys.argv[1].endswith(".py")):
        sys.exit("Not a Python file")

    line_num = 0

    # Counting lines unless FileNotFoundError
    try:
        with open(sys.argv[1]) as file:
            # Omitting blank lines and comments
            for line in file:
                if line.lstrip().startswith("#"):
                    continue
                elif line.strip() == "":
                    continue
                else:
                    line_num += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        print(line_num)
        sys.exit()


counter()
