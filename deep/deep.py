# Program answering a question

def main():

    num = input("What is the Asnwer to the Great Question of Life, the Universe and Everything? ").lower().strip()

    # Checking answer
    if (num == "42") or (num == "forty two") or (num == "forty-two"):
        print("Yes")
    else:
        print("No")


main()
