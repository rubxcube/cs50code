# Program converting text faces to emojis

# Main function
def main():

    text = input()

    converted = convert(text)

    print(converted)


def convert(text):

    # Replacing old part of string with new one
    replaced = text.replace(":)", "🙂").replace(":(", "🙁")

    return replaced


main()
