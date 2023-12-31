# To do list for a Tic Tac Toe game
#	1. Create the board
#	2. Take first player input
#	3. Check for win or tie
#	4. Take computer input
#	5. Check again for win or tie
#	6. Go back to 1.

# Define global variables for the game

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

currentPlayer = 'X'

gameRunning = True

winner = None

# Define a function to draw the board

def printBoard(board):
    print(board[0] + "  |  " + board[1] + "  |  " + board[2])
    print("--------------")
    print(board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("--------------")
    print(board[6] + "  |  " + board[7] + "  |  " + board[8])
    
# Take player input

def playerInput(board):
    try:
        inp = int(input('Enter a number 1 - 9: '))
    except ValueError:
        print("Sorry, that is not a valid entry!")
        return
    if inp >= 1 and inp <= 9 and board[inp-1] == "-": # [inp-1] because the list index starts with 0
        board[inp-1] = currentPlayer # change list item from - to X
    else:
        print('Sorry, that is not a valid entry!')

# check for a winner or a tie

def checkHorizontle(board):
	global winner
	if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[3]
        print('You won')
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
	    winner = board[4]
        print('You won')
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[5]
        print('You won')
        return True
    

# Check the game so far

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkHorizontle(board)