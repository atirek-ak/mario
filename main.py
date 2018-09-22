from random import *
import sys, tty
import os
from time import *
import termios
import threading
from Gameplay import *
from Entity import *
from Board import *
import NonBlockingInput as keyboard

char=""
kb = keyboard.KBHit()

class Game():

	def _init_(self):
		pass


	def initialise(self,lev):
		#Initialize 
		level = int(lev)
		board = GameBoard()
		mario = Player(2,24,0,0,0,0,0)
		colours = bcolors()

		#Level Setup
		gameLength = 0
		nEnemies = 0
		nPipes = 0
		nStrips = 0
		nPits = 0
		startFrame = 0
		timeout = 0
		gameSpeed = 0
		clouds = 0
		coins = 0
		springs = 0
		if( level == 1 ):
			gameLength = 300
			nEnemies = 23
			nPipes = 20
			nStrips = 21
			timeout = 0.07
			gameSpeed = 1
			nPits = 18
			clouds = 20
			mario.lives = 5
			coins = 100
			springs = 1
		elif( level == 2):
			gameLength = 700
			nEnemies = 40
			nPipes = 39
			nStrips = 40
			timeout = 0.07
			gameSpeed = 0.6
			nPits = 40	
			mario.lives = 4
			clouds = 40
			coins = 240
			springs = 10
		elif( level == 3 ):	
			gameLength = 1300
			nEnemies = 50
			nPipes = 50
			nStrips = 53
			timeout = 0.07
			gameSpeed = 0.6
			nPits = 65
			springs = 18
			mario.lives = 3
			clouds = 47
			coins = 400
		elif( level == 4 ):	
			gameLength = 2000
			nEnemies = 70
			nPipes = 72
			nStrips = 74
			timeout = 0.07
			gameSpeed = 0.6
			nPits = 75
			mario.lives = 2
			clouds = 90
			coins = 700
			springs = 25

		#GenerateMap
		gameplane = [[ ' ' for x in range(gameLength) ] for y in range(28) ]
		for i in range(gameLength ):
			gameplane[26][i] = colours.BROWN + '#' + bcolors.ENDC
			gameplane[27][i] = colours.BROWN + '#' + bcolors.ENDC
				

		#Place Mario
		gameplane[24][2] = colours.RED  + '0' +  bcolors.ENDC
		gameplane[24][3] = colours.RED +'0' +  bcolors.ENDC
		gameplane[25][2] = colours.CYAN + '/' +  bcolors.ENDC
		gameplane[25][3] = colours.CYAN + '\\' + bcolors.ENDC

		#Generate Random Enemies
		for i in range(nEnemies):
			x = choice(range(10,gameLength - 20,2))
			y = 25
			while gameplane[y][x] != ' ':
				x = choice(range(2,gameLength - 20,2))
			gameplane[y][x]= colours.GREEN + 'R' + bcolors.ENDC
			gameplane[y][x + 1]= colours.GREEN + 'R' + bcolors.ENDC

		#Generate Pipes
		for i in range(nEnemies):
			x = choice(range(10,gameLength - 20,2))
			y = 25
			while gameplane[y][x] != ' ':
				x = choice(range(2,gameLength - 2,2))
			height = choice(range(2,6,2))
			for	i in range(height):
				gameplane[y - i][x] = colours.BROWN + '#' + bcolors.ENDC
				gameplane[y - i][x + 1] = colours.BROWN + '#' + bcolors.ENDC

		#Generate Springs
		for i in range(springs):
			y = 25
			x = choice(range(10,gameLength - 20,2))
			while gameplane[y][x] != ' ':
				x = choice(range(10,gameLength - 20,2))
			gameplane[y][x] = colours.ORANGE + 'T' + bcolors.ENDC

		#Generate Strips
		for i in range(nStrips):
			x = choice(range(10,gameLength - 20,2))
			y = choice([21,17])
			length = choice([2,4,6,8,10,12])
			while 1:
				if gameplane[y][x] == ' ' and gameplane[y][x + length] == ' ':
					break
				else:
					x = choice(range(10,gameLength - 20,2))
					y = choice([21,17])
					length = choice([2,4,6,8,10,12])
			for i in range(length):
				gameplane[y][x + i] = colours.BROWN + '#' + bcolors.ENDC
				gameplane[y + 1][x + i] = colours.BROWN + '#' + bcolors.ENDC
				
									
		#Generate Pits
		for i in range(nPits):
			y = 26
			x = choice(range(10,gameLength - 20,2))
			while gameplane[y - 1][x] != ' ':
				x = choice(range(10,gameLength - 20,2))
			gameplane[y][x] = ' '
			gameplane[y][x + 1] = ' '
			gameplane[y + 1][x] = ' '
			gameplane[y + 1][x + 1] = ' '

		#Generate Clouds
		for i in range(clouds):
			y = 1
			x = choice(range(2,gameLength - 20))
			for j in range(7):
				gameplane[y][x+ 1 + j] = colours.BLUE + '^' + bcolors.ENDC
				gameplane[y + 2][x+ 1 + j] = colours.BLUE + '^' + bcolors.ENDC
			for j in range(9):
				gameplane[y + 1][x + j] = colours.BLUE + '^' + bcolors.ENDC

		#Generate Coins
		for i in range(coins):
			x = choice(range(2,gameLength - 20))
			y = choice(range(1,25))
			while gameplane[y][x] != ' ':
				x = choice(range(2,gameLength - 20))
				y = choice(range(1,25))
			gameplane[y][x] = colours.PURPLE + '*' + bcolors.ENDC

		#Generate Flag
		for i in range(23):
			gameplane[i + 3][gameLength - 11] = '|'
		gameplane[3][gameLength - 12] = '/'
		gameplane[4][gameLength - 13] = '/'
		gameplane[5][gameLength - 13] = '\\'
		gameplane[6][gameLength - 12] = '\\'

		#Gameloop
		self.gameloop(gameplane,startFrame,mario,board,timeout,gameSpeed,gameLength)
				

	def gameloop(self,gameplane,startFrame,mario,board, timeout, gameSpeed, gameLength):
		while mario.lives > 0:
			mario.score += float(level)
			sleep(timeout)

			for i in range(100):
				if gameplane[25][startFrame + i] == colours.YELLOW + 'R' + bcolors.ENDC:
					gameplane[25][startFrame + i] = colours.GREEN + 'R' + bcolors.ENDC

			#Set Frame
			startFrame = mario.x - 50
			if startFrame < 0:
				startFrame = 0
			elif startFrame > gameLength - 100:
				startFrame = gameLength - 100		

			board.printboard(gameplane,startFrame,mario.lives,int(mario.score/100),mario.killed)


			if mario.x > gameLength - 15:
				gameplane[mario.y][mario.x] = ' '
				gameplane[mario.y][mario.x + 1] = ' '
				gameplane[mario.y + 1][mario.x] = ' '
				gameplane[mario.y + 1][mario.x + 1] = ' '
				gaming.endLevel(gameplane,mario,gameLength)

			if gameplane[mario.y + 2][mario.x] == colours.GREEN + 'R' + bcolors.ENDC or gameplane[mario.y + 2][mario.x + 1] == colours.GREEN + 'R' + bcolors.ENDC:
				if mario.jump == 0:
					gaming.enemyKilled(mario,gameplane)


			c = '('
			if kb.kbhit():
				c = kb.getch()
			else:
				c = '('
			if c == 'q':
				gaming.quitgame(int(mario.score/100),mario.killed)
			elif c == 'p':
				gaming.pause(mario)
				board.printboard(gameplane,startFrame,mario.lives,int(mario.score/100),mario.killed)
			elif c == 'a':
				mario.moveLeft(gameplane,gameLength)
			elif c == 'd':
				mario.moveRight(gameplane, gameLength)
			elif c == 'w':
				if gameplane[mario.y + 2][mario.x] == colours.BROWN + '#' + bcolors.ENDC or gameplane[mario.y + 2][mario.x + 1] == colours.BROWN + '#' + bcolors.ENDC:
					os.system("afplay ./Music/jump.wav&")
					mario.jump = 1
					mario.height = mario.y - 10

			if mario.jump == 0:
				mario.down(gameplane)
			else:
				if gameplane[mario.y - 1][mario.x] not in [' ',colours.PURPLE + '*' + bcolors.ENDC] or gameplane[mario.y - 1][mario.x + 1] not in [' ',colours.PURPLE + '*' + bcolors.ENDC]:
					mario.jump = 0
				elif mario.y > mario.height:
					mario.up(gameplane)
				elif mario.y == mario.height:	
					mario.jump = 0

			if mario.y == 25:
				if mario.lives > 1:
					mario.reduceLife(gameplane,gameLength)		
				else:
					mario.lives = 0	
					board.printboard(gameplane,startFrame,mario.lives,int(mario.score/100),mario.killed)
					gaming.quitgame(int(mario.score/100),mario.killed)

			#Enemies movement
			if mario.score % (int(level) * 10) == 0:	
				gaming.automate(mario,gameplane,startFrame,gameLength)	

			if gameplane[mario.y + 2][mario.x] == colours.ORANGE + 'T' + bcolors.ENDC:
				mario.jump = 1
				os.system("afplay ./Music/jump.wav&")
				mario.height = mario.y - 16

					
	def startMenu(self):
			os.system("afplay ./Music/main_theme.wav&")
			print("Welcome to Mario!!")
			print("Controls:")
			print("W = Jump")
			print("A = Move Left")
			print("D = Move Right")
			print("p = Pause/Resume Game")
			print("q = Quit Game")
			print()
			print("Characters:")
			print(colours.RED  + "Mario: 00" +  bcolors.ENDC)
			print(colours.CYAN + "       /\\" +  bcolors.ENDC)
			print(colours.GREEN + "Enemy: RR" + bcolors.ENDC)
			print(colours.BROWN + "Ground, Pipes and Strips: ###" + bcolors.ENDC)
			print(colours.BLUE + 'Clouds:	^^^^' + bcolors.ENDC)
			print(colours.ORANGE + 'Spring:	T' + bcolors.ENDC)
			print(colours.PURPLE + 'Coins: *' + bcolors.ENDC)
			print("Choose level difficulty from 1 to 4")
			c = self.userinput()
			while c not in [ "1" , "2" , "3" , "4" , "q" ]:
				print("Enter Valid Level!!")
				c = self.userinput()
			return c



	def userinput(self):
		old = termios.tcgetattr(sys.stdin)
		tty.setcbreak(sys.stdin.fileno())
		try:
	    		key = sys.stdin.read(1)
		except:
			pass
		return key	


print(char)
obj = Game()
gaming = Gaming()
level = obj.startMenu()
if level == 'q':
	gaming.quitgame(0,0)
obj.initialise(level)		
