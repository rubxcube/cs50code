# Program checking file extensions

def main():

    # Getting input and extension
    file = input("File name: ").strip().lower()
    *name, suffix ,= file.split(".")

    # Printing type based on extension
    if file.endswith(".gif") or file.endswith(".png"):
        print(f"image/{suffix}")
    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        print(f"image/jpeg")
    elif file.endswith(".pdf") or file.endswith(".zip"):
        print(f"application/{suffix}")
    elif file.endswith(".txt"):
        print(f"text/plain")
    else:
        print("application/octet-stream")


main()
