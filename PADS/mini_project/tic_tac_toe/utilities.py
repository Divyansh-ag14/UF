class Move:

    """
    This class represents the move chosen by the player.

    It checks if the values entered in the list are valid or not.
    """
 
    def __init__(self, value: list):

        """Intializes the move made by the player"""

        self._value = value
 
    
    def value(self)-> list:

        """Returns the coordinates"""

        return self._value
 
    def is_valid(self)-> bool:

        """Checks if the values are in the allowed range"""

        for i in self._value:
            if i<0 or i>=3: # fixed board size (3,3)
                return False
        
        return True