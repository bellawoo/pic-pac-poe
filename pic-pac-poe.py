from __future__ import print_fuction
from IPython.display import clear_output
import random

board = [' '] * 10

#Shows board
def show_board(board):
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

#Assigns X or O
def player_symbol():
	pass

#Determines who goes first
def first_player():
	pass

#Assign symbol to board
def make_play(board, marker, move):
	pass

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

#Is space available?
def check_board(board, move):
	pass

#Are there spaces left?
def game_over(board):
	pass

#Ask and process play
def take_turn():
	pass