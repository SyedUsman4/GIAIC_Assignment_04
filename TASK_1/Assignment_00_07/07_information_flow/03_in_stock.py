def num_in_stock(fruit: str) -> int:
    """
    This function returns the number of fruit Sophia has in stock.
    """
    inventory = {
        "apple": 2,
        "durian": 4,
        "pear": 1000
    }
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

if __name__ == "__main__":
    main()