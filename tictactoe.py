# To do list for a Tic Tac Toe game
#	1. Create the board
#	2. Take first player input
#	3. Check for win or tie
#	4. Take second player input
#	5. Check again for win or tie
#	6. Go back to 1.

# Define global variables for the game

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

# Define a function to draw the board

def printBoard(board):
    print(board[0] + "  |  " + board[1] + "  |  " + board[2])
    print("--------------")
    print(board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("--------------")
    print(board[6] + "  |  " + board[7] + "  |  " + board[8])
    
# Take player input

def playerInput(board):
    inp = int(input('Enter a number 1 - 9: "'))
    
