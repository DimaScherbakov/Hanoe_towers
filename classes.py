# -*- coding: utf-8 -*-
from time import sleep
import pygame
from pygame import *
class Construction():
	towers = []
	current_block = 0

	def main_loop(self):
		pygame.init()
		BLACK = (0, 0, 0)
		WHITE = (255, 255, 255)
		BLUE = (0, 0, 255)
		GREEN = (0, 255, 0)
		RED = (255, 0, 0)
		PI = 3.141592653
		size = (1080, 480)
		screen = pygame.display.set_mode(size)
		clock = pygame.time.Clock()
		done = True
		while done:
			# a = raw_input("Добро пожаловать в игру ")
			# sleep(1)
			# print a
			for event in pygame.event.get():  # User did something
				if event.type == pygame.QUIT:  # If user clicked close
					done = False
			screen.fill(WHITE)
			pygame.draw.line(screen, BLACK, [0,400], [1080, 400], 10)
			pygame.draw.line(screen, RED, [220,400], [220, 100], 3)
			pygame.draw.line(screen, RED, [560,400], [560, 100], 3)
			pygame.draw.line(screen, RED, [900,400], [900, 100], 3)
			pygame.display.flip()
			clock.tick(60)

	def __init__(self,count_of_blocks_init):
		for x in range(0,3):
			self.towers.append(Tower())
		for created_block in range(0,count_of_blocks_init):
			self.towers[0].current_blocks.append(Block(created_block+1))
		self.towers[0].current_blocks.reverse()
		self.main_loop()




class Tower():
	current_blocks = []
	count_of_blocks = len(current_blocks)

	def get_block(self,from_tower):
		Construction.current_block = self.current_blocks.pop()
	def put_block(self, to_tower):
		pass



class Block():
	size = 0
#длинна самого большого блока не может привышать 180 едениц
	def __init__(self,size):
		self.size = size
