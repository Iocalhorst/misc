import pygame
import random

RED=(255,0,0)
BLUE=(0,255,0)
GREEN=(0,0,255)

def main():
	pygame.init()
	window_width=640
	window_height=480
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((window_width,window_height))
	blocksize=20
	while True:
		clock.tick(50)
		color=random.choice((RED,BLUE,GREEN))
		position_x=random.randint(0,10)
		position_y=random.randint(0,20)

		pygame.draw.rect(screen,color, (position_x*blocksize,position_y*blocksize,blocksize,blocksize))
		pygame.display.update()



main()