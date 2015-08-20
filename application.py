# Aqui escribe tu codigo

import os
import sys
import random

class my_game(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.board = []

	def menu(self):
		menu_option = {}

	def my_board(self):
		self.board.append(['	'] * 5)
		for raw in self.board:
			for column in self.board:
				print "|".join(column)
			print "----".join(raw)

	def random_column(self):
		return random.randint(0, len(self.board) -1)

	def random_row(self):
		return random.randint(0, len(self.board) -1)

user1 = my_game()
user1.my_board()
user1.my_board()
user1.my_board()
#print user1.random_column()
#print user1.random_row()
