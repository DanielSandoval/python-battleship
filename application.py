# Aqui escribe tu codigo

import os
import sys
import random

class my_game(object):
	"""docstring for ClassName"""
	def __init__(self):
		'''self.board_inside_player1 = []
		self.board_outside_player1 = []'''
		'''self.board_inside_player2 = []
		self.board_outside_player2 = []'''
		'''self.board_inside_compu = []
		self.board_outside_compu = []'''
		self.menu_option = {1:self.single_player, 2:self.multi_player, 3:self.exit_program}

	def create_boards_compu(self):
		self.board_inside_compu = []
		self.board_outside_compu = []
		for x in xrange(1,16):
			self.board_inside_compu.append(["O"] * 15)
		for x in xrange(1,16):
			self.board_outside_compu.append(["O"] * 15)

	def create_boards_player1(self):
		self.board_inside_player1 = []
		self.board_outside_player1 = []
		for x in xrange(1,16):
			self.board_inside_player1.append(["O"] * 15)
		for x in xrange(1,16):
			self.board_outside_player1.append(["O"] * 15)

	def create_boards_player2(self):
		self.board_inside_player2 = []
		self.board_outside_player2 = []
		for x in xrange(1,16):
			self.board_inside_player2.append(["O"] * 15)
		for x in xrange(1,16):
			self.board_outside_player2.append(["O"] * 15)

	def my_board_inside_player1(self):
		#os.system('reset')
		print "BOARD INSIDE PLAYER 1\n"
		for row in self.board_inside_player1:
			print " ".join(row)

	def my_board_outside_player1(self):
		#os.system('reset')
		print "BOARD OUTSIDE PLAYER 1\n"
		for row in self.board_outside_player1:
			print " ".join(row)

	def my_board_inside_player2(self):
		#os.system('reset')
		print "BOARD INSIDE PLAYER 2\n"
		for row in self.board_inside_player2:
			print " ".join(row)

	def my_board_outside_player2(self):
		#os.system('reset')
		print "BOARD OUTSIDE PLAYER 2\n"
		for row in self.board_outside_player2:
			print " ".join(row)

	def my_board_inside_compu(self):
		#os.system('reset')
		print "BOARD INSIDE COMPU\n"
		for row in self.board_inside_compu:
			print " ".join(row)

	def my_board_outside_compu(self):
		#os.system('reset')
		print "BOARD OUTSIDE COMPU\n"
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
		self.create_boards_compu()
		self.create_boards_player1()
		self.put_ships("random", self.board_inside_compu, self.my_board_inside_compu, self.my_board_outside_compu, "COMPU")
		os.system('reset')
		self.my_board_outside_player1()
		#print ""
		self.put_ships("no random", self.board_inside_player1, self.my_board_inside_player1, self.my_board_outside_player1, "PLAYER 1")
		game = True
		while game == True:
			os.system('reset')
			self.my_board_inside_compu()
			print ""
			self.my_board_outside_compu()
			self.turn_player_one(self.board_inside_compu, self.board_outside_compu, self.my_board_inside_compu, self.my_board_outside_compu, "PLAYER 1")
			game = self.win_or_no(self.board_inside_compu, self.board_outside_compu)
			if game == True:
				os.system('reset')
				'''self.my_board_inside_player1()
				print ""
				self.my_board_outside_player1()'''
				self.turn_computer_player(self.board_inside_player1, self.board_outside_player1, self.my_board_inside_player1, self.my_board_outside_player1, "COMPU")
				game = self.win_or_no(self.board_inside_player1, self.board_outside_player1)
		self.create_boards_compu()
		self.create_boards_player1()

	def multi_player(self):
		self.create_boards_player1()
		self.create_boards_player2()
		os.system('reset')
		self.my_board_outside_player1()
		#print ""
		self.put_ships("no random", self.board_inside_player1, self.my_board_inside_player1, self.my_board_outside_player1, "PLAYER 1")
		os.system('reset')
		self.my_board_outside_player2()
		self.put_ships("no random", self.board_inside_player2, self.my_board_inside_player2, self.my_board_outside_player2, "PLAYER 2")
		game = True
		while game == True:
			os.system('reset')
			self.my_board_inside_player2()
			print ""
			self.my_board_outside_player2()
			self.turn_player_one(self.board_inside_player2, self.board_outside_player2, self.my_board_inside_player2, self.my_board_outside_player2, "PLAYER 1")
			game = self.win_or_no(self.board_inside_player2, self.board_outside_player2)
			if game == True:
				os.system('reset')
				self.my_board_inside_player1()
				print ""
				self.my_board_outside_player1()
				self.turn_player_two(self.board_inside_player1, self.board_outside_player1, self.my_board_inside_player1, self.my_board_outside_player1, "PLAYER 2")
				game = self.win_or_no(self.board_inside_player1, self.board_outside_player1)
		self.create_boards_player1()
		self.create_boards_player2()


	def put_ships(self, condition, inside_list, inside_function, outside_function, player):
		#self.put_ships_four_pieces(condition, inside_list, inside_function, player)
		#self.put_ships_three_pieces(condition, inside_list, inside_function, player)
		self.put_ships_two_pieces(condition, inside_list, inside_function, outside_function, player)
		self.put_ships_one_pieces(condition, inside_list, inside_function, outside_function, player)
		#print ""
		#self.my_board_inside_compu()
		#message = raw_input("Final Put Ships")

	def vertical_or_horizontal(self, condition):
		#print "\n%s" % player
		if condition == "no random":
			vertical_or_horizontal = self.ask_vertical_or_horizontal()
		elif condition == "random":
			vertical_or_horizontal = self.random_vertical_or_horizontal()
		return vertical_or_horizontal

	def ask_vertical_or_horizontal(self):
		vertical_or_horizontal = raw_input("\nVertical or horizontal v/h: ")
		return vertical_or_horizontal

	def random_vertical_or_horizontal(self):
		vertical_horizontal_random = random.randint(1, 2)
		if vertical_horizontal_random == 1:
			return "v"
		elif vertical_horizontal_random == 2:
			return "h"

	def put_ships_four_pieces(self, condition, inside_list, inside_function, player):
		#print "\n%s" % player
		#print "Ship of four pieces"
		for x in xrange(1,3):
			print "\n%s" % player
			print "Ship of four pieces"
			#random_vertical_or_horizontal = self.random_vertical_or_horizontal()
			vertical_or_horizontal = self.vertical_or_horizontal(condition)
			if vertical_or_horizontal == "h":
				self.ship_four_horizontal(condition, inside_list, inside_function, player)
			elif vertical_or_horizontal == "v":
				self.ship_four_vertical(condition, inside_list, inside_function, player)

	def put_ships_three_pieces(self, condition, inside_list, inside_function, player):
		#print "\n%s" % player
		#print "Ship of three pieces"
		for x in xrange(1,4):
			print "\n%s" % player
			print "Ship of three pieces"
			#random_vertical_or_horizontal = self.random_vertical_or_horizontal()
			vertical_or_horizontal = self.vertical_or_horizontal(condition)
			if vertical_or_horizontal == "h":
				self.ship_three_horizontal(condition, inside_list, inside_function, player)
			elif vertical_or_horizontal == "v":
				self.ship_three_vertical(condition, inside_list, inside_function, player)

	def put_ships_two_pieces(self, condition, inside_list, inside_function, outside_function, player):
		#print "\n%s" % player
		#print "Ship of two pieces"
		for x in xrange(1,4):
			print "\n%s" % player
			print "Ship of two pieces"
			#random_vertical_or_horizontal = self.random_vertical_or_horizontal()
			vertical_or_horizontal = self.vertical_or_horizontal(condition)
			if vertical_or_horizontal == "h":
				self.ship_two_horizontal(condition, inside_list, inside_function, outside_function, player)
			elif vertical_or_horizontal == "v":
				self.ship_two_vertical(condition, inside_list, inside_function, outside_function, player)

	def put_ships_one_pieces(self, condition, inside_list, inside_function, outside_function, player):
		for x in xrange(1,3):
			print "\n%s" % player
			print "Ship of one piece"
			self.ship_one_both(condition, inside_list, inside_function, outside_function, player)
		print "\nYou put your ships on the board"

	def ship_four_horizontal(self, condition, inside_list, inside_function, player):
		column = self.column(condition,12)
		row = self.row(condition,12)
		#print column
		#print row
		try:
			if (column < 12 and ("S" in inside_list[row - 1][column + 3] or "S" in inside_list[row - 1][column + 2] or "S" in inside_list[row - 1][column + 1] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2]))\
				or (column == 12 and ("S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2]))\
				or ("S" in inside_list[row - 2][column + 3] or "S" in inside_list[row - 2][column + 2] or "S" in inside_list[row - 2][column + 1] or "S" in inside_list[row - 2][column] or "S" in inside_list[row - 2][column - 1] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row][column + 3] or "S" in inside_list[row][column + 2] or "S" in inside_list[row][column + 1] or "S" in inside_list[row][column] or "S" in inside_list[row][column - 1] or "S" in inside_list[row][column - 2]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_four_horizontal(condition, inside_list, inside_function, player)
			else:
				inside_list[row -1][column - 1] = "S"
				for x in xrange(1,4):
					column += 1
					inside_list[row -1][column - 1] = "S"
				self.decide_if_print_board(condition, inside_function)
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_four_horizontal(condition, inside_list, inside_function, player)
		#message = raw_input("Final ship for one")

	def ship_four_vertical(self, condition, inside_list, inside_function, player):
		column = self.column(condition,12)
		row = self.row(condition,12)
		#print column
		#print row
		try:
			if (row < 12 and ("S" in inside_list[row + 3][column - 1] or "S" in inside_list[row + 2][column - 1] or "S" in inside_list[row + 1][column - 1] or "S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1]))\
				or (row == 12 and ("S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1]))\
				or ("S" in inside_list[row + 3][column - 2] or "S" in inside_list[row + 2][column - 2] or "S" in inside_list[row + 1][column - 2] or "S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row + 3][column] or "S" in inside_list[row + 2][column] or "S" in inside_list[row + 1][column] or "S" in inside_list[row][column] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 2][column]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_four_vertical(condition, inside_list, inside_function, player)
			else:
				inside_list[row - 1][column - 1] = "S"
				for x in xrange(1,4):
					row += 1
					inside_list[row - 1][column - 1] = "S"
				self.decide_if_print_board(condition, inside_function)
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_four_vertical(condition, inside_list, inside_function, player)
		#message = raw_input("Final ship for one")

	def ship_three_horizontal(self, condition, inside_list, inside_function, player):
		column = self.column(condition,13)
		row = self.row(condition,13)
		#print column
		#print row
		try:
			if (column < 13 and ("S" in inside_list[row - 1][column + 2] or "S" in inside_list[row - 1][column + 1] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2]))\
				or (column == 13 and ("S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2]))\
				or ("S" in inside_list[row - 2][column + 2] or "S" in inside_list[row - 2][column + 1] or "S" in inside_list[row - 2][column] or "S" in inside_list[row - 2][column - 1] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row][column + 2] or "S" in inside_list[row][column + 1] or "S" in inside_list[row][column] or "S" in inside_list[row][column - 1] or "S" in inside_list[row][column - 2]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_three_horizontal(condition, inside_list, inside_function, player)
			else:
				inside_list[row - 1][column - 1] = "S"
				for x in xrange(1,3):
					column += 1
					inside_list[row - 1][column - 1] = "S"
				self.decide_if_print_board(condition, inside_function)
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_three_horizontal(condition, inside_list, inside_function, player)
		#message = raw_input("Final ship for one")

	def ship_three_vertical(self, condition, inside_list, inside_function, player):
		column = self.column(condition,13)
		row = self.row(condition,13)
		#print column
		#print row
		try:
			if (row < 13 and ("S" in inside_list[row + 2][column - 1] or "S" in inside_list[row + 1][column - 1] or "S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1]))\
				or (row == 13 and ("S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1]))\
				or ("S" in inside_list[row + 2][column - 2] or "S" in inside_list[row + 1][column - 2] or "S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row + 2][column] or "S" in inside_list[row + 1][column] or "S" in inside_list[row][column] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 2][column]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_three_vertical(condition, inside_list, inside_function, player)
			else:
				inside_list[row - 1][column - 1] = "S"
				for x in xrange(1,3):
					row += 1
					inside_list[row - 1][column - 1] = "S"
				self.decide_if_print_board(condition, inside_function)
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_three_vertical(condition, inside_list, inside_function, player)
		#message = raw_input("Final ship for one")

	def ship_two_horizontal(self, condition, inside_list, inside_function, outside_function, player):
		'''inside_function()
		outside_function()'''
		column = self.column(condition,14)
		row = self.row(condition,14)
		#print column
		#print row
		try:
			if (column < 14 and ("S" in inside_list[row - 1][column + 1] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2]))\
				or (column == 14 and ("S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2]))\
				or ("S" in inside_list[row - 2][column + 1] or "S" in inside_list[row - 2][column] or "S" in inside_list[row - 2][column - 1] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row][column + 1] or "S" in inside_list[row][column] or "S" in inside_list[row][column - 1] or "S" in inside_list[row][column - 2]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_two_horizontal(condition, inside_list, inside_function, outside_function, player)
			else:
				inside_list[row - 1][column - 1] = "S"
				for x in xrange(1,2):
					column += 1
					inside_list[row - 1][column - 1] = "S"
				self.decide_if_print_board(condition, inside_function)
				#message = raw_input("two pieces")
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_two_horizontal(condition, inside_list, inside_function, outside_function, player)
		#message = raw_input("Final ship for one")

	def ship_two_vertical(self, condition, inside_list, inside_function, outside_function, player):
		'''inside_function()
		outside_function()'''
		column = self.column(condition,14)
		row = self.row(condition,14)
		#print column
		#print row
		try:
			if (row < 14 and ("S" in inside_list[row + 1][column - 1] or "S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1]))\
				or (row == 14 and ("S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1]))\
				or ("S" in inside_list[row + 1][column - 2] or "S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row + 1][column] or "S" in inside_list[row][column] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 2][column]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_two_vertical(condition, inside_list, inside_function, outside_function, player)
			else:
				inside_list[row - 1][column - 1] = "S"
				for x in xrange(1,2):
					row += 1
					inside_list[row - 1][column - 1] = "S"
				self.decide_if_print_board(condition, inside_function)
				#message = raw_input("two pieces")
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_two_vertical(condition, inside_list, inside_function, outside_function, player)
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

	def ship_one_both(self, condition, inside_list, inside_function, outside_function, player):
		'''inside_function()
		outside_function()'''
		#print "\n%s" % player
		#random_column = random.randint(1,15)
		#random_row = self.random_row()
		column = self.column(condition, 15)
		row = self.row(condition, 15)
		#print column
		#print row
		#"S" in inside_list[row - 1][column] or
		try:
			if (column < 15 and (row < 15 and ("S" in inside_list[row - 1][column + 1] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2]))\
				or ("S" in inside_list[row + 1][column - 1] or "S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1])\
				or ("S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1]))\
				or (column == 15 and ("S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2])):#\
				'''or (row < 15 and ("S" in inside_list[row + 1][column - 1] or "S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1]))\
				or (row == 15 and ("S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1]))\
				or ("S" in inside_list[row - 1][column + 1] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2])\
				or ("S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2]):'''
				#message = raw_input("Already there is a ship in this position")
				self.ship_one_both(condition, inside_list, inside_function, outside_function, player)
			else:
				inside_list[row - 1][column - 1] = "S"
				self.decide_if_print_board(condition, inside_function)
		except IndexError:
			message = raw_input("Out of the board")
			self.ship_one_both(condition, inside_list, inside_function, outside_function, player)
		#message = raw_input("Final ship for one")

	def decide_if_print_board(self, condition, inside_function):
		if condition == "no random":
			inside_function()

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
		os.system('reset')
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

	def turn_player_one(self, inside_list, outside_list, inside_function, outside_function, player):
		print "\n%s" % player
		guess_column = self.guess_column()
		guess_row = self.guess_row()
		self.verify_shot(False, guess_column, guess_row, inside_list, outside_list, inside_function, outside_function, player)
		#game_over = self.win_or_no()

	def turn_player_two(self, inside_list, outside_list, inside_function, outside_function, player):
		print "\n%s" % player
		guess_column = self.guess_column()
		guess_row = self.guess_row()
		self.verify_shot(False, guess_column, guess_row, inside_list, outside_list, inside_function, outside_function, player)

	def turn_computer_player(self, inside_list, outside_list, inside_function, outside_function, player):
		random_column = self.random_column()
		random_row = self.random_row()
		self.verify_shot(True,random_column, random_row, inside_list, outside_list, inside_function, outside_function, player)

	def guess_column(self):
		print "\nTry to guess the column where is hidden a part of a ship:"
		guess_column = raw_input("  > ")
		guess_column = self.guess_column_int(guess_column)
		return guess_column

	def guess_row(self):
		print "Try to guess the row where is hidden a part of a ship:"
		guess_row = raw_input("  > ")
		guess_row = self.guess_row_int(guess_row)
		os.system('reset')
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

	def verify_shot(self,true_or_false, column, row, inside_list, outside_list, inside_function, outside_function, player):
		if column <= 0 or column > len(inside_list[0]) or row <= 0 or row > len(inside_list[0]):
			print "\nThis is outside of the board\n"
		else:
			if inside_list[row - 1][column - 1] == "S":
				outside_list[row - 1][column - 1] = "S"
				inside_function()
				print ""
				outside_function()
				print "\n%s" % player
				self.decide_print_coordenates(true_or_false, player, column, row)
				message = raw_input("\nYou guessed a part of the ship")
			else:
				outside_list[row -1][column - 1] = "X"
				inside_function()
				print ""
				outside_function()
				print "\n%s" % player
				self.decide_print_coordenates(true_or_false, player, column, row)
				message =  raw_input("\nYou didn't guess any part of a ship")
			#os.system('reset')
		#self.win_or_no()
		#message = raw_input("PRESS ENTER")

	def decide_print_coordenates(self,true_or_false, player, column, row):
		if true_or_false == True:
			print "\n%s shot in this position:" % player
			print "Column: %s" % column
			print "Row %s" % row

	def compare_boards(self, inside_list, outside_list):
		"""Compare the boards to know if somebody win the game"""
		times_in_board_inside = 0
		for row in inside_list:
			times_in_board_inside += row.count("S")
		times_in_board_outside = 0
		for row in outside_list:
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
