# a cat and a dog may fight but a cat and a cat may fight more
def build_dictionary(keys: list) -> dict:
    my_dict = {}

    for key in keys:
        if key in my_dict.keys():
            my_dict[key]+=1
        else:
            my_dict[key]=1

    return my_dict
    

def main():
    print("==============================")
    words = input("Enter words seperated by a space: ")

    keys = [word for word in words.split()]
    keys.sort()
    
    my_dict = build_dictionary(keys)
    print("Soretd keys:", list(my_dict.keys()))
    print("\nLet's print the frequency for each word!")
    
    for key, val in my_dict.items():
        print(f"{key}: {val}")

if __name__ =="__main__":
    print("Welcome to the word frequency program!")
    
    
    choice = "yes"
    
    while choice != "n":
        main()
        choice = input("\nRepeat the program? (y or n): ")
    print("==============================")
    print("Thank you! Goodbye!")