from Board import *
import sys, tty
from time import *
import termios
import os
from random import *
colours = bcolors()
board = GameBoard()

class Gaming():
	def __init__(self):
		pass


	def pause(self,mario):
		print("You have paused the game. Press 'p' to restart")
		while(1):
			c = self.userinput()
			if c == 'p':
				break
			elif c == 'q':
				self.quitgame(mario.score,mario.killed)


	def quitgame(self,score,killed):
		os.system('killall aplay')
		os.system('aplay ./Music/death.wav&')
		print()
		print('Game Over!!')
		print('Your Final Score is ' + str(score))
		print('Enemies killed = ' + str(killed))
		quit()		


	def userinput(self):
		old = termios.tcgetattr(sys.stdin)
		tty.setcbreak(sys.stdin.fileno())
		try:
	    		key = sys.stdin.read(1)
		except:
			pass
		return key

	def enemyKilled(self,mario,gameplane):
		mario.killed += 1
		mario.score += 1200
		if gameplane[mario.y + 2][mario.x] == colours.GREEN + 'R' + bcolors.ENDC:
			gameplane[mario.y + 2][mario.x] = ' '
			gameplane[mario.y + 2][mario.x + 1] = ' '

	def automate(self,mario,gameplane,startFrame,gameLength):
		for i in range(0,100,2):
			if gameplane[25][startFrame + i] == colours.GREEN + 'R' + bcolors.ENDC:
				rand = choice(['L','R'])
				if rand == 'L':
					if gameplane[25][startFrame + i - 2] == ' ' and gameplane[26][startFrame + i - 2] == colours.BROWN + '#' + bcolors.ENDC:
						gameplane[25][startFrame + i - 2] = colours.YELLOW + 'R' + bcolors.ENDC
						gameplane[25][startFrame + i - 1] = colours.YELLOW + 'R' + bcolors.ENDC
						gameplane[25][startFrame + i] = ' '
						gameplane[25][startFrame + i + 1] = ' '
					elif gameplane[25][startFrame + i - 1] == colours.CYAN + '\\' + bcolors.ENDC:
						gameplane[25][startFrame + i - 2] = colours.YELLOW + 'R' + bcolors.ENDC
						gameplane[25][startFrame + i - 1] = colours.YELLOW + 'R' + bcolors.ENDC
						gameplane[25][startFrame + i] = ' '
						gameplane[25][startFrame + i + 1] = ' '
						board.printboard(gameplane,startFrame,mario.lives,int(mario.score/100),mario.killed)

						if mario.lives > 1:
							mario.reduceLife(gameplane,gameLength)
						else:
							mario.lives = 0	
							board.printboard(gameplane,startFrame,mario.lives,int(mario.score/100),mario.killed)
							self.quitgame(int(mario.score/100),mario.killed)	

				elif rand == 'R':
					if gameplane[25][startFrame + i + 2] == ' ' and gameplane[25][startFrame + i + 3] == ' ' and gameplane[26][startFrame + i + 2] == colours.BROWN + '#' + bcolors.ENDC:
						gameplane[25][startFrame + i + 2] = colours.YELLOW + 'R' + bcolors.ENDC
						gameplane[25][startFrame + i + 3] = colours.YELLOW + 'R' + bcolors.ENDC
						gameplane[25][startFrame + i] = ' '
						gameplane[25][startFrame + i + 1] = ' '
						i += 2
					elif gameplane[25][startFrame + i + 3] == colours.CYAN + '\\' + bcolors.ENDC or gameplane[25][startFrame + i + 2] == colours.CYAN + '\\' + bcolors.ENDC:
						gameplane[25][startFrame + i + 2] = colours.YELLOW + 'R' + bcolors.ENDC
						gameplane[25][startFrame + i + 3] = colours.YELLOW + 'R' + bcolors.ENDC
						gameplane[25][startFrame + i] = ' '
						gameplane[25][startFrame + i + 1] = ' '
						board.printboard(gameplane,startFrame,mario.lives,int(mario.score/100),mario.killed)

						if mario.lives > 1:
							mario.reduceLife(gameplane,gameLength)
						else:
							mario.lives = 0	
							board.printboard(gameplane,startFrame,mario.lives,int(mario.score/100),mario.killed)
							self.quitgame(int(mario.score/100),mario.killed)

	def endLevel(self,gameplane,mario,gameLength):
		mario.y = 24
		mario.x = gameLength - 10
		gameplane[mario.y][mario.x] = colours.RED  + '0' +  bcolors.ENDC
		gameplane[mario.y][mario.x + 1] = colours.RED +'0' +  bcolors.ENDC
		gameplane[mario.y + 1][mario.x] = colours.CYAN + '/' +  bcolors.ENDC
		gameplane[mario.y + 1][mario.x + 1] = colours.CYAN + '\\' + bcolors.ENDC
		os.system('killall aplay')
		os.system('aplay ./Music/flagpole.wav&')
		for i in range(19):
			gameplane[4 + i][gameLength - 12] = '/'
			gameplane[5 + i][gameLength - 13] = '/'
			gameplane[6 + i][gameLength - 13] = '\\'
			gameplane[7 + i][gameLength - 12] = '\\'
			gameplane[3 + i][gameLength - 12] = ' '
			gameplane[4 + i][gameLength - 13] = ' '
			gameplane[6 + i][gameLength - 12] = ' '
			board.printboard(gameplane,gameLength - 100,mario.lives,int(mario.score/100),mario.killed)
			sleep(0.05)

		#Mario exits	
		os.system('aplay ./Music/stage_clear.wav&')
		for i in range(7):
			mario.x += 1
			gameplane[mario.y][mario.x - 1] = ' '
			gameplane[mario.y + 1][mario.x - 1] = ' '
			gameplane[mario.y][mario.x] = colours.RED  + '0' +  bcolors.ENDC
			gameplane[mario.y][mario.x + 1] = colours.RED +'0' +  bcolors.ENDC
			gameplane[mario.y + 1][mario.x] = colours.CYAN + '/' +  bcolors.ENDC
			gameplane[mario.y + 1][mario.x + 1] = colours.CYAN + '\\' + bcolors.ENDC
			board.printboard(gameplane,gameLength - 100,mario.lives,int(mario.score/100),mario.killed)
			sleep(0.6)



		#Quit	
		#os.system('killall aplay')
		os.system('clear')
		print()
		print('Congratulations!! You cleared the level.')
		print('Your Final Score is ' + str(int(mario.score)))
		print('Enemies killed = ' + str(mario.killed))
		quit()	

	
	     