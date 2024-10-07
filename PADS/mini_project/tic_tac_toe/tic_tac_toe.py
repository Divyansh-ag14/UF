class Move:

    """
    This class represents the move chosen by the player.

    It checks if the values entered in the list are valid or not.
    """
 
    def __init__(self, value: list):

        """Intializes the move made by the player"""

        self.__value = value
 
    
    def value(self)-> list:

        """Returns the coordinates"""

        return self.__value
 
    def is_valid(self)-> bool:

        """Checks if the values are in the allowed range"""

        for i in self.__value:
            if i<0 or i>=3: # fixed board size (3,3)
                return False
        
        return True
         
 
    def get_row(self)-> int:

        """Fetches the first value of the list"""

        return self.__value[0]
    
    def get_column(self)-> int:

        """Fetches the second value of the list"""

        return self.__value[1]
     
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

            user_input = input("Please enter your move (row, col): ") # get input (row, col)
            user_input = [int(i) for i in user_input.split(",")] # convert to int

            #print(user_input[1])
            move = Move(user_input) # instantiate move with user input

            # check if it is in the valid range
            if move.is_valid():
                break

            else:
                print("\nThe values must be between 0 and 2.")
                print("Please try again!\n")

        return move
    
class Board:
    
    """
    This class intializes a (6x7) borad.

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
|(1, 0) | (1, 1) | (1, 2) |\n\
| (2, 0) | (2, 1) | (2, 2) |\n")
 
    def update_board(self, player: Player, move: Move):
            
            """
            Updates the board with player's marker
            """

            while True: # loop runs until player makes a valid choice

                # get the row and col coordinates
                row = move.get_row()
                col = move.get_column()

                # fetch the current value in the board for (row, col)
                value = self.game_board[row][col] 

                # check if the position is available on the board
                if value == Board.EMPTY_CELL: # fill the position with marker if its empty
                    self.game_board[row][col] = player.get_marker()
                    break # switch control to the other player

                else: 
                    print("\nThis position is already taken!")
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
        Gets the row index of player's move

        Searches the entire row in the board for their marker

        returns true if the count is 3
        """

        row_index = last_move.get_row() # fetch row from Move
        board_row = self.game_board[row_index]
 
        return board_row.count(player.get_marker()) == 3
 
    def check_column(self, player: Player, last_move: Move)-> bool:

        """
        Gets the column index of player's move

        Searches the entire column in the board for their marker

        returns true if the count is 3
        """

        markers_count = 0
        column_index = last_move.get_column() # fetch column from Move
 
        for i in range(3):
            if self.game_board[i][column_index] == player.get_marker():
                markers_count += 1
 
        return markers_count == 3
    
    def check_diagonal(self, player: Player)-> bool:

        """
        Searches the diagnol in the board for player's marker

        returns true if the count is 3
        """

        markers_count = 0
        for i in range(3):
            if self.game_board[i][i] == player.get_marker():
                markers_count += 1
 
        return markers_count == 3
 
    def check_antidiagonal(self, player: Player)-> bool:

        """
        Searches the anti-diagnol in the board for player's marker

        returns true if the count is 3
        """
         
        markers_count = 0
 
        for i in range(3):
            if self.game_board[i][2-i] == player.get_marker():
                markers_count += 1
 
        return markers_count == 3
 
    def check_draw(self)-> bool:

        """
        Checks if the board has available positions.
        
        Returns true if no positions are left
        """
        
        empty_counter = 0
        
        for row in self.game_board:
            empty_counter += row.count(Board.EMPTY_CELL)
        
        return empty_counter == 0
 
class TicTacToeGame:

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
        print("  Welcome to Tic-Tac-Toe  ")
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
    game = TicTacToeGame()
    game.start()

if __name__ == "__main__":

    choice = "yes"
    
    while choice[0].lower() == "y":
        main()
        choice = input("Do you want to play again? (y/n): ")
    
    print("\nHave a nice day! Follow me on insta @_______divyansh")
 