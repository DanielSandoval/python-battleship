# Aqui escribe tu codigo

import os
import sys
import random
#import pygame

class my_game(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.board_inside = []
		self.board_outside = []
		self.ship_4_horizontal = []
		self.ship_4_vertical = []
		self.menu_option = {1:self.one_player, 3:self.exit_program}
		for x in xrange(1,16):
			self.board_inside.append(["O"] * 15)
		for x in xrange(1,16):
			self.board_outside.append(["O"] * 15)

	def my_board_inside(self):
		for row in self.board_inside:
			print " ".join(row)

	def my_board_outside(self):
		for row in self.board_outside:
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

	def one_player(self):
		os.system('reset')
		self.my_board_inside()
		print ""
		self.put_ships_random()
		#if :
			#pass
		self.player_one()
		'''game = "Continue"
		while game == "Continue":
			guess_column = self.guess_column()
			guess_row = self.guess_row()'''
			#self.verify_shot(random_column, random_row, guess_column, guess_row)

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
		print self.ship_4_horizontal
		print self.ship_4_vertical
		self.my_board_inside()
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

	def put_ships_one_pieces(self):
		for x in xrange(1,6):
			self.ship_one_both()

	def ship_four_horizontal(self):
		random_column = random.randint(1,12)
		random_row = self.random_row()
		#print random_column
		#print random_row
		try:
			if (random_column < 12 and ("S" in self.board_inside[random_row - 1][random_column + 3] or "S" in self.board_inside[random_row - 1][random_column + 2] or "S" in self.board_inside[random_row - 1][random_column + 1] or "S" in self.board_inside[random_row - 1][random_column] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 2]))\
				or (random_column == 12 and ("S" in self.board_inside[random_row - 1][random_column] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 2])):
				#message = raw_input("Already there is a ship in this position")
				self.ship_four_horizontal()
			else:
				self.board_inside[random_row -1][random_column - 1] = "S"
				#self.ship_4_horizontal[random_row].append(random_column) #Add INVERTED coordinates to a dictionary
				for x in xrange(1,4):
					random_column += 1
					self.board_inside[random_row -1][random_column - 1] = "S"
					self.ship_4_horizontal 
					#self.ship_4_horizontal[random_row].append(random_column) #Add INVERTED coordinates to a dictionary
				#print self.ship_4_horizontal
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
			if (random_row < 12 and ("S" in self.board_inside[random_row + 3][random_column - 1] or "S" in self.board_inside[random_row + 2][random_column - 1] or "S" in self.board_inside[random_row + 1][random_column - 1] or "S" in self.board_inside[random_row][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 2][random_column - 1]))\
				or (random_row == 12 and ("S" in self.board_inside[random_row][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 2][random_column - 1])):
				#message = raw_input("Already there is a ship in this position")
				self.ship_four_vertical()
			else:
				self.board_inside[random_row - 1][random_column - 1] = "S"
				#self.ship_4_vertical[random_row] = random_column #Add coordinates to a dictionary
				for x in xrange(1,4):
					random_row += 1
					self.board_inside[random_row - 1][random_column - 1] = "S"
					#self.ship_4_vertical[random_row] = random_column #Add coordinates to a dictionary
				#print self.ship_4_vertical
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
			if (random_column < 13 and ("S" in self.board_inside[random_row - 1][random_column + 2] or "S" in self.board_inside[random_row - 1][random_column + 1] or "S" in self.board_inside[random_row - 1][random_column] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 2]))\
				or (random_column == 13 and ("S" in self.board_inside[random_row - 1][random_column] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 2])):
				#message = raw_input("Already there is a ship in this position")
				self.ship_three_horizontal()
			else:
				self.board_inside[random_row - 1][random_column - 1] = "S"
				for x in xrange(1,3):
					random_column += 1
					self.board_inside[random_row - 1][random_column - 1] = "S"
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
			if (random_row < 13 and ("S" in self.board_inside[random_row + 2][random_column - 1] or "S" in self.board_inside[random_row + 1][random_column - 1] or "S" in self.board_inside[random_row][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 2][random_column - 1]))\
				or (random_row == 13 and ("S" in self.board_inside[random_row][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 2][random_column - 1])):
				#message = raw_input("Already there is a ship in this position")
				self.ship_three_vertical()
			else:
				self.board_inside[random_row - 1][random_column - 1] = "S"
				for x in xrange(1,3):
					random_row += 1
					self.board_inside[random_row - 1][random_column - 1] = "S"
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
			if (random_column < 14 and ("S" in self.board_inside[random_row - 1][random_column + 1] or "S" in self.board_inside[random_row - 1][random_column] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 2]))\
				or (random_column == 14 and ("S" in self.board_inside[random_row - 1][random_column] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 2])):
				#message = raw_input("Already there is a ship in this position")
				self.ship_two_horizontal()
			else:
				self.board_inside[random_row - 1][random_column - 1] = "S"
				for x in xrange(1,2):
					random_column += 1
					self.board_inside[random_row - 1][random_column - 1] = "S"
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
			if (random_row < 14 and ("S" in self.board_inside[random_row + 1][random_column - 1] or "S" in self.board_inside[random_row][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 2][random_column - 1]))\
				or (random_row == 14 and ("S" in self.board_inside[random_row][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 2][random_column - 1])):
				#message = raw_input("Already there is a ship in this position")
				self.ship_two_vertical()
			else:
				self.board_inside[random_row - 1][random_column - 1] = "S"
				for x in xrange(1,2):
					random_row += 1
					self.board_inside[random_row - 1][random_column - 1] = "S"
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_two_vertical()
		#message = raw_input("Final ship for one")

	def ship_one_both(self):
		random_column = random.randint(1,15)
		random_row = self.random_row()
		#print random_column
		#print random_row
		try:
			if (random_column < 15 and ("S" in self.board_inside[random_row - 1][random_column + 1] or "S" in self.board_inside[random_row - 1][random_column] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 2]))\
				or (random_column == 15 and ("S" in self.board_inside[random_row - 1][random_column] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 2]))\
				or ("S" in self.board_inside[random_row + 1][random_column - 1] or "S" in self.board_inside[random_row][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 2][random_column - 1])\
				or ("S" in self.board_inside[random_row][random_column - 1] or "S" in self.board_inside[random_row - 1][random_column - 1] or "S" in self.board_inside[random_row - 2][random_column - 1]):
				#message = raw_input("Already there is a ship in this position")
				self.ship_one_both()
			else:
				self.board_inside[random_row - 1][random_column - 1] = "S"
		except IndexError:
			#message = raw_input("Out of the board")
			self.ship_one_both()
		#message = raw_input("Final ship for one")

	def random_column(self):
		return random.randint(1, len(self.board_inside[0]))

	def random_row(self):
		return random.randint(1, len(self.board_inside[0]))

	#def game_single_player(self):

	def player_one(self):
		game_over = False
		while game_over == False:
			guess_column = self.guess_column()
			guess_row = self.guess_row()
			self.verify_shot(guess_column, guess_row)
			game_over = self.continue_or_game_over()
			#times_in_board_inside, times_in_board_outside = self.compare_boards()
			#self.continue_or_game_over()

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

	def verify_shot(self, guess_column, guess_row):
		if guess_column <= 0 or guess_column > len(self.board_inside[0]) or guess_row <= 0 or guess_row > len(self.board_inside[0]):
			print "\nThis is outside of the board\n"
		else:
			if self.board_inside[guess_row - 1][guess_column - 1] == "S":
				print "\nYou guessed a part of the ship\n"
				self.board_outside[guess_row - 1][guess_column - 1] = "S"
			else:
				print "\nYou didn't guess any part of a ship\n"
				self.board_outside[guess_row -1][guess_column - 1] = "X"
			self.my_board_inside()
			print ""
			self.my_board_outside()
		#self.continue_or_game_over()
		message = raw_input("PRESS ENTER")

	def compare_boards(self):
		times_in_board_inside = 0
		for row in self.board_inside:
			times_in_board_inside += row.count("S")
		times_in_board_outside = 0
		for row in self.board_outside:
			times_in_board_outside += row.count("S")
		return times_in_board_inside, times_in_board_outside

	def continue_or_game_over(self):
		times_in_board_inside, times_in_board_outside = self.compare_boards()
		if times_in_board_inside == times_in_board_outside:
			game_over = True
		else:
			game_over = False
		return game_over

	def exit_program(self):
		os.system('reset')
		sys.exit()

user1 = my_game()
user1.menu()
