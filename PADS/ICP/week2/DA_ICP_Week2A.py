
def get_price():
    price = float(input("What is the cost of items ordered?($) "))
    return price

def main():

    price = get_price()

    while price <= 0:
        print("You must enter a positive number. Please try again.")
        price = get_price()

    shipping_cost = 0

    # if price == 0:
    #     #print(f"Your shipping cost is: ${shipping_cost}")

    if price < 30:
        shipping_cost = 5.95
        #print(f"Your shipping cost is: ${shipping_cost}")

    elif price < 50:
        shipping_cost = 7.95
        #print(f"Your shipping cost is: ${shipping_cost}")

    elif price < 75:
        shipping_cost = 9.95
        #print(f"Your shipping cost is: ${shipping_cost}")   
    
    else:
        shipping_cost=0

    print(f"Your shipping cost is: ${shipping_cost}")
    print(f"Your total cost including shipping is: ${(price+shipping_cost):.2f}")

if __name__ == "__main__":

    print("Let's calculate the total cost of your order!\n")
    
    choice = "yes"
    
    while choice.lower() == "yes" or choice.lower() == "y":
        main()
        choice = input("\nContinue? (y/n): ")
        print("")

    print("Bye!")