from game import ConnectFour

def main(): 
    game = ConnectFour()
    game.start()

if __name__ == "__main__":

    choice = "yes"
    
    while choice[0].lower() == "y":
        main()
        choice = input("Do you want to play again? (y/n): ")
    
    print("\nHave a nice day! Follow me on insta @_______divyansh")


