from game import BullsAndCowsGame

def main(): 
    game = BullsAndCowsGame(secret="1708")
    game.play()

if __name__ == "__main__":

    choice = "yes"
    
    while choice[0].lower() == "y": # choice loop
        main()
        choice = input("Do you want to play again? (y/n): ")
    
    print("\nHave a nice day! Follow me on insta @_______divyansh")


