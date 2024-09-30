import numpy as np
import pandas as pd

df = pd.read_csv("data/customers.csv")

class Customer:

    def __init__(self, id, firstName, lastName, company, address, city, state, zip):

        self.id = id
        self.firsName = firstName
        self.lastName = lastName
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def get_name_address(self):
        return self.firsName, self.lastName, self.company, self.address, self.city, self.state, self.zip

customers = []

for row in range(df.shape[0]):
    
    customer = Customer(id = df.iloc[row]["cust_id"], 
                        firstName = df.iloc[row]["first_name"], 
                        lastName = df.iloc[row]["last_name"],
                        company = df.iloc[row]["company_name"],
                        address = df.iloc[row]["address"],
                        city = df.iloc[row]["city"],
                        state = df.iloc[row]["state"],
                        zip = df.iloc[row]["zip"])

    customers.append(customer)

def main():

    id = int(input("\nEnter customer ID: "))

    not_found = 0

    for customer in customers:

        if customer.id == id:
            fname, lname, cname, address, city, state, zip = customer.get_name_address()
            print(f"\n{fname} {lname}")
            print(address)
            print(f"{city}, {state} {zip}")

            if pd.notna(cname): 
                print(cname)
        
        else:
            not_found+=1

    # no customer with the entered id
    if not_found == len(customers):
        print("\nNo customer with that ID.")

if __name__ == "__main__":
    
    print("Customer Viewer")
    choice = "yes"
    
    while choice.lower() == "yes" or choice.lower() ==  "y":
        main()
        choice = input("\nContinue (y/n): ")

    print("\nBye!")

