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

        self.__name = name

        if flag==0:
            self.__marker = "O"
        else:
            self.__marker = "X"
 
    def get_name(self):

        """Returns the player's name"""
        return self.__name
    
    def get_marker(self):
        
        """Returns the marker for the player"""

        return self.__marker
 
    def get_move(self):

        """
        This function is responsible to get the player's choice of action in real time

        It checks if the values entered are valid and not already filled on the board
        """

        while True: # run an infinite loop till player makes a valid choice

            print(f"Its your turn {self.__name}!")

            user_input = input("Please enter your move: ") # get input (row, col)

            #print(user_input[1])
            move = Move(user_input.upper()) # instantiate move with user input
            print(user_input.upper())
            # check if it is in the valid range
            if move.is_valid():
                move.set_row()
                move.set_column()
                # print(user_input[1])
                # print(move.get_row(),move.get_column())
                break

            else:
                print("\nInvalid Position.")
                print("Please try again!\n")

        return move
    
class Move:

    """
    This class represents the move chosen by the player.

    It checks if the values entered in the string are valid or not.
    """
 
    def __init__(self, value: str):

        """Intializes the move made by the player"""
        self.__inputstring = value
        self.__value = [0,0]
  
    def value(self)-> list:

        """Returns the coordinates"""

        return self.__value
 
    def is_valid(self)-> bool:

        """Checks if the values are in the allowed range"""

        valid_cols = ["A", "B", "C", "D", "E", "F", "G"]
        valid_rows = [1, 2, 3, 4, 5, 6]

        if self.__inputstring[0] not in valid_cols:
            return False
        
        if int(self.__inputstring[1]) not in valid_rows:
            return False

        return True

    def set_row(self):

        """Sets the row value using the second element of input string"""

        self.__value[0] = int(self.__inputstring[1])-1    

    def set_column(self):

        """
        Sets a numeric value of the column from [1-6] using the user input
        """

        if(self.__inputstring[0] == "A"):
            self.__value[1] = 0

        elif(self.__inputstring[0] == "B"):
            self.__value[1] = 1

        elif(self.__inputstring[0] == "C"):
            self.__value[1] = 2

        elif(self.__inputstring[0] == "D"):
            self.__value[1] = 3

        elif(self.__inputstring[0] == "E"):
            self.__value[1] = 4

        elif(self.__inputstring[0] == "F"):
            self.__value[1] = 5

        else:
            self.__value[1] = 6

    def get_row(self)-> int:

        """Fetches the first value of the list"""

        return self.__value[0]
    
    def get_column(self)-> int:

        """Fetches the second value of the list"""

        return self.__value[1]

