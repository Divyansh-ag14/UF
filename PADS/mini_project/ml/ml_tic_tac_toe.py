# File: SS_Tic_Tac_Toe
# Made by: Soroush Saririan and Divyansh Agarwal
# Start date: 10/24/2024

# Description: 
# A simple tic tac toe game that utilizes user inputs for 
# a user X and user O. It takes two coordinates that have
# to fit under the coordinates specified. The game can be 
# restarted by the user. The game is displayed on a grid
# and the program validates all positions as well as moves
# that generate a win or a draw. The original game has been
# updated to include classes following the skeleton that was
# provided in the project files. Then the part A of the project 
# was updated to include a random position selection. In this
# way the computer can play against itself or against the user.
# The implementation was conducted using the simplest method
# by slightly adjusting the existing code to simplify the task.
# the computer selects the poisiton based on the txt file and 
# the position that will give it an advantage.

# There are some issues with the draw condition, as for some 
# reason the game gives the draw to the person who had the last
# move. So if i end the game in a draw i get the win. 
# Also the computer is not too good at selecting the best potion
# as it often ignore the most obvious position.

import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def filedata(filename): #giving instructions on what to do to the file
    data=pd.read_csv(filename,header=None,delimiter=' ')
    X=data.drop(columns=[9])
    y=data[9]
    return X,y
# path = '/Users/soroush/Downloads/ICP Assignments/Project 2/tictac_final.txt'
X,y=filedata('data/tictac_final.txt') #initalizing the file and opening it
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=2,random_state=55) #paramaters for the model
model=RandomForestClassifier(n_estimators=1000,random_state=55) #wasn't too sure what model to use, but was most comfortable with RF from class experience
model.fit(Xtrain,ytrain)

class Board:
    def __init__(self):
        self.board=[[" " for _ in range(3)] for _ in range(3)]

    def printBoard(self): #printing the board
        print(f"-----------------")
        print(f"|R\\C| 0 | 1 | 2 |")
        print(f"-----------------")
        for i, row in enumerate(self.board):
            print(f"| {i} | " + " | ".join(row) + " | ")
            print("-----------------")

    def resetBoard(self): #reset board
        self.board=[[" " for _ in range(3)] for _ in range(3)]

    def fileadj(self): #setting the fact that -1 is O, 0 is " ", and 1 is X
        return [1 if cell =="X" else -1 if cell=="O" else 0 for row in self.board for cell in row]

    def setBoardState(self,comp):
        self.board=[comp[i*3:(i+1)*3] for i in range(3)]

class Game: #class with all of the game conditions
    def __init__(self,endgameposition):
        self.board=Board()
        self.turn='X'
        self.endgameposition=endgameposition

    def switchPlayer(self): #swithes the player turn, to human or computer
        self.turn='O'if self.turn=='X' else 'X'

    def validateEntry(self,row,col): #ensure that the position is on the board or not taken
        if row not in [0,1,2] or col not in [0,1,2]:
            print(f"Invalid entry: try again")
            print(f"Row & column numbers must be either 0, 1, or 2")
            return False
        elif self.board.board[row][col]!=" ":
            print(f"This cell is already taken.")
            print(f"Please make another selection")
            return False
        return True

    def checkFull(self): #check if the board is full for draw condition
        return all(cell!=" " for row in self.board.board for cell in row)

    def checkWin(self): #check if there is a winner on the current turn
        comppos=self.board.fileadj()
        for position, winner in self.endgameposition:
            if comppos == position:
                print(f"{'X' if winner==1 else 'O'} IS THE WINNER!!!")
                return True
        return False

    def btofeat(self): #turn board into list
        availpos_bto=[]
        for row in self.board.board:
            for cell in row:
                if cell=='X':
                    availpos_bto.append(1)
                elif cell=='O':
                    availpos_bto.append(-1)
                else:
                    availpos_bto.append(0)
        return availpos_bto

    #implementing the computer move selection based on the score
    def computerMove(self):
        dict={0:(0,0),1:(0,1),2:(0,2),3:(1,0),4:(1,1),5:(1,2),6:(2,0),7:(2,1),8:(2,2)}
        features = self.btofeat()
        empty = [i for i in range(9) if features[i] == 0]
    
        bestmove = None
        bestscore = -float('inf')  # lowest score 

        for move in empty:
            row, col = dict[move]
            self.board.board[row][col] = self.turn  # temp move
            adjboard = self.board.fileadj()
            score = model.predict([adjboard])[0]  # predicted score
            self.board.board[row][col] = " "  # undo the move

        if score > bestscore: # update bestmove only for a higher score
            bestscore = score
            bestmove = move

        if bestmove is None:  # If no best move is found
            bestmove = random.choice(empty)
            print(f"Random spot selected")
    
        row, col = dict[bestmove]
        self.board.board[row][col] = self.turn
        print(f"Computer selected {self.turn} at position {row},{col}")

def endgamesfile(filename): #opening the endgame positions from the file
    endgameposition=[]
    with open(filename,'r') as data:
        for line in data:
            *board,winner=map(int,line.split())
            endgameposition.append((board,winner))
    return endgameposition

def main(): #main function that is called to run the game as well as restarting, input positions
    # path = '/Users/soroush/Downloads/ICP Assignments/Project 2/tictac_final.txt'
    endgameposition=endgamesfile('data/tictac_final.txt')
    game=Game(endgameposition)
    endgame=False
    print(f"New Game: {game.turn} goes first.")
    while not endgame:
        game.board.printBoard()
        if game.turn=='X':
            print(f"Where do you want your {game.turn} placed?")
            position=input("Please enter row number and column number separated by a comma.\n")
            row,col=map(int,position.split(","))
            if not game.validateEntry(row,col):
                continue
            game.board.board[row][col] = game.turn
        else:
            game.computerMove()
        if game.checkWin():
            game.board.printBoard()
            endgame=True
        elif game.checkFull():
            game.board.printBoard() 
            print(f"DRAW! NOBODY WINS!") 
            endgame=True
        else:
            game.switchPlayer()
        if endgame:  
            restart=input("Another game? Enter Y or y for yes.\n")
            if restart.lower()=='y': 
                game.board.resetBoard()
                print(f"New Game: {game.turn} goes first")
                print()
                game.turn="X"
                endgame=False
            elif restart.lower()=='n':
                print()
                print(f"Thank you for playing!")

if __name__ == "__main__":
    main()