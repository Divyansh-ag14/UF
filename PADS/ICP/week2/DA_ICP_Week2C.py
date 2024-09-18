
def value_checker(s: str, val: float, val_range: list = None):
    
    if s == "inv":
        while val<=0:
            print("Entry must be greater than 0. Please try again.")
            val = float(input("Enter monthly inverstment: "))
        return val
    
    if s == "ir":
        while not ((val>val_range[0]) and (val<=val_range[1])):
            print(f"Enrty must be greater than {val_range[0]} and less than or equal to {val_range[1]}.")
            val = float(input("Enter yearly interest rate: "))
        return val
    
    if s == "yr":
        while not ((val>val_range[0]) and (val<=val_range[1])):
            print(f"Enrty must be greater than {val_range[0]} and less than or equal to {val_range[1]}.")
            val = int(input("Enter number of years: "))
        return val


def main():
    
    monthly_investment = float(input("Enter monthly inverstment: "))
    monthly_investment = value_checker("inv", monthly_investment)

    yearly_ir = float(input("Enter yearly interest rate: "))
    yearly_ir = value_checker("ir", yearly_ir, [0, 15])

    years = int(input("Enter number of years: "))
    years = value_checker("yr", years, [0, 50])

    prev_inv = 0
    monthly_ir = (yearly_ir/12)/100
    future_value = 0

    print("")
    for i in range(years):
        for j in range(12):
                future_value = (prev_inv+monthly_investment)*(1+monthly_ir)
                prev_inv = future_value
                #print("prev: ", prev_inv)

        print(f"Year = {i+1}", end="    ")            
        print(f"Future Value = {future_value:.2f}")
    


if __name__ == "__main__":

    print("Welcome to the Future Value Calculator\n")
    
    choice = "yes"
    
    while choice.lower() == "yes" or choice.lower() ==  "y":
        main()
        choice = input("\nContinue? (y/n): ")

    print("\nThank you. Bye.")