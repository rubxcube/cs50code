# Program that prints Mario pyramid

# Prompting user for input between 0 and 9
while True:
    try:
        height = int(input("Height: "))
    except ValueError:
        continue
    if 1 <= height <= 8:
        break

# Drawing pyramid
if height == 1:
    print("#")
else:
    # Loop for rows
    for i in range(1, height + 1):
        # Loop for spaces
        for j in range(height - i):
            print(" ", end="")
        # Loop for hashes
        for k in range(i):
            print("#", end="")
        print()
