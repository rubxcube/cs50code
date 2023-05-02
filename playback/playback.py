# Program replacing input whitespaces with ...

# Getting the input
text = input()

# Splitting input by spaces
*words ,= text.split()

# Replacing whitespaces
print(*words, sep='...')
