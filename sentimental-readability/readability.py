# Readability program
import cs50


def main():

    # Prompting user for text
    text = cs50.get_string("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Calculating index
    letters_w = (letters / words) * 100
    sentences_w = (sentences / words) * 100

    index = round(0.0588 * letters_w - 0.296 * sentences_w - 15.8)

    # Printing grade based on index
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


# Counting letters
def count_letters(text):

    letters = 0
    for i in range(len(text)):
        if text[i].isalpha():
            letters += 1
    return letters


# Counting words
def count_words(text):

    words = 1
    for i in range(len(text)):
        if text[i].isspace():
            words += 1
    return words


# Counting sentances
def count_sentences(text):

    sentences = 0
    for i in range(len(text)):
        if (text[i] == '.') or (text[i] == '!') or (text[i] == '?'):
            sentences += 1
    return sentences


main()
