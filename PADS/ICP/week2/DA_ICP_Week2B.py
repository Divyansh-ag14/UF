
def lucky_number(n: int ) -> int:

    lucky_num = 0

    while n:
        lucky_num+= int(n%10)
        n = int(n/10)
    
    return lucky_num
    

def main():
    
    first_name = input("\nWhat is your first name? ")
   
    print("What is your date of birth?")
   
    year = int(input("Year: "))
    month = int(input("Month: "))
    date = int(input("Date: "))

    lucky_num = lucky_number(year) + lucky_number(month) + lucky_number(date)
    #lucky_num = lucky_number((year*100+month)*100+date)

    while lucky_num > 9:
        lucky_num = lucky_number(lucky_num)

    print(f"\nHello {first_name}!")
    print(f"Your luck number is {lucky_num}!")


if __name__ == "__main__":

    print("Welcome to the lucky calculator!")
    
    choice = "yes"
    
    while choice != "n":
        main()
        choice = input("\nRepeat the program? (y or n): ")

    print("\nThank you. Bye.")