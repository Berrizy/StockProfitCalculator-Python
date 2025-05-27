def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Please enter a valid number.")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Please enter a valid whole number.")

def main():
    print("Welcome to the Stock Profit Calculator!\n")
    
    total_cost = 0
    total_value = 0
    num_stocks = get_int("How many different stocks have you bought? ")

    for i in range(num_stocks):
        print(f"\nStock #{i + 1}")
        symbol = input("Enter the stock symbol (e.g., AAPL): ")
        shares = get_int(f"How many shares of {symbol} did you buy? ")
        buy_price = get_float(f"What was the purchase price per share of {symbol}? $")
        current_price = get_float(f"What is the current price per share of {symbol}? $")

        cost = shares * buy_price
        value = shares * current_price
        profit = value - cost

        total_cost += cost
        total_value += value

        print(f"→ You spent ${cost:.2f} on {symbol}")
        print(f"→ Current value: ${value:.2f}")
        print(f"→ Profit/Loss on {symbol}: ${profit:.2f}")

    net_profit = total_value - total_cost
    print("\n--- Portfolio Summary ---")
    print(f"Total Invested: ${total_cost:.2f}")
    print(f"Current Portfolio Value: ${total_value:.2f}")
    print(f"Net Profit/Loss: ${net_profit:.2f}")

    if net_profit > 0:
        print("Great job! You're making a profit.")
    elif net_profit < 0:
        print("You're currently at a loss. Stay informed and be patient!")
    else:
        print("You're breaking even.")

if __name__ == "__main__":
    main()
