# Program that emojizes text imput

import emoji


def emojizer():

    text = input("Input: ").strip().lower()

    # Emojizing for both :thumbs_up: and :thumbsup: formats
    emojized_txt = emoji.emojize(text, language="alias")

    print(f"Output: {emojized_txt}")


emojizer()
