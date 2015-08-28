# Aqui escribe tu codigo

import os
import sys
import random
import pygame

class my_game(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.board = []
		self.my_ships = []
		self.menu_option = {1:self.one_player, 3:self.exit_program}
		for x in xrange(1,11):
			self.board.append(["0"] * 10)

	def menu(self):
		while True:
			os.system('reset')
			self.menu_print()
			menu_ask_option = self.menu_ask_option()
			menu_perform_action = self.menu_perform_action(menu_ask_option)

	def menu_ask_option(self):
		ask_option = int(raw_input("Select the option you want: "))
		return ask_option

	def menu_perform_action(self, menu_ask_option):
		if menu_ask_option in self.menu_option.keys():
		#if menu_ask_option in self.menu_option():
			option_menu = self.menu_option[menu_ask_option]
			option_menu()
		else:
			message = raw_input("Invalid option")

	def menu_print(self):
		print "1.ONE PLAYER"
		print "2.TWO PLAYERS"
		print "3.EXIT"

	def one_player(self):
		os.system('reset')
		self.my_board()
		#random_column = self.random_column()
		#random_row = self.random_row()
		#print random_column, "column"
		#print random_row,"row"
		random_vertical_or_horizontal = self.random_vertical_or_horizontal()
		vertical_or_horizontal = self.vertical_or_horizontal(random_vertical_or_horizontal)
		game = "Continue"
		while game == "Continue":
			guess_column = self.guess_column()
			guess_row = self.guess_row()
			#self.verify_shot(random_column, random_row, guess_column, guess_row)

	def my_board(self):
		for row in self.board:
			print " ".join(row)

	def put_ships_random(self):
		for ship in range(1,6):
			random_vertical_or_horizontal = self.random_vertical_or_horizontal()
			vertical_or_horizontal = self.vertical_or_horizontal()

	def random_vertical_or_horizontal(self):
		vertical_horizontal_random = random.randint(1, 2)
		print vertical_horizontal_random
		message = raw_input("el numero")
		if vertical_horizontal_random == 1:
			return "vertical"
		elif vertical_horizontal_random == 2:
			return "horizontal"

	def vertical_or_horizontal(self, random_vertical_or_horizontal):
		if random_vertical_or_horizontal == "vertical":
			#pass
			print "vertical"
			message = raw_input("vertical")
			self.ships_vertical_random()
		elif random_vertical_or_horizontal == "horizontal":
			print "horizontal"
			message = raw_input("horizontal")
			self.ships_vertical_random()

	def ships_vertical_random(self):
		random_column = self.random_column()
		random_row = self.random_row()
		print random_column, "column"
		print random_row,"row"
		self.board[random_row -1][random_column - 1] = "S"
		self.my_board()

	def random_column(self):
		return random.randint(1, len(self.board[0]))

	def random_row(self):
		return random.randint(1, len(self.board[0]))

	def guess_column(self):
		print "\nTry to guess the column where is hidden a part of a ship:"
		guess_column = int(raw_input("  > "))
		return guess_column

	def guess_row(self):
		print "Try to guess the row where is hidden a part of a ship:"
		guess_row = int(raw_input("  > "))
		return guess_row

	def verify_shot(self, random_column, random_row, guess_column, guess_row):
		if guess_column == random_column and guess_row == random_row:
			print "You guessed a part of the ship"
		else:
			if guess_column <= 0 or guess_column > len(self.board[0]) or guess_row <= 0 or guess_row > len(self.board[0]):
				print "This is outside of the board"
			else:
				print "You didn't guess any part of a ship\n"
				self.board[guess_row -1][guess_column - 1] = "X"
				self.my_board()
		message = raw_input("\nPRESS ENTER")

	def exit_program(self):
		os.system('reset')
		sys.exit()

user1 = my_game()
user1.menu()
