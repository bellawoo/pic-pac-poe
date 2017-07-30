from __future__ import print_fuction
from IPython.display import clear_output
import random

board = [' '] * 10
referee = ''
game_state = True

#Shows board
def show_board():
	clear_output()
	print(' | |')
	print(' '+board[7]+' | '+board[8]+' | ' +board[9])
	print(' | |')
	print('---------')
	print(' | |')
	print(' '+board[4]+' | '+board[5]+' | '+board[6])
	print(' | |')
	print('---------')
	print(' '+board[1]+' | '+board[2]+' | '+board[3])
	print(' | |')

#Assign symbol to board
def check_board(board, marker, move):
	global board,referee, referee
	referee = ''
	move = str(move)
	take_turn(move)

	if three_row(board,mark)
		clear_output
		show_board()
		referee = mark +" wins!"
		game_state = False

	clear_output()
	show_board()

	if game_over(board):
		referee = "No more moves. Tie!"
		game_state = False

	return game_state, referee

#Checks against possible wins
def three_row(board, mark):
	if (board[7] == board[8] == board[9] == player) or \
		(board[4] == board[5] == board[6] == player) or \
		(board[1] == board[2] == board[3] == player) or \
		(board[7] == board[4] == board[1] == player) or \
		(board[8] == board[5] == board[2] == player) or \
		(board[9] == board[6] == board[3] == player) or \
		(board[7] == board[5] == board[3] == player) or \
		(board[9] == board[5] == board[1] == player):
		return True
	else:
		return False

#Are there spaces left?
def game_over(board):
	if " " in board[1:]:
		return False
	else:
		return True

def reset_board():
	global board, game_state
	board = [' '] * 10
	game_state = True

#Ask and process move
def take_turn(move):
	global board
	move = 'Make your move: ' + mark
	while True:
		try:
			choice = int(raw_input(move))
		except ValueError:
			print("Oops! Looks like that's not a valid entry. Try again with a number from 1-9.")
			continue

		if choice not in  range(1,10):
			print("Oops! Looks like that's not a valid entry. Try again with a number from 1-9.")
			continue

		if board[choice] == " "
			board[choice] == mark
			break
		else:
			print("Whoa there! Looks like someone's already there. Try choosing another spot.")
			continue

def play_game():
	global referee

	reset_board()

	x = 'X'
	o = 'O'

	while True:
		clear_output()
		show_board()

		game_state, referee = take_turn(x)
		print referee
		if game_state == False:
			break

		game_state, referee = take_turn(o)
		print referee
		if game_state == False;
			break

		new_game = raw_input('Play again? y/n')
		if new_game.lower == 'y':
			play_game()
		else:
			print("Goodbye!")

play_game()