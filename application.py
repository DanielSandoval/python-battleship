# Aqui escribe tu codigo

import os
import sys
import random
#import pygame

class my_game(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.board_inside_player1 = []
		self.board_outside_player1 = []
		self.board_inside_player2 = []
		self.board_outside_player2 = []
		self.board_inside_compu = []
		self.board_outside_compu = []
		self.menu_option = {1:self.single_player, 2:self.multi_player, 3:self.exit_program}
		for x in xrange(1,16):
			self.board_inside_compu.append(["O"] * 15)
		for x in xrange(1,16):
			self.board_outside_compu.append(["O"] * 15)
		for x in xrange(1,16):
			self.board_inside_player1.append(["O"] * 15)
		for x in xrange(1,16):
			self.board_outside_player1.append(["O"] * 15)
		for x in xrange(1,16):
			self.board_inside_player2.append(["O"] * 15)
		for x in xrange(1,16):
			self.board_outside_player2.append(["O"] * 15)

	def my_board_inside_player1(self):
		for row in self.board_inside_player1:
			print " ".join(row)

	def my_board_outside_player1(self):
		for row in self.board_outside_player1:
			print " ".join(row)

	def my_board_inside_player2(self):
		for row in self.board_inside_player2:
			print " ".join(row)

	def my_board_outside_player2(self):
		for row in self.board_outside_player2:
			print " ".join(row)

	def my_board_inside_compu(self):
		for row in self.board_inside_compu:
			print " ".join(row)

	def my_board_outside_compu(self):
		for row in self.board_outside_compu:
			print " ".join(row)

	def menu(self):
		while True:
			os.system('reset')
			self.menu_print()
			menu_ask_option = self.menu_ask_option()
			menu_perform_action = self.menu_perform_action(menu_ask_option)

	def menu_ask_option(self):
		ask_option = raw_input("Select the option you want: ")
		try:
			ask_option = int(ask_option)
		except ValueError:
			pass
		return ask_option

	def menu_perform_action(self, menu_ask_option):
		if menu_ask_option in self.menu_option.keys():
			option_menu = self.menu_option[menu_ask_option]
			option_menu()
		else:
			message = raw_input("Invalid option")

	def menu_print(self):
		print "1.ONE PLAYER"
		print "2.TWO PLAYERS"
		print "3.EXIT"

	def single_player(self):
		os.system('reset')
		self.my_board_inside_compu()
		print ""
		#self.put_ships_random()
		self.put_ships_one_pieces("random", self.board_inside_compu)
		#self.put_ships_one_pieces("no random", self.board_inside_player1)
		game = True
		while game == True:
			self.my_board_inside_compu()
			print ""
			self.my_board_outside_compu()
			#self.my_board_inside_player1()
			print ""
			#self.my_board_outside_player1()
			self.turn_player_one(self.board_inside_compu, self.board_outside_compu, self.my_board_inside_compu, self.my_board_outside_compu)
			#self.turn_computer_player(self.board_inside_player1, self.board_outside_player1)
			game = self.win_or_no(self.board_inside_compu, self.board_outside_compu)

	def multi_player(self):
		os.system('reset')
		self.my_board_inside_player2()
		print ""
		#self.put_ships_one_pieces("no random", self.board_inside_player1)
		self.put_ships_one_pieces("no random", self.board_inside_player2)
		game = True
		while game == True:
			#self.my_board_inside_player1()
			print ""
			#self.my_board_outside_player1()
			'''self.my_board_inside_player2()
			print ""
			self.my_board_outside_player2()'''
			#self.turn_player_two(self.board_inside_player2, self.board_outside_player2)
			self.turn_player_one(self.board_inside_player2, self.board_outside_player2, self.my_board_inside_player2, self.my_board_outside_player2)
			game = self.win_or_no(self.board_inside_player2, self.board_outside_player2)


	def put_ships_random(self):
		self.put_ships_four_pieces()
		#message = raw_input("ships of four pieces")
		self.put_ships_three_pieces()
		#message = raw_input("ships of there pieces")
		self.put_ships_two_pieces()
		#message = raw_input("ships of two pieces")
		self.put_ships_one_pieces()
		#message = raw_input("ships of one pieces")
		print ""
		self.my_board_inside_compu()
		message = raw_input("Final Put Ships")

	def random_vertical_or_horizontal(self):
		vertical_horizontal_random = random.randint(1, 2)
		if vertical_horizontal_random == 1:
			return "vertical"
		elif vertical_horizontal_random == 2:
			return "horizontal"

	def put_ships_four_pieces(self):
		for x in xrange(1,3):
			random_vertical_or_horizontal = self.random_vertical_or_horizontal()
			if random_vertical_or_horizontal == "horizontal":
				self.ship_four_horizontal()
			elif random_vertical_or_horizontal == "vertical":
				self.ship_four_vertical()

	def put_ships_three_pieces(self):
		for x in xrange(1,4):
			random_vertical_or_horizontal = self.random_vertical_or_horizontal()
			if random_vertical_or_horizontal == "horizontal":
				self.ship_three_horizontal()
			elif random_vertical_or_horizontal == "vertical":
				self.ship_three_vertical()

	def put_ships_two_pieces(self):
		for x in xrange(1,4):
			random_vertical_or_horizontal = self.random_vertical_or_horizontal()
			if random_vertical_or_horizontal == "horizontal":
				self.ship_two_horizontal()
			elif random_vertical_or_horizontal == "vertical":
				self.ship_two_vertical()

	'''def put_ships_one_pieces(self, condition):
		for x in xrange(1,6):
			self.ship_one_both(condition)'''

	def put_ships_one_pieces(self, condition, my_list):
		for x in xrange(1,6):
			self.ship_one_both(condition, my_list)

	def ship_four_horizontal(self):
		random_column = random.randint(1,12)
		random_row = self.random_row()
		#print random_column
		#print random_row
		try:
			if (random_column < 12 and ("S" in self.board_inside_compu[random_row - 1][random_column + 3] or "S" in self.board_inside_compu[random_row - 1][random_column + 2] or "S" in self.board_inside_compu[random_row - 1][random_column + 1] or "S" in self.board_inside_compu[random_row - 1][random_column] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 2]))\
				or (random_column == 12 and ("S" in self.board_inside_compu[random_row - 1][random_column] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 2]))\
				or ("S" in self.board_inside_compu[random_row - 2][random_column + 3] or "S" in self.board_inside_compu[random_row - 2][random_column + 2] or "S" in self.board_inside_compu[random_row - 2][random_column + 1] or "S" in self.board_inside_compu[random_row - 2][random_column] or "S" in self.board_inside_compu[random_row - 2][random_column - 1] or "S" in self.board_inside_compu[random_row - 2][random_column - 2])\
				or ("S" in self.board_inside_compu[random_row][random_column + 3] or "S" in self.board_inside_compu[random_row][random_column + 2] or "S" in self.board_inside_compu[random_row][random_column + 1] or "S" in self.board_inside_compu[random_row][random_column] or "S" in self.board_inside_compu[random_row][random_column - 1] or "S" in self.board_inside_compu[random_row][random_column - 2]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_four_horizontal()
			else:
				self.board_inside_compu[random_row -1][random_column - 1] = "S"
				for x in xrange(1,4):
					random_column += 1
					self.board_inside_compu[random_row -1][random_column - 1] = "S"
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_four_horizontal()
		#message = raw_input("Final ship for one")

	def ship_four_vertical(self):
		random_column = self.random_column()
		random_row = random.randint(1,12)
		#print random_column
		#print random_row
		try:
			if (random_row < 12 and ("S" in self.board_inside_compu[random_row + 3][random_column - 1] or "S" in self.board_inside_compu[random_row + 2][random_column - 1] or "S" in self.board_inside_compu[random_row + 1][random_column - 1] or "S" in self.board_inside_compu[random_row][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 2][random_column - 1]))\
				or (random_row == 12 and ("S" in self.board_inside_compu[random_row][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 2][random_column - 1]))\
				or ("S" in self.board_inside_compu[random_row + 3][random_column - 2] or "S" in self.board_inside_compu[random_row + 2][random_column - 2] or "S" in self.board_inside_compu[random_row + 1][random_column - 2] or "S" in self.board_inside_compu[random_row][random_column - 2] or "S" in self.board_inside_compu[random_row - 1][random_column - 2] or "S" in self.board_inside_compu[random_row - 2][random_column - 2])\
				or ("S" in self.board_inside_compu[random_row + 3][random_column] or "S" in self.board_inside_compu[random_row + 2][random_column] or "S" in self.board_inside_compu[random_row + 1][random_column] or "S" in self.board_inside_compu[random_row][random_column] or "S" in self.board_inside_compu[random_row - 1][random_column] or "S" in self.board_inside_compu[random_row - 2][random_column]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_four_vertical()
			else:
				self.board_inside_compu[random_row - 1][random_column - 1] = "S"
				for x in xrange(1,4):
					random_row += 1
					self.board_inside_compu[random_row - 1][random_column - 1] = "S"
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_four_vertical()
		#message = raw_input("Final ship for one")

	def ship_three_horizontal(self):
		random_column = random.randint(1,13)
		random_row = self.random_row()
		#print random_column
		#print random_row
		try:
			if (random_column < 13 and ("S" in self.board_inside_compu[random_row - 1][random_column + 2] or "S" in self.board_inside_compu[random_row - 1][random_column + 1] or "S" in self.board_inside_compu[random_row - 1][random_column] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 2]))\
				or (random_column == 13 and ("S" in self.board_inside_compu[random_row - 1][random_column] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 2]))\
				or ("S" in self.board_inside_compu[random_row - 2][random_column + 2] or "S" in self.board_inside_compu[random_row - 2][random_column + 1] or "S" in self.board_inside_compu[random_row - 2][random_column] or "S" in self.board_inside_compu[random_row - 2][random_column - 1] or "S" in self.board_inside_compu[random_row - 2][random_column - 2])\
				or ("S" in self.board_inside_compu[random_row][random_column + 2] or "S" in self.board_inside_compu[random_row][random_column + 1] or "S" in self.board_inside_compu[random_row][random_column] or "S" in self.board_inside_compu[random_row][random_column - 1] or "S" in self.board_inside_compu[random_row][random_column - 2]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_three_horizontal()
			else:
				self.board_inside_compu[random_row - 1][random_column - 1] = "S"
				for x in xrange(1,3):
					random_column += 1
					self.board_inside_compu[random_row - 1][random_column - 1] = "S"
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_three_horizontal()
		#message = raw_input("Final ship for one")

	def ship_three_vertical(self):
		random_column = self.random_column()
		random_row = random.randint(1,13)
		#print random_column
		#print random_row
		try:
			if (random_row < 13 and ("S" in self.board_inside_compu[random_row + 2][random_column - 1] or "S" in self.board_inside_compu[random_row + 1][random_column - 1] or "S" in self.board_inside_compu[random_row][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 2][random_column - 1]))\
				or (random_row == 13 and ("S" in self.board_inside_compu[random_row][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 2][random_column - 1]))\
				or ("S" in self.board_inside_compu[random_row + 2][random_column - 2] or "S" in self.board_inside_compu[random_row + 1][random_column - 2] or "S" in self.board_inside_compu[random_row][random_column - 2] or "S" in self.board_inside_compu[random_row - 1][random_column - 2] or "S" in self.board_inside_compu[random_row - 2][random_column - 2])\
				or ("S" in self.board_inside_compu[random_row + 2][random_column] or "S" in self.board_inside_compu[random_row + 1][random_column] or "S" in self.board_inside_compu[random_row][random_column] or "S" in self.board_inside_compu[random_row - 1][random_column] or "S" in self.board_inside_compu[random_row - 2][random_column]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_three_vertical()
			else:
				self.board_inside_compu[random_row - 1][random_column - 1] = "S"
				for x in xrange(1,3):
					random_row += 1
					self.board_inside_compu[random_row - 1][random_column - 1] = "S"
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_three_vertical()
		#message = raw_input("Final ship for one")

	def ship_two_horizontal(self):
		random_column = random.randint(1,14)
		random_row = self.random_row()
		#print random_column
		#print random_row
		try:
			if (random_column < 14 and ("S" in self.board_inside_compu[random_row - 1][random_column + 1] or "S" in self.board_inside_compu[random_row - 1][random_column] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 2]))\
				or (random_column == 14 and ("S" in self.board_inside_compu[random_row - 1][random_column] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 2]))\
				or ("S" in self.board_inside_compu[random_row - 2][random_column + 1] or "S" in self.board_inside_compu[random_row - 2][random_column] or "S" in self.board_inside_compu[random_row - 2][random_column - 1] or "S" in self.board_inside_compu[random_row - 2][random_column - 2])\
				or ("S" in self.board_inside_compu[random_row][random_column + 1] or "S" in self.board_inside_compu[random_row][random_column] or "S" in self.board_inside_compu[random_row][random_column - 1] or "S" in self.board_inside_compu[random_row][random_column - 2]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_two_horizontal()
			else:
				self.board_inside_compu[random_row - 1][random_column - 1] = "S"
				for x in xrange(1,2):
					random_column += 1
					self.board_inside_compu[random_row - 1][random_column - 1] = "S"
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_two_horizontal()
		#message = raw_input("Final ship for one")

	def ship_two_vertical(self):
		random_column = self.random_column()
		random_row = random.randint(1,14)
		#print random_column
		#print random_row
		try:
			if (random_row < 14 and ("S" in self.board_inside_compu[random_row + 1][random_column - 1] or "S" in self.board_inside_compu[random_row][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 2][random_column - 1]))\
				or (random_row == 14 and ("S" in self.board_inside_compu[random_row][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 2][random_column - 1]))\
				or ("S" in self.board_inside_compu[random_row + 1][random_column - 2] or "S" in self.board_inside_compu[random_row][random_column - 2] or "S" in self.board_inside_compu[random_row - 1][random_column - 2] or "S" in self.board_inside_compu[random_row - 2][random_column - 2])\
				or ("S" in self.board_inside_compu[random_row + 1][random_column] or "S" in self.board_inside_compu[random_row][random_column] or "S" in self.board_inside_compu[random_row - 1][random_column] or "S" in self.board_inside_compu[random_row - 2][random_column]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_two_vertical()
			else:
				self.board_inside_compu[random_row - 1][random_column - 1] = "S"
				for x in xrange(1,2):
					random_row += 1
					self.board_inside_compu[random_row - 1][random_column - 1] = "S"
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_two_vertical()
		#message = raw_input("Final ship for one")

	'''def ship_one_both(self):
		random_column = random.randint(1,15)
		random_row = self.random_row()
		#print random_column
		#print random_row
		try:
			if (random_column < 15 and ("S" in self.board_inside_compu[random_row - 1][random_column + 1] or "S" in self.board_inside_compu[random_row - 1][random_column] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 2]))\
				or (random_column == 15 and ("S" in self.board_inside_compu[random_row - 1][random_column] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 2]))\
				or ("S" in self.board_inside_compu[random_row + 1][random_column - 1] or "S" in self.board_inside_compu[random_row][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 2][random_column - 1])\
				or ("S" in self.board_inside_compu[random_row][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 2][random_column - 1]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_one_both()
			else:
				self.board_inside_compu[random_row - 1][random_column - 1] = "S"
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_one_both()
		#message = raw_input("Final ship for one")'''

	'''def ship_one_both(self, condition):
		#random_column = random.randint(1,15)
		#random_row = self.random_row()
		random_column = self.column(condition, 15)
		random_row = self.row(condition, 15)
		#print random_column
		#print random_row
		try:
			if (random_column < 15 and ("S" in self.board_inside_compu[random_row - 1][random_column + 1] or "S" in self.board_inside_compu[random_row - 1][random_column] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 2]))\
				or (random_column == 15 and ("S" in self.board_inside_compu[random_row - 1][random_column] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 2]))\
				or ("S" in self.board_inside_compu[random_row + 1][random_column - 1] or "S" in self.board_inside_compu[random_row][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 2][random_column - 1])\
				or ("S" in self.board_inside_compu[random_row][random_column - 1] or "S" in self.board_inside_compu[random_row - 1][random_column - 1] or "S" in self.board_inside_compu[random_row - 2][random_column - 1]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_one_both(condition)
			else:
				self.board_inside_compu[random_row - 1][random_column - 1] = "S"
				self.decide_if_print_board(condition)
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_one_both(condition)
		message = raw_input("Final ship for one")'''

	def ship_one_both(self, condition, my_list):
		#random_column = random.randint(1,15)
		#random_row = self.random_row()
		random_column = self.column(condition, 15)
		random_row = self.row(condition, 15)
		#print random_column
		#print random_row
		try:
			if (random_column < 15 and ("S" in my_list[random_row - 1][random_column + 1] or "S" in my_list[random_row - 1][random_column] or "S" in my_list[random_row - 1][random_column - 1] or "S" in my_list[random_row - 1][random_column - 2]))\
				or (random_column == 15 and ("S" in my_list[random_row - 1][random_column] or "S" in my_list[random_row - 1][random_column - 1] or "S" in my_list[random_row - 1][random_column - 2]))\
				or ("S" in my_list[random_row + 1][random_column - 1] or "S" in my_list[random_row][random_column - 1] or "S" in my_list[random_row - 1][random_column - 1] or "S" in my_list[random_row - 2][random_column - 1])\
				or ("S" in my_list[random_row][random_column - 1] or "S" in my_list[random_row - 1][random_column - 1] or "S" in my_list[random_row - 2][random_column - 1]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_one_both(condition, my_list)
			else:
				my_list[random_row - 1][random_column - 1] = "S"
				self.decide_if_print_board(condition)
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_one_both(condition, my_list)
		message = raw_input("Final ship for one")

	def decide_if_print_board(self, condition):
		if condition == "no random":
			self.my_board_inside_player1()

	def column(self, condition, end_range):
		if condition == "random":
			column = random.randint(1, end_range)
		elif condition == "no random":
			column = self.ask_column_position()
		return column

	def ask_column_position(self):
		print "\nEnter the column where you want to start the ship"
		column_position = raw_input(" > ")
		column_position = self.ask_column_position_int(column_position)
		return column_position

	def ask_column_position_int(self, column_position):
		try:
			column_position = int(column_position)
		except ValueError:
			pass
		return column_position

	def row(self, condition, end_range):
		if condition == "random":
			row = random.randint(1, end_range)
		elif condition == "no random":
			row = self.ask_row_position()
		return row

	def ask_row_position(self):
		print "Enter the row where you want to start the ship"
		row_position = raw_input(" > ")
		row_position = self.ask_row_position_int(row_position)
		return row_position

	def ask_row_position_int(self, row_position):
		try:
			row_position = int(row_position)
		except ValueError:
			pass
		return row_position

	def random_column(self):
		return random.randint(1, len(self.board_inside_compu[0]))

	def random_row(self):
		return random.randint(1, len(self.board_inside_compu[0]))

	def turn_player_one(self, inside_list, outside_list, inside_function, outside_function):
		#game_over = False
		#while game_over == False:
		guess_column = self.guess_column()
		guess_row = self.guess_row()
		self.verify_shot(guess_column, guess_row, inside_list, outside_list, inside_function, outside_function)
		#game_over = self.win_or_no()

	def turn_player_two(self, inside_list, outside_list, inside_function, outside_function):
		guess_column = self.guess_column()
		guess_row = self.guess_row()
		self.verify_shot(guess_column, guess_row, inside_list, outside_list)

	def turn_computer_player(self, inside_list, outside_list, inside_function, outside_function):
		random_column = self.random_column()
		random_row = self.random_row()
		self.verify_shot(random_column, random_row, inside_list, outside_list)

	def guess_column(self):
		print "\nTry to guess the column where is hidden a part of a ship:"
		guess_column = raw_input("  > ")
		guess_column = self.guess_column_int(guess_column)
		return guess_column

	def guess_row(self):
		print "Try to guess the row where is hidden a part of a ship:"
		guess_row = raw_input("  > ")
		guess_row = self.guess_row_int(guess_row)
		return guess_row

	def guess_column_int(self, guess_column):
		guess_column = int(guess_column)
		return guess_column

	def guess_row_int(self, guess_row):
		guess_row = int(guess_row)
		return guess_row

	'''def verify_shot(self, guess_column, guess_row):
		if guess_column <= 0 or guess_column > len(self.board_inside_compu[0]) or guess_row <= 0 or guess_row > len(self.board_inside_compu[0]):
			print "\nThis is outside of the board\n"
		else:
			if self.board_inside_compu[guess_row - 1][guess_column - 1] == "S":
				print "\nYou guessed a part of the ship\n"
				self.board_outside_compu[guess_row - 1][guess_column - 1] = "S"
			else:
				print "\nYou didn't guess any part of a ship\n"
				self.board_outside_compu[guess_row -1][guess_column - 1] = "X"
			self.my_board_inside_compu()
			print ""
			self.my_board_outside_compu()
		#self.win_or_no()
		message = raw_input("PRESS ENTER")'''

	def verify_shot(self, column, row, inside_list, outside_list, inside_function, outside_function):
		if column <= 0 or column > len(inside_list[0]) or row <= 0 or row > len(inside_list[0]):
			print "\nThis is outside of the board\n"
		else:
			if inside_list[row - 1][column - 1] == "S":
				print "\nYou guessed a part of the ship\n"
				outside_list[row - 1][column - 1] = "S"
			else:
				message =  raw_input("\nYou didn't guess any part of a ship")
				outside_list[row -1][column - 1] = "X"
			inside_function()
			print ""
			outside_function()
		#self.win_or_no()
		message = raw_input("PRESS ENTER")

	def compare_boards(self, inside_list, outside_list):
		"""Compare the boards to know if somebody win the game"""
		times_in_board_inside = 0
		for row in self.board_inside_compu:
			times_in_board_inside += row.count("S")
		times_in_board_outside = 0
		for row in self.board_outside_compu:
			times_in_board_outside += row.count("S")
		return times_in_board_inside, times_in_board_outside

	def win_or_no(self, inside_list, outside_list):
		times_in_board_inside, times_in_board_outside = self.compare_boards(inside_list, outside_list)
		if times_in_board_inside == times_in_board_outside:
			game = False
			message = raw_input("You won the game")
		else:
			game = True
		return game

	def exit_program(self):
		os.system('reset')
		sys.exit()

user1 = my_game()
user1.menu()
