from utilities import Board, Player

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