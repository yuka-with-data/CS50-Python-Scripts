import sys
import requests

# Check Command Line Argument
def command_line_arg() -> float:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line argument")
    else:
        try:
            n = float(sys.argv[1])
            print(f"Debug Print {n}")
            return n
        except ValueError:
            sys.exit("Command-line argument is not a number")

# Request API
def request_api() -> float:
    try:
    # save JSON API into r
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        # get the JSON content and save it into dict
        bpi_dict = r.json()
        # accessing bpi_dict and retreve rate_float data
        rate = bpi_dict["bpi"]["USD"]["rate_float"]
        return rate
    except requests.RequestException:
        sys.exit()

# generate price
def generate_price(n, rate: float):
    bitcoin_price = n*rate
    return bitcoin_price

def main():
    n = command_line_arg()
    rate = request_api()
    price = generate_price(n, rate)
    print(f"${price:,.4f}")

if __name__ == "__main__":
    main()