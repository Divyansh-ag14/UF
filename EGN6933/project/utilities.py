import math

class EntropyMI:

    def frequecny_mapper(self, values: list) -> dict:

        """generates frequencies for each item in the list and returns a hashmap"""
        frequencies = {}
        for letter in values:
            if letter in frequencies:
                frequencies[letter] += 1
            else:
                frequencies[letter] = 1
        return frequencies

    
    def get_entropy(self, values: list) -> float:

        """calculates entropy for a list of values"""

        n = len(values)
        if n == 0:
            return 0
        freq = self.frequecny_mapper(values)
        entropy = 0
        for count in freq.values():
            prob = count / n
            entropy -= prob * math.log2(prob)
        return entropy

class SearchLogic:

    """counts the bulls and cows for a given guess and manipulates the number list"""
    def __init__(self, secret: str):
        self.secret = secret

    def check_bac(self, secret, guess):
        
        """creates the secret and guess list 

           identifies the number of bulls and cows
        """
        bulls, cows = 0, 0
        secret_list = list(secret)
        guess_list = list(guess)

        
        for i in range(4): # fixed length number: 4 digits
            if secret_list[i] == guess_list[i]: # bull: right number and right position
                bulls += 1
                secret_list[i] = guess_list[i] = None  # set current bull pos to none

        for i in range(4):
            if guess_list[i] is not None and guess_list[i] in secret_list:
                cows += 1 # cows: numbers that are not none and present in both the lists
                secret_list[secret_list.index(guess_list[i])] = None  # set current cow pos to none
        
        return bulls, cows
