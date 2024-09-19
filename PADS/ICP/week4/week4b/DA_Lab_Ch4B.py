from sales_tax import  get_tax, get_total_after_tax

def get_items_total():
    
    """
    accepts zero argument and returns total cost of all items
    """

    costs = []
    item_cost = 1

    while item_cost != 0:
        item_cost = float(input("Cost of item: "))
        costs.append(item_cost)
    
    total_cost = sum(costs)
    
    print(f"Total:           {total_cost}")
    print(f"Sales tax:       {get_tax(total_cost)}")
    print(f"Total after tax: {get_total_after_tax(total_cost)}")


def main():
    
    print("\nENTER ITEMS (ENTER 0 TO END)")
    get_items_total()

if __name__ == "__main__":
    
    print("Sales Tax Calculator")
    choice = "yes"
    
    while choice.lower() == "yes" or choice.lower() ==  "y":
        main()
        choice = input("\nAgain? (y/n): ")

    print("\nThanks, bye!")