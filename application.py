# -*- encoding: utf-8 -*-
# Aqui escribe tu codigo

import os
import sys
import random
import platform

class my_game(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.menu_option = {1:self.single_player, 2:self.multi_player, 3:self.exit_program}
		self.operative_system = platform.system()

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
		#self.clean_screen()
		print """
		 _____               _    _____ _                    ___   
		| __  |___ ___ ___ _| |  |  _  | |___ _ _ ___ ___   |_  |  
		| __ -| . | .'|  _| . |  |   __| | .'| | | -_|  _|   _| |_ 
		|_____|___|__,|_| |___|  |__|  |_|__,|_  |___|_|    |_____|
		                                     |___|                 
		"""
		#print "BOARD INSIDE PLAYER 1\n"
		for row in self.board_inside_player1:
			print " ".join(row)

	def my_board_outside_player1(self):
		#self.clean_screen()
		print """
		 _____               _    _____ _                    ___   
		| __  |___ ___ ___ _| |  |  _  | |___ _ _ ___ ___   |_  |  
		| __ -| . | .'|  _| . |  |   __| | .'| | | -_|  _|   _| |_ 
		|_____|___|__,|_| |___|  |__|  |_|__,|_  |___|_|    |_____|
		                                     |___|                 
		"""
		#print "BOARD OUTSIDE PLAYER 1\n"
		for row in self.board_outside_player1:
			print " ".join(row)

	def my_board_inside_player2(self):
		#self.clean_screen()
		print """
		 _____               _    _____ _                    ___ 
		| __  |___ ___ ___ _| |  |  _  | |___ _ _ ___ ___   |_  |
		| __ -| . | .'|  _| . |  |   __| | .'| | | -_|  _|  |  _|
		|_____|___|__,|_| |___|  |__|  |_|__,|_  |___|_|    |___|
		                                     |___|               
		"""
		#print "BOARD INSIDE PLAYER 2\n"
		for row in self.board_inside_player2:
			print " ".join(row)

	def my_board_outside_player2(self):
		#self.clean_screen()
		print """
		 _____               _    _____ _                    ___ 
		| __  |___ ___ ___ _| |  |  _  | |___ _ _ ___ ___   |_  |
		| __ -| . | .'|  _| . |  |   __| | .'| | | -_|  _|  |  _|
		|_____|___|__,|_| |___|  |__|  |_|__,|_  |___|_|    |___|
		                                     |___|               
		"""
		#print "BOARD OUTSIDE PLAYER 2\n"
		for row in self.board_outside_player2:
			print " ".join(row)

	def my_board_inside_compu(self):
		#self.clean_screen()
		print """
		 _____               _    _____                   
		| __  |___ ___ ___ _| |  |     |___ _____ ___ _ _ 
		| __ -| . | .'|  _| . |  |   --| . |     | . | | |
		|_____|___|__,|_| |___|  |_____|___|_|_|_|  _|___|
		                                         |_|      
		"""
		#print "BOARD INSIDE COMPU\n"
		for row in self.board_inside_compu:
			print " ".join(row)

	def my_board_outside_compu(self):
		#self.clean_screen()
		print """
		 _____               _    _____                   
		| __  |___ ___ ___ _| |  |     |___ _____ ___ _ _ 
		| __ -| . | .'|  _| . |  |   --| . |     | . | | |
		|_____|___|__,|_| |___|  |_____|___|_|_|_|  _|___|
		                                         |_|      
		"""
		#print "BOARD OUTSIDE COMPU\n"
		for row in self.board_outside_compu:
			print " ".join(row)

	def menu(self):
		while True:
			self.clean_screen()
			self.instructions()
			self.menu_print()
			menu_ask_option = self.menu_ask_option()
			menu_perform_action = self.menu_perform_action(menu_ask_option)

	def instructions(self):
		print """
		Select if you want to choose:\n
		Single Player
		Multi Player
		Exit\n
		In Single Player the ships of the computer are placed automatically then you have to
		place your ships on your board.
		Then you have to try to guess all the parts of the ship to sink it and the computer has
		to try to sink your boards too\n
		In Multi Player both players have to put their ships on their board and then they have
		to try to sink the ships of the opponent
		"""

	def menu_print(self):
		print """
		 _____ _____ _____ _____ 
		|     |   __|   | |  |  |
		| | | |   __| | | |  |  |
		|_|_|_|_____|_|___|_____|
		"""
		print "1.ONE PLAYER"
		print "2.TWO PLAYERS"
		print "3.EXIT"

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

	def single_player(self):
		self.create_boards_compu()
		self.create_boards_player1()
		self.put_ships("random", self.board_inside_compu, self.my_board_inside_compu, self.my_board_outside_compu, "COMPU")
		self.clean_screen()
		self.my_board_outside_player1()
		#print ""
		self.put_ships("no random", self.board_inside_player1, self.my_board_inside_player1, self.my_board_outside_player1, "PLAYER 1")
		game = True
		while game == True:
			self.clean_screen()
			self.my_board_outside_player1()
			print ""
			#self.my_board_inside_compu()
			#print ""
			self.my_board_outside_compu()
			self.turn_player_one(self.board_inside_compu, self.board_outside_compu, self.my_board_outside_player1, self.my_board_inside_compu, self.my_board_outside_compu, "PLAYER 1", "no random")
			game = self.win_or_no(self.board_inside_compu, self.board_outside_compu)
			if game == True:
				self.clean_screen()
				'''self.my_board_inside_player1()
				print ""
				self.my_board_outside_player1()'''
				self.turn_computer_player(self.board_inside_player1, self.board_outside_player1, self.my_board_outside_compu, self.my_board_inside_player1, self.my_board_outside_player1, "COMPU", "random")
				game = self.win_or_no(self.board_inside_player1, self.board_outside_player1)
		self.create_boards_compu()
		self.create_boards_player1()

	def multi_player(self):
		self.create_boards_player1()
		self.create_boards_player2()
		self.clean_screen()
		self.my_board_outside_player1()
		#print ""
		self.put_ships("no random", self.board_inside_player1, self.my_board_inside_player1, self.my_board_outside_player1, "PLAYER 1")
		self.clean_screen()
		self.my_board_outside_player2()
		self.put_ships("no random", self.board_inside_player2, self.my_board_inside_player2, self.my_board_outside_player2, "PLAYER 2")
		game = True
		while game == True:
			self.clean_screen()
			self.my_board_outside_player1()
			print ""
			#self.my_board_inside_player2()
			#print ""
			self.my_board_outside_player2()
			self.turn_player_one(self.board_inside_player2, self.board_outside_player2, self.my_board_outside_player1, self.my_board_inside_player2, self.my_board_outside_player2, "PLAYER 1", "no random")
			game = self.win_or_no(self.board_inside_player2, self.board_outside_player2)
			if game == True:
				self.clean_screen()
				self.my_board_outside_player2()
				print ""
				#self.my_board_inside_player1()
				#print ""
				self.my_board_outside_player1()
				self.turn_player_two(self.board_inside_player1, self.board_outside_player1, self.my_board_outside_player2, self.my_board_inside_player1, self.my_board_outside_player1, "PLAYER 2", "no random")
				game = self.win_or_no(self.board_inside_player1, self.board_outside_player1)
		self.create_boards_player1()
		self.create_boards_player2()


	def put_ships(self, condition, inside_list, inside_function, outside_function, player):
		self.put_ships_four_pieces(condition, inside_list, inside_function, outside_function, player)
		self.put_ships_three_pieces(condition, inside_list, inside_function, outside_function, player)
		self.put_ships_two_pieces(condition, inside_list, inside_function, outside_function, player)
		self.put_ships_one_pieces(condition, inside_list, inside_function, outside_function, player)

	def vertical_or_horizontal(self, condition):
		if condition == "no random":
			vertical_or_horizontal = self.ask_vertical_or_horizontal()
		elif condition == "random":
			vertical_or_horizontal = self.random_vertical_or_horizontal()
		return vertical_or_horizontal

	def ask_vertical_or_horizontal(self):
		vertical_or_horizontal = ""
		print ""
		while vertical_or_horizontal != "v" and vertical_or_horizontal != "h" and vertical_or_horizontal != "V" and vertical_or_horizontal != "H":
			vertical_or_horizontal = raw_input("Vertical or horizontal v/h: ")
		return vertical_or_horizontal

	def random_vertical_or_horizontal(self):
		vertical_horizontal_random = random.randint(1, 2)
		if vertical_horizontal_random == 1:
			return "v"
		elif vertical_horizontal_random == 2:
			return "h"

	def put_ships_four_pieces(self, condition, inside_list, inside_function, outside_function, player):
		for x in xrange(1,2):
			self.decide_print_player(condition, player, "four")
			vertical_or_horizontal = self.vertical_or_horizontal(condition)
			if vertical_or_horizontal == "h":
				self.ship_four_horizontal(condition, inside_list, inside_function, outside_function, player)
			elif vertical_or_horizontal == "v":
				self.ship_four_vertical(condition, inside_list, inside_function, outside_function, player)

	def put_ships_three_pieces(self, condition, inside_list, inside_function, outside_function, player):
		for x in xrange(1,2):
			self.decide_print_player(condition, player, "three")
			vertical_or_horizontal = self.vertical_or_horizontal(condition)
			if vertical_or_horizontal == "h":
				self.ship_three_horizontal(condition, inside_list, inside_function, outside_function, player)
			elif vertical_or_horizontal == "v":
				self.ship_three_vertical(condition, inside_list, inside_function, outside_function, player)

	def put_ships_two_pieces(self, condition, inside_list, inside_function, outside_function, player):
		for x in xrange(1,3):
			self.decide_print_player(condition, player, "two")
			vertical_or_horizontal = self.vertical_or_horizontal(condition)
			if vertical_or_horizontal == "h":
				self.ship_two_horizontal(condition, inside_list, inside_function, outside_function, player)
			elif vertical_or_horizontal == "v":
				self.ship_two_vertical(condition, inside_list, inside_function, outside_function, player)

	def put_ships_one_pieces(self, condition, inside_list, inside_function, outside_function, player):
		for x in xrange(1,3):
			self.decide_print_player(condition, player, "one")
			self.ship_one_both(condition, inside_list, inside_function, outside_function, player)

	def decide_print_player(self, condition, player, pieces):
		if condition == "no random":
			print "\n%s" % player
			print "Ship of %s pieces" % pieces

	def ship_four_horizontal(self, condition, inside_list, inside_function, outside_function, player):
		column, row = self.column_and_row(condition, 12, 15)
		try:
			if (column < 12 and row < 15)\
				and (("S" in inside_list[row - 1][column + 3] or "S" in inside_list[row - 1][column + 2] or "S" in inside_list[row - 1][column + 1] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2])\
				or ("S" in inside_list[row - 2][column + 3] or "S" in inside_list[row - 2][column + 2] or "S" in inside_list[row - 2][column + 1] or "S" in inside_list[row - 2][column] or "S" in inside_list[row - 2][column - 1] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row][column + 3] or "S" in inside_list[row][column + 2] or "S" in inside_list[row][column + 1] or "S" in inside_list[row][column] or "S" in inside_list[row][column - 1] or "S" in inside_list[row][column - 2])):
				self.decide_print_message_there_is_ship(condition)
				self.ship_four_horizontal(condition, inside_list, inside_function, outside_function, player)
			elif (column < 12 and row == 15)\
				and (("S" in inside_list[row - 1][column + 3] or "S" in inside_list[row - 1][column + 2] or "S" in inside_list[row - 1][column + 1] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2])\
				or ("S" in inside_list[row - 2][column + 3] or "S" in inside_list[row - 2][column + 2] or "S" in inside_list[row - 2][column + 1] or "S" in inside_list[row - 2][column] or "S" in inside_list[row - 2][column - 1] or "S" in inside_list[row - 2][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_four_horizontal(condition, inside_list, inside_function, outside_function, player)
			elif (column == 12 and row < 15)\
				and (("S" in inside_list[row - 1][column + 2] or "S" in inside_list[row - 1][column + 1] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2])\
				or ("S" in inside_list[row - 2][column + 2] or "S" in inside_list[row - 2][column + 1] or "S" in inside_list[row - 2][column] or "S" in inside_list[row - 2][column - 1] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row][column + 2] or "S" in inside_list[row][column + 1] or "S" in inside_list[row][column] or "S" in inside_list[row][column - 1] or "S" in inside_list[row][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_four_horizontal(condition, inside_list, inside_function, outside_function, player)
			elif (column == 12 and row == 15)\
				and (("S" in inside_list[row - 1][column + 2] or "S" in inside_list[row - 1][column + 1] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2])\
				or ("S" in inside_list[row - 2][column + 2] or "S" in inside_list[row - 2][column + 1] or "S" in inside_list[row - 2][column] or "S" in inside_list[row - 2][column - 1] or "S" in inside_list[row - 2][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_four_horizontal(condition, inside_list, inside_function, outside_function, player)
			else:
				self.clean_screen()
				inside_list[row -1][column - 1] = "S"
				for x in xrange(1,4):
					column += 1
					inside_list[row -1][column - 1] = "S"
				self.decide_if_print_board(condition, inside_function)
		except IndexError:
			self.decide_print_mess_out_board(condition)
			self.ship_four_horizontal(condition, inside_list, inside_function, outside_function, player)

	def ship_four_vertical(self, condition, inside_list, inside_function, outside_function, player):
		column, row = self.column_and_row(condition, 15, 12)
		try:
			if (row < 12 and column < 15)\
				and ("S" in inside_list[row + 3][column - 1] or "S" in inside_list[row + 2][column - 1] or "S" in inside_list[row + 1][column - 1] or "S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1]\
				or ("S" in inside_list[row + 3][column - 2] or "S" in inside_list[row + 2][column - 2] or "S" in inside_list[row + 1][column - 2] or "S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row + 3][column] or "S" in inside_list[row + 2][column] or "S" in inside_list[row + 1][column] or "S" in inside_list[row][column] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 2][column])):
				self.decide_print_message_there_is_ship(condition)
				self.ship_four_vertical(condition, inside_list, inside_function, outside_function, player)
			elif (row < 12 and column == 15)\
				and (("S" in inside_list[row + 3][column - 1] or "S" in inside_list[row + 2][column - 1] or "S" in inside_list[row + 1][column - 1] or "S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1])\
				or ("S" in inside_list[row + 3][column - 2] or "S" in inside_list[row + 2][column - 2] or "S" in inside_list[row + 1][column - 2] or "S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_four_vertical(condition, inside_list, inside_function, outside_function, player)
			elif (row == 12 and column < 15)\
				and (("S" in inside_list[row + 2][column - 1] or "S" in inside_list[row + 1][column - 1] or "S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1])\
				or ("S" in inside_list[row + 2][column - 2] or "S" in inside_list[row + 1][column - 2] or "S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row + 2][column] or "S" in inside_list[row + 1][column] or "S" in inside_list[row][column] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 2][column])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_four_vertical(condition, inside_list, inside_function, outside_function, player)
			elif (row == 12 and column == 15)\
				and (("S" in inside_list[row + 2][column - 1] or "S" in inside_list[row + 1][column - 1] or "S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1])\
				or ("S" in inside_list[row + 2][column - 2] or "S" in inside_list[row + 1][column - 2] or "S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_four_vertical(condition, inside_list, inside_function, outside_function, player)
			else:
				self.clean_screen()
				inside_list[row - 1][column - 1] = "S"
				for x in xrange(1,4):
					row += 1
					inside_list[row - 1][column - 1] = "S"
				self.decide_if_print_board(condition, inside_function)
		except IndexError:
			self.decide_print_mess_out_board(condition)
			self.ship_four_vertical(condition, inside_list, inside_function, outside_function, player)

	def ship_three_horizontal(self, condition, inside_list, inside_function, outside_function, player):
		column, row = self.column_and_row(condition, 13, 15)
		try:
			if (column < 13 and row < 15)\
				and (("S" in inside_list[row - 1][column + 2] or "S" in inside_list[row - 1][column + 1] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2])\
				or ("S" in inside_list[row - 2][column + 2] or "S" in inside_list[row - 2][column + 1] or "S" in inside_list[row - 2][column] or "S" in inside_list[row - 2][column - 1] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row][column + 2] or "S" in inside_list[row][column + 1] or "S" in inside_list[row][column] or "S" in inside_list[row][column - 1] or "S" in inside_list[row][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_three_horizontal(condition, inside_list, inside_function, outside_function, player)
			elif (column < 13 and row == 15)\
				and (("S" in inside_list[row - 1][column + 2] or "S" in inside_list[row - 1][column + 1] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2])\
				or ("S" in inside_list[row - 2][column + 2] or "S" in inside_list[row - 2][column + 1] or "S" in inside_list[row - 2][column] or "S" in inside_list[row - 2][column - 1] or "S" in inside_list[row - 2][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_three_horizontal(condition, inside_list, inside_function, outside_function, player)
			elif (column == 13 and row < 15)\
				and (("S" in inside_list[row - 1][column + 1] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2])\
				or ("S" in inside_list[row - 2][column + 1] or "S" in inside_list[row - 2][column] or "S" in inside_list[row - 2][column - 1] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row][column + 1] or "S" in inside_list[row][column] or "S" in inside_list[row][column - 1] or "S" in inside_list[row][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_three_horizontal(condition, inside_list, inside_function, outside_function, player)
			elif (column == 13 and row == 15)\
				and (("S" in inside_list[row - 1][column + 1] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2])\
				or ("S" in inside_list[row - 2][column + 1] or "S" in inside_list[row - 2][column] or "S" in inside_list[row - 2][column - 1] or "S" in inside_list[row - 2][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_three_horizontal(condition, inside_list, inside_function, outside_function, player)
			else:
				self.clean_screen()
				inside_list[row - 1][column - 1] = "S"
				for x in xrange(1,3):
					column += 1
					inside_list[row - 1][column - 1] = "S"
				self.decide_if_print_board(condition, inside_function)
		except IndexError:
			self.decide_print_mess_out_board(condition)
			self.ship_three_horizontal(condition, inside_list, inside_function, outside_function, player)

	def ship_three_vertical(self, condition, inside_list, inside_function, outside_function, player):
		column, row = self.column_and_row(condition, 15, 13)
		try:
			if (row < 13 and column < 15)\
				and ("S" in inside_list[row + 2][column - 1] or "S" in inside_list[row + 1][column - 1] or "S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1]\
				or ("S" in inside_list[row + 2][column - 2] or "S" in inside_list[row + 1][column - 2] or "S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row + 2][column] or "S" in inside_list[row + 1][column] or "S" in inside_list[row][column] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 2][column])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_three_vertical(condition, inside_list, inside_function, outside_function, player)
			elif (row < 13 and column == 15)\
				and (("S" in inside_list[row + 2][column - 1] or "S" in inside_list[row + 1][column - 1] or "S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1])\
				or ("S" in inside_list[row + 2][column - 2] or "S" in inside_list[row + 1][column - 2] or "S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_three_vertical(condition, inside_list, inside_function, outside_function, player)
			elif (row == 13 and column < 15)\
				and (("S" in inside_list[row + 1][column - 1] or "S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1])\
				or ("S" in inside_list[row + 1][column - 2] or "S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row + 1][column] or "S" in inside_list[row][column] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 2][column])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_three_vertical(condition, inside_list, inside_function, outside_function, player)
			elif (row == 13 and column == 15)\
				and (("S" in inside_list[row + 1][column - 1] or "S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1])\
				or ("S" in inside_list[row + 1][column - 2] or "S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_three_vertical(condition, inside_list, inside_function, outside_function, player)
			else:
				self.clean_screen()
				inside_list[row - 1][column - 1] = "S"
				for x in xrange(1,3):
					row += 1
					inside_list[row - 1][column - 1] = "S"
				self.decide_if_print_board(condition, inside_function)
		except IndexError:
			self.decide_print_mess_out_board(condition)
			self.ship_three_vertical(condition, inside_list, inside_function, outside_function, player)

	def ship_two_horizontal(self, condition, inside_list, inside_function, outside_function, player):
		column, row = self.column_and_row(condition, 14, 15)
		try:
			if (column < 14 and row < 15)\
				and (("S" in inside_list[row - 1][column + 1] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2])\
				or ("S" in inside_list[row - 2][column + 1] or "S" in inside_list[row - 2][column] or "S" in inside_list[row - 2][column - 1] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row][column + 1] or "S" in inside_list[row][column] or "S" in inside_list[row][column - 1] or "S" in inside_list[row][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_two_horizontal(condition, inside_list, inside_function, outside_function, player)
			elif (column < 14 and row == 15)\
				and (("S" in inside_list[row - 1][column + 1] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2])\
				or ("S" in inside_list[row - 2][column + 1] or "S" in inside_list[row - 2][column] or "S" in inside_list[row - 2][column - 1] or "S" in inside_list[row - 2][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_two_horizontal(condition, inside_list, inside_function, outside_function, player)
			elif (column == 14 and row < 15)\
				and (("S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2])\
				or ("S" in inside_list[row - 2][column] or "S" in inside_list[row - 2][column - 1] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row][column] or "S" in inside_list[row][column - 1] or "S" in inside_list[row][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_two_horizontal(condition, inside_list, inside_function, outside_function, player)
			elif (column == 14 and row == 15)\
				and (("S" in inside_list[row - 1][column] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 1][column - 2])\
				or ("S" in inside_list[row - 2][column] or "S" in inside_list[row - 2][column - 1] or "S" in inside_list[row - 2][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_two_horizontal(condition, inside_list, inside_function, outside_function, player)
			else:
				self.clean_screen()
				inside_list[row - 1][column - 1] = "S"
				for x in xrange(1,2):
					column += 1
					inside_list[row - 1][column - 1] = "S"
				self.decide_if_print_board(condition, inside_function)
		except IndexError:
			self.decide_print_mess_out_board(condition)
			self.ship_two_horizontal(condition, inside_list, inside_function, outside_function, player)

	def ship_two_vertical(self, condition, inside_list, inside_function, outside_function, player):
		column, row = self.column_and_row(condition, 15, 14)
		try:
			if (row < 14 and column < 15)\
				and ("S" in inside_list[row + 1][column - 1] or "S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1]\
				or ("S" in inside_list[row + 1][column - 2] or "S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row + 1][column] or "S" in inside_list[row][column] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 2][column])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_two_vertical(condition, inside_list, inside_function, outside_function, player)
			elif (row < 14 and column == 15)\
				and (("S" in inside_list[row + 1][column - 1] or "S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1])\
				or ("S" in inside_list[row + 1][column - 2] or "S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_two_vertical(condition, inside_list, inside_function, outside_function, player)
			elif (row == 14 and column < 15)\
				and (("S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1])\
				or ("S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row][column] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 2][column])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_two_vertical(condition, inside_list, inside_function, outside_function, player)
			elif (row == 14 and column == 15)\
				and (("S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1])\
				or ("S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_two_vertical(condition, inside_list, inside_function, outside_function, player)
			else:
				self.clean_screen()
				inside_list[row - 1][column - 1] = "S"
				for x in xrange(1,2):
					row += 1
					inside_list[row - 1][column - 1] = "S"
				self.decide_if_print_board(condition, inside_function)
		except IndexError:
			self.decide_print_mess_out_board(condition)
			self.ship_two_vertical(condition, inside_list, inside_function, outside_function, player)

	def ship_one_both(self, condition, inside_list, inside_function, outside_function, player):
		column, row = self.column_and_row(condition, 15, 15)
		try:
			if (row < 15 and column < 15)\
				and ("S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1]\
				or ("S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row][column] or "S" in inside_list[row - 1][column] or "S" in inside_list[row - 2][column])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_one_both(condition, inside_list, inside_function, outside_function, player)
			elif (row < 15 and column == 15)\
				and (("S" in inside_list[row][column - 1] or "S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1])\
				or ("S" in inside_list[row][column - 2] or "S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_one_both(condition, inside_list, inside_function, outside_function, player)
			elif (row == 15 and column < 15)\
				and (("S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1])\
				or ("S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])\
				or ("S" in inside_list[row - 1][column] or "S" in inside_list[row - 2][column])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_one_both(condition, inside_list, inside_function, outside_function, player)
			elif (row == 15 and column == 15)\
				and (("S" in inside_list[row - 1][column - 1] or "S" in inside_list[row - 2][column - 1])\
				or ("S" in inside_list[row - 1][column - 2] or "S" in inside_list[row - 2][column - 2])):
					self.decide_print_message_there_is_ship(condition)
					self.ship_one_both(condition, inside_list, inside_function, outside_function, player)
			else:
				self.clean_screen()
				inside_list[row - 1][column - 1] = "S"
				self.decide_if_print_board(condition, inside_function)
		except IndexError:
			self.decide_print_mess_out_board(condition)
			self.ship_one_both(condition, inside_list, inside_function, outside_function, player)

	def decide_if_print_board(self, condition, inside_function):
		if condition == "no random":
			inside_function()

	def decide_print_message_there_is_ship(self, condition):
		if condition == "no random":
			message = raw_input("Already there is a ship near or in this position")

	def decide_print_mess_out_board(self, condition):
		if condition == "no random":
			message = raw_input("Out of range")

	def column_and_row(self, condition, *end_range):
		column = 0
		row = 0
		while (column < 1 or column > end_range[0]) or (row < 1 or row > end_range[1]):
			column = self.column(condition, end_range)
			row = self.row(condition, end_range)
			self.decide_if_print_message(condition, end_range, column, row)
		return column, row

	def column(self, condition, end_range):
		if condition == "random":
			column = random.randint(1, end_range[0])
		elif condition == "no random":
			column = self.ask_column_position()
		return column

	def ask_column_position(self):
		column_position = 0
		while column_position < 1 or column_position > 15:
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
			row = random.randint(1, end_range[0])
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

	def decide_if_print_message(self, condition, end_range, column, row):
		if condition == "no random" and ((column < 1 or column > end_range[0]) or (row < 0 or row > end_range[1])):
			message = raw_input("Enter a number between 1 and the number that make to fit the ship on the board")

	def turn_player_one(self, inside_list, outside_list, outside_function_opponent, inside_function, outside_function, player, condition):
		print "\n%s" % player
		guess_column, guess_row = self.guess_column_and_row(outside_list, condition)
		self.verify_shot(False, guess_column, guess_row, inside_list, outside_list, outside_function_opponent, inside_function, outside_function, player)

	def turn_player_two(self, inside_list, outside_list, outside_function_opponent, inside_function, outside_function, player, condition):
		print "\n%s" % player
		guess_column, guess_row = self.guess_column_and_row(outside_list, condition)
		self.verify_shot(False, guess_column, guess_row, inside_list, outside_list, outside_function_opponent, inside_function, outside_function, player)

	def turn_computer_player(self, inside_list, outside_list, outside_function_opponent, inside_function, outside_function, player, condition):
		random_column, random_row = self.random_column_and_row(outside_list, condition)
		self.verify_shot(True, random_column, random_row, inside_list, outside_list, outside_function_opponent, inside_function, outside_function, player)

	def guess_column_and_row(self, outside_list, condition):
		repeted = True
		while repeted == True:
			guess_column = 0
			guess_row = 0
			while (guess_column < 1 or guess_column > 15) or (guess_row < 1 or guess_row > 15):
				guess_column = self.guess_column()
				guess_row = self.guess_row()
				self.decide_print_message_out_range(guess_column, guess_row)
			repeted = self.repeted(outside_list, guess_column, guess_row, condition)
		self.clean_screen()
		return guess_column, guess_row

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
		try:
			guess_column = int(guess_column)
		except ValueError:
			pass
		return guess_column

	def guess_row_int(self, guess_row):
		try:
			guess_row = int(guess_row)
		except ValueError:
			pass
		return guess_row

	def decide_print_message_out_range(self, guess_column, guess_row):
		if (guess_column < 1 or guess_column > 15) or (guess_row < 1 or guess_row > 15):
			message = raw_input("Enter a number between 1 and 15")

	def repeted(self, outside_list, column, row, condition):
		if ("O" in outside_list[row - 1][column - 1]):
			repeted = False
		else:
			repeted = True
			self.print_if_there_is_a_ship_in_position(condition)
		return repeted

	def print_if_there_is_a_ship_in_position(self, condition):
		if condition == "no random":
			print "Shot in a position where you have not shot"

	def random_column_and_row(self, outside_list, condition):
		repeted = True
		while repeted == True:
			random_column = self.random_column()
			random_row = self.random_row()
			repeted = self.repeted(outside_list, random_row, random_row, condition)
		return random_column, random_row

	def random_column(self):
		return random.randint(1, len(self.board_inside_compu[0]))

	def random_row(self):
		return random.randint(1, len(self.board_inside_compu[0]))

	def verify_shot(self,true_or_false, column, row, inside_list, outside_list, outside_function_opponent, inside_function, outside_function, player):
		if column <= 0 or column > len(inside_list[0]) or row <= 0 or row > len(inside_list[0]):
			print "\nThis is outside of the board\n"
		else:
			if inside_list[row - 1][column - 1] == "S":
				outside_list[row - 1][column - 1] = "S"
				outside_function_opponent()
				print ""
				#inside_function()
				#print ""
				outside_function()
				#print "\n%s" % player
				self.decide_print_coordenates(true_or_false, player, column, row)
				message = ("\n%s guessed a part of the ship") % player
				message = raw_input(message)
			else:
				outside_list[row -1][column - 1] = "X"
				outside_function_opponent()
				print ""
				#inside_function()
				#print ""
				outside_function()
				#print "\n%s" % player
				self.decide_print_coordenates(true_or_false, player, column, row)
				message = ("\n%s didn't guess any part of a ship") %player
				message =  raw_input(message)

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

	def clean_screen(self):
		if self.operative_system == "Linux":
			os.system('reset')
		elif self.operative_system == "Windows":
			os.system('cls')

	def exit_program(self):
			self.clean_screen()
			sys.exit()

user1 = my_game()
user1.menu()
