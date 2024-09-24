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

class Player:

    """
    This class represents the player.

    It is used to assign name, marker and fetch the move played.

    """
    
    def __init__(self, name, flag=0):
        
        """
        Initializes the Player Object.

        Provides a maker and sets the name.
        """

        self.name = name

        if flag==0:
            self._marker = "O"
        else:
            self._marker = "X"
 
    
    def get_marker(self):
        
        """Returns the marker for the player"""

        return self._marker