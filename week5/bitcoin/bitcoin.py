# Importing packages
import json
import sys
import requests

# Checking command line validity
if len(sys.argv) == 2:
    # Getting number of bitcoins, json file from API and converting to json file
    try:
        num = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = response.json()

    # Exception Handling
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        sys.exit("API server down")

    # Computing and printing total price in proper format
    price = response["bpi"]["USD"]["rate_float"]
    total = price * num
    print("$" + f"{total:,.4f}")

else:
    sys.exit("Missing command-line argument")

