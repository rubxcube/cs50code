# Program interpreting math expressions

def main():

    # Getting expression from user
    expression = input("Expression: ").strip()

    num1, opr, num2 = expression.split(" ")

    num1 = int(num1)
    num2 = int(num2)

    # Printing output based on operation
    if opr == "+":
        print(float(num1 + num2))
    elif opr == "-":
        print(float(num1 - num2))
    elif opr == "*":
        print(float(num1 * num2))
    elif opr == "/":
        print(float(num1 / num2))


main()
