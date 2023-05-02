# Program that returns change owed to Coke machine

def coke_machine():

    amount = 50

    # Looping until Coke bought (50 payed)
    while amount > 0:
        print(f"Amount Due: {amount}")
        coin = int(input("Insert Coin: "))
        if (coin == 25) or (coin == 10) or (coin == 5):
            amount = amount - coin

    # Displaying correct change
    left = abs(amount)
    print(f"Change Owed: {left}")


coke_machine()