class Board:
    
    """
    This class intializes a (6x7) borad.

    It can print the allowed positions as well as the current state of the board.

    It also checks if the game is over or not
    """

    EMPTY_CELL = 0 # used to check if board is empty
    ROWS, COLS = 6, 7 # dimensions of the board

    def __init__(self): # board intialization (6*7)
        self.game_board = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0]]


 
    def print_board(self):
        
        """
        Prints the current state of the board.
        """

        print("\nBoard:")

    # Print the column headers
        print("   A   B   C   D   E   F   G")  # Column headers

        for row_index, row in enumerate(self.game_board):

            print(f"{row_index + 1} |", end="")  # Row label
            for cell in row:
                if cell == Board.EMPTY_CELL:  # Print blank space for empty cell
                    print("   |", end="")
                else:  # Print the marker
                    print(f" {cell} |", end="")

            print()  # Newline after each row

        print()
            
    def print_board_with_positions(self):

        """
        Displays the allowed values on the board.

        Each value has a row and column.

        Column is represented by the letter and row by the number
        """
        print("\nPositions:")

        print("| A1 | B1 | C1 | D1 | E1 | F1 | G1 |")
        print("| A2 | B2 | C2 | D2 | E2 | F2 | G2 |")
        print("| A3 | B3 | C3 | D3 | E3 | F3 | G3 |")
        print("| A4 | B4 | C4 | D4 | E4 | F4 | G4 |")
        print("| A5 | B5 | C5 | D5 | E5 | F5 | G5 |")
        print("| A6 | B6 | C6 | D6 | E6 | F6 | G6 |")

    def is_empty(self, row: int, col: int):

        """check if the position is available on the board"""

        if self.game_board[row][col] == Board.EMPTY_CELL:
            return True
        
    def is_lowest(self, row: int , col: int):

        """
        Checks if the move played is the lowest row value available
        """

        # last row
        if row==5:
            return True
        
        # chip below
        if not self.is_empty(row+1, col):
            return True
        
        return False

    def update_board(self, player: Player, move: Move):
            
            """
            Updates the board with player's marker
            """

            while True: # loop runs until player makes a valid choice

                # get the row and col coordinates
                row = move.get_row()
                col = move.get_column()

                # check if the position is available on the board and is valid
                if self.is_empty(row, col) and self.is_lowest(row, col):
                    self.game_board[row][col] = player.get_marker() # fill the position with marker if its empty
                    break # switch control to the other player

                else: 
                    print("\nThis position is not valid!")
                    print("Please enter another one.\n")
                    move = player.get_move() # get player's input again               
                
    def check_terminal_state(self, player, last_move)-> bool:
        
        """
        Checks if the game is over and returns a boolean.

        Searches rows, columns and diagnols to highlight a win

        Checks the number of remaining empty cells to determine a draw
        """
        return (self.check_row(player, last_move) 
                
                or (self.check_column(player, last_move))

                or (self.check_diagonal(player))

                or (self.check_antidiagonal(player)))

    # utility functions for check_terminal_state()

    def check_row(self, player: Player, last_move: Move)-> bool:

        """
        Fetches the row from user's last move

        Checks the row for user marker in the board
        Returns True if the same marker is found at 4 consecutive positions
        """
        row = last_move.get_row()
        for y in range(Board.COLS - 3):
            if (self.game_board[row][y] == player.get_marker() and
                self.game_board[row][y + 1] == player.get_marker() and
                self.game_board[row][y + 2] == player.get_marker() and
                self.game_board[row][y + 3] == player.get_marker()):
                return True
        return False
 
    def check_column(self, player: Player, last_move: Move)-> bool:

        """
        Fetches the column from user's last move.

        Checks the column for user marker in the board

        Returns True if the same marker is found at 4 consecutive positions
        """
        col = last_move.get_column()
        for x in range(Board.ROWS - 3):
            if (self.game_board[x][col] == player.get_marker() and
                self.game_board[x + 1][col] == player.get_marker() and
                self.game_board[x + 2][col] == player.get_marker() and
                self.game_board[x + 3][col] == player.get_marker()):
                return True
        return False
    
    def check_diagonal(self, player: Player)-> bool:

        """
        Checks the diagnol for user marker in the board
        Returns True if the same marker is found at 4 consecutive positions
        """

        for x in range(Board.ROWS - 3):
            for y in range(3, Board.COLS):
                if (self.game_board[x][y] == player.get_marker() and
                    self.game_board[x + 1][y - 1] == player.get_marker() and
                    self.game_board[x + 2][y - 2] == player.get_marker() and
                    self.game_board[x + 3][y - 3] == player.get_marker()):
                    return True
                
        return False
    
 
    def check_antidiagonal(self, player: Player)-> bool:

        """
        Checks the anti diagnol for user marker in the board
        Returns True if the same marker is found at 4 consecutive positions
        """

        for x in range(Board.ROWS - 3):
            for y in range(Board.COLS - 3):
                if (self.game_board[x][y] == player.get_marker() and
                    self.game_board[x + 1][y + 1] == player.get_marker() and
                    self.game_board[x + 2][y + 2] == player.get_marker() and
                    self.game_board[x + 3][y + 3] == player.get_marker()):
                    return True
        return False
    
    def check_draw(self)-> bool:

        """
        Checks if the board has available positions.
        
        Returns true if no positions are left
        """

        empty_counter = 0
        
        for row in self.game_board:
            empty_counter += row.count(Board.EMPTY_CELL)
        
        return empty_counter == 0
 

class ConnectFour:

    """
    Binds the utility classes.

    Runs the game loop and switches control flow between the players
    """
    
    def start(self):

        """
        Initializes (3x3) board with 0s.

        Initializes player 1 and player 2

        Switches control bw the players.

        Checks if the game is over
        """
        
        print("\n**************************")
        print("  Welcome to Connect Four  ")
        print("**************************")

        print("\nEnter the player names!")
        name1 = input("player1: ")
        name2 = input("player2: ")

        # utility instances
        board = Board() 
        player1 = Player(name1) # flag 0: marker = O
        player2 = Player(name2, flag=1) 

        # print all the valid positions
        board.print_board_with_positions()
 
        while True: # infinite loop to switch between the players until the game is over
            
            # game starts with player 1
            player1_move = player1.get_move() # player 1 input

            board.update_board(player1, player1_move) # update the board with their marker 
            board.print_board() #print the updated board

            # check if player 1 has won
            if board.check_terminal_state(player1, player1_move):
                print(f"Awesome. {player1.get_name()} won the game!\n")
                break
            # check for draw
            if board.check_draw():
                print("You both won or none did!")
                break
            
            # player 2's turn
            player2_move = player2.get_move() # player 2 input
            board.update_board(player2, player2_move) # update the board with their marker 
            board.print_board() # print the updated board

            # check if player 2 has won
            if board.check_terminal_state(player2, player2_move):
                print(f"Awesome. {player2.get_name()} won the game!\n")
                break 

            # check for draw
            if board.check_draw():
                print("You both won or none did!\n")
                break

def main(): 
    game = ConnectFour()
    game.start()

if __name__ == "__main__":

    choice = "yes"
    
    while choice[0].lower() == "y":
        main()
        choice = input("Do you want to play again? (y/n): ")
    
    print("\nHave a nice day! Follow me on insta @_______divyansh") # kindly follow :)


