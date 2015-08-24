# Aqui escribe tu codigo

import os
import sys
import random
import pygame

class my_game(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.board = []

	def menu(self):
		os.system('reset')
		menu_option = {1:self.one_player}
		ask_option = int(raw_input("Select the option you want: "))
		one_player = menu_option[ask_option]
		one_player()

	def one_player(self):
		os.system('reset')
		self.my_board()
		column_random = self.random_column()
		row_random = self.random_row()
		print column_random, "column"
		print row_random,"row"
		while True:
			column_guess = self.guess_column()
			row_guess = self.guess_row()
			self.verify_shot(column_random, row_random, column_guess, row_guess)

	def my_board(self):
		self.board.append(['O'] * 10)
		for raw in self.board[0]:
			for column in self.board:
				print " ".join(column)

	def random_column(self):
		return random.randint(1, len(self.board[0]))

	def random_row(self):
		return random.randint(1, len(self.board[0]))

	def guess_column(self):
		column_guess = int(raw_input("Try to guess the column where is hidden a part of a ship: "))
		return column_guess

	def guess_row(self):
		row_guess = int(raw_input("Try to guess the row where is hidden a part of a ship: "))
		return row_guess

	def verify_shot(self, column_random, row_random, column_guess, row_guess):
		if column_guess == column_random and row_guess == row_random:
			print "You guessed a part of the ship"
		else:
			if column_guess <= 0 or column_guess > len(self.board):
				print "This is outside of the board"
			print "You didn't guess any part of a ship"

user1 = my_game()
#user1.one_player()
user1.menu()
#user1.my_board()
