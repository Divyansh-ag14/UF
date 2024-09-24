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
    
class Board:
    
    """
    This class intializes a (3x3) borad.

    It can print the allowed positions as well as the current state of the board.

    It also checks if the game is over or not
    """

    EMPTY_CELL = 0 # used to check if board is empty
 
    def __init__(self): # board intialization
        self.game_board = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]
        
    def print_board(self):
        
        """
        Prints the current state of the board.
        """

        print("\nBoard:")

        # Print the board row by row
        for row in self.game_board:
            print("|", end="")

            for column in row:
                if column == Board.EMPTY_CELL: # print blank space for empty column
                    print("   |", end="")
                
                else: #print value (marker)
                    print(f" {column} |", end="")

             # break line       
            print()

        print()
            
    def print_board_with_positions(self):

        """
        Displays the allowed values on the board.
        Each value has a row and column coordinate from (0 to 2)
        """
        print("\nPositions:")

        print("| (0, 0) | (0, 1) | (0, 2) |\n\
| (1, 0) | (1, 1) | (1, 2) |\n\
| (2, 0) | (2, 1) | (2, 2) |\n")