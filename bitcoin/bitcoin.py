# Program calculating current Bitcoin price

import requests
import json
import sys


def bitcoin_calculator():

    # If no command-line arguments
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    # Catch errors for 1 command-line argument
    try:
        if len(sys.argv) == 2:
            num = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Query Bitcoin API unless error
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        pass
    else:
        json_response = response.json()

    # Calculate current Bitcoin price
    rate_float = json_response["bpi"]["USD"]["rate_float"]
    current_cost = num * rate_float

    print(f"${current_cost:,.4f}")


bitcoin_calculator()
