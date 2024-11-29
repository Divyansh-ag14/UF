from utilities import EntropyMI, SearchLogic

class BullsAndCowsGame:

    """
    binds the utility classes.

    runs the game loop.
    """

    def __init__(self, secret: str):

        """
        intitializes the secret number

        calculates the total possible 4 digit combinations
        """
        self.__secret = secret
        self.total_secrets = [str(i).zfill(4) for i in range(10000) if len(set(str(i))) == 4]  # All 4-digit unique numbers
    
    def get_secret(self):

        """
        returns the secret number
        """
        
        return self.__secret

    def play(self):
        
        """
        starts the game loop.

        fetches bulls and cows based on user input.

        calculates entropy after each guess
        """
        while True:

            entropy = EntropyMI()
            search_log = SearchLogic(self.get_secret())

            # user input
            guess = input("Enter your guess: ")
            bulls, cows = search_log.check_bac(self.get_secret(), guess)

            print(f"\nBulls: {bulls}, Cows: {cows}")

            # calculate the entropy and mutual information for the remaining possible secrets
            remaining_secrets = [s for s in self.total_secrets if search_log.check_bac(s, guess) == (bulls, cows)]

            entropy_of_remaining_secrets = entropy.get_entropy(remaining_secrets)
            #mutual_information = entropy.get_mi(remaining_secrets, [guess])

            print(f"Entropy of remaining secrets: {entropy_of_remaining_secrets}")
            print("---------------------------")

            # termination: user finds the correct number
            if bulls == 4:
                print("You guessed the correct number!")
                break

            # update possible secrets and repeat
            self.total_secrets= remaining_secrets
