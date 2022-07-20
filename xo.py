# Tic-Tac-Toe Program using
# random number in Python

# importing all necessary libraries
import numpy as np
import random
from time import sleep

# Creates an empty board
def create_board(n):
	return(np.array(n*[n*[0]]))
    

# Check for empty places on board
def possibilities(board):
	l = []
	
	for i in range(len(board)):
		for j in range(len(board)):
			
			if board[i][j] == 0:
				l.append((i, j))
	return(l)

# Select a random place for the player
def random_place(board, player):
	selection = possibilities(board)
	current_loc = random.choice(selection)
	board[current_loc] = player
	return([board,current_loc])

# Checks whether the player has three
# of their marks in a horizontal row
def row_win(board, player,current_loc):
    bound=len(board)-1
    if len(board)==3:
        for x in range(len(board)):
            win = True
            
            for y in range(len(board)):
                if board[x, y] != player:
                    win = False
                    continue
                    
            if win == True:
                return(win)
        return(win)
    else:
        x=current_loc[0]
        y=current_loc[1]
        if y+1<=bound:
            if board[x, y+1]==player:
                if y+2<=bound:
                    if board[x,y+2]==player:
                        return True
                if y-1>=0:
                    if board[x,y-1]==player:
                        return True
        if y-1>=0:
            if board[x,y-1]== player:
                if y-2>=0:
                    if board[x,y-2]==player:
                        return True
        return False

# Checks whether the player has three
# of their marks in a vertical row
def col_win(board, player,current_loc):
    if len(board)==3:
        for x in range(len(board)):
            win = True
            
            for y in range(len(board)):
                if board[y][x] != player:
                    win = False
                    continue
                    
            if win == True:
                return(win)
        return(win)
    else:
        bound=len(board)-1
        x=current_loc[0]
        y=current_loc[1]
        if x-1>=0:
            if board[x-1, y]==player:
                if x-2>=0:
                    if board[x-2,y]==player:
                        return True
                if x+1<=bound:
                    if board[x+1,y]==player:
                        return True
        if x+1<=bound:
            if board[x+1,y]== player:
                if x+2<=bound:
                    if board[x+2,y]==player:
                        return True
        return False

# Checks whether the player has three
# of their marks in a diagonal row
def diag_win(board, player,current_loc):
    if len(board)==3:
        win = True
        y = 0
        for x in range(len(board)):
            if board[x, x] != player:
                win = False
        if win:
            return win
        win = True
        if win:
            for x in range(len(board)):
                y = len(board) - 1 - x
                if board[x, y] != player:
                    win = False
        return win
    else:
        bound=len(board)-1
        x=current_loc[0]
        y=current_loc[1]
        if x-1>=0 and y-1>=0:
            if board[x-1, y-1]==player:
                if x-2>=0 and y-2>=0:
                    if board[x-2,y-2]==player:
                        return True
                if x+1<=bound and y+1<=bound:
                    if board[x+1,y+1]==player:
                        return True
        elif x+1<=bound and y+1<=bound:
            if board[x+1,y+1]==player:
                if x+2<=bound and y+2<=bound:
                    if board[x+2][y+2]==player:
                        return True
        if x-1>=0 and y+1<=bound:
            if board[x-1,y+1]== player:
                if x-2>=0 and y+2<=bound:
                    if board[x-2,y+2]==player:
                        return True
                if x+1<=bound and y-1>=0:
                    if board[x+1,y-1]==player:
                        return True
        elif x+1<=bound and y-1>=0:
            if board[x+1,y-1]==player:
                if x+2<=bound and y-2>=0:
                    if [x+2,y-2]==player:
                        return True
        return False

# Evaluates whether there is
# a winner or a tie
def evaluate(board,player,current_loc):
    winner = 0
    if (row_win(board, player,current_loc) or
        col_win(board,player,current_loc) or 
        diag_win(board,player,current_loc)):
             
        winner = player
              
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

# Main function to start the game
def play_game(n,m):
	board, winner, counter = create_board(n), 0, 1
	print(board)
	sleep(2)
	
	while winner == 0:
		for player in list(range(1,m+1)):
			info= random_place(board, player)
			print("Board after " + str(counter) + " move")
			print(info[0])
			sleep(2)
			counter += 1
			winner = evaluate(board,player,info[1])
			if winner != 0:
				break
	return(winner)

# Driver Code
n=int(input("enter size of board: "))
m=int(input("enter number of players: "))
print("Winner is: " + str(play_game(n,m)))
#print(create_board(10))
