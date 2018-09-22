from Board import *
from Gameplay import *
from time import *
colours = bcolors()
board = GameBoard()
gaming = Gaming()
class Character():
	def __init__(self,x,y,jump,height,lives,score,killed):
		self.x=x
		self.y=y
		self.jump = jump
		self.height = height
		self.lives = lives
		self.score = score
		self.killed = killed
		


class Player(Character):		
	def __init__(self,x,y,jump,height,lives,score, killed):
		Character.__init__(self,x,y,jump,height,lives,score, killed)


	def moveLeft(self,gameplane,gameLength):
		if gameplane[self.y + 1][self.x - 2] in [' ',colours.PURPLE + '*' + bcolors.ENDC] and gameplane[self.y][self.x - 2] in [' ',colours.PURPLE + '*' + bcolors.ENDC] and gameplane[self.y + 1][self.x - 1] in [' ',colours.PURPLE + '*' + bcolors.ENDC] and gameplane[self.y][self.x - 1] in [' ',colours.PURPLE + '*' + bcolors.ENDC] and self.x > 3:
			#Collect coins
			if gameplane[self.y][self.x - 2] == colours.PURPLE + '*' + bcolors.ENDC:
				os.system('aplay ./Music/coin.wav&')
				self.score += 360
			if gameplane[self.y + 1][self.x - 2] == colours.PURPLE + '*' + bcolors.ENDC:
				os.system('aplay ./Music/coin.wav&')
				self.score += 360
			if gameplane[self.y][self.x - 1] == colours.PURPLE + '*' + bcolors.ENDC:
				os.system('aplay ./Music/coin.wav&')
				self.score += 360
			if gameplane[self.y + 1][self.x - 1] == colours.PURPLE + '*' + bcolors.ENDC:
				os.system('aplay ./Music/coin.wav&')
				self.score += 360

			self.x -= 2
			gameplane[self.y][self.x] = colours.RED + '0' + bcolors.ENDC
			gameplane[self.y][self.x + 1] = colours.RED + '0' + bcolors.ENDC
			gameplane[self.y][self.x + 2] = ' '
			gameplane[self.y][self.x + 3] = ' '
			gameplane[self.y + 1][self.x] = colours.CYAN + '/' + bcolors.ENDC
			gameplane[self.y + 1][self.x + 1] = colours.CYAN + '\\' + bcolors.ENDC
			gameplane[self.y + 1][self.x + 2] = ' '
			gameplane[self.y + 1][self.x + 3] = ' '
		#elif gameplane[self.y + 1][self.x - 2] == colours.PURPLE + '*' + bcolors.ENDC or gameplane[self.y + 1][self.x - 2] == colours.PURPLE + '*' + bcolors.ENDC
		
		elif gameplane[self.y + 1][self.x -1] == colours.GREEN + 'R' + bcolors.ENDC:
			#Set Frame
			startFrame = self.x - 50
			if startFrame < 0:
				startFrame = 0
			elif startFrame > gameLength - 100:
				startFrame = gameLength - 100	

			#Set Enemy
			gameplane[self.y + 1][self.x] = colours.GREEN + 'R' + bcolors.ENDC
			gameplane[self.y + 1][self.x + 1] = colours.GREEN + 'R' + bcolors.ENDC
			gameplane[self.y + 1][self.x - 1] = ' '
			gameplane[self.y + 1][self.x - 2] = ' '
			if self.lives > 1:
				self.reduceLife(gameplane,gameLength)	
			else:
				self.lives = 0	
				board.printboard(gameplane,self.x - 51,self.lives,int(self.score/100),self.killed)
				gaming.quitgame(int(self.score/100),self.killed)

	def moveRight(self,gameplane, gameLength):
		if gameplane[self.y + 1][self.x + 3] in [' ',colours.PURPLE + '*' + bcolors.ENDC] and gameplane[self.y ][self.x + 3] in [' ',colours.PURPLE + '*' + bcolors.ENDC] and gameplane[self.y + 1][self.x + 2] in [' ',colours.PURPLE + '*' + bcolors.ENDC] and gameplane[self.y ][self.x + 2] in [' ',colours.PURPLE + '*' + bcolors.ENDC] and self.x < gameLength - 5:
			#Collect coins
			if gameplane[self.y][self.x + 2] == colours.PURPLE + '*' + bcolors.ENDC:
				os.system('aplay ./Music/coin.wav&')
				self.score += 360
			if gameplane[self.y + 1][self.x + 2] == colours.PURPLE + '*' + bcolors.ENDC:
				os.system('aplay ./Music/coin.wav&')
				self.score += 360
			if gameplane[self.y][self.x + 3] == colours.PURPLE + '*' + bcolors.ENDC:
				os.system('aplay ./Music/coin.wav&')
				self.score += 360
			if gameplane[self.y + 1][self.x + 3] == colours.PURPLE + '*' + bcolors.ENDC:
				os.system('aplay ./Music/coin.wav&')
				self.score += 360
			self.x += 2
			gameplane[self.y][self.x] = colours.RED + colours.RED + '0' + bcolors.ENDC + bcolors.ENDC
			gameplane[self.y][self.x + 1] = colours.RED + colours.RED + '0' + bcolors.ENDC + bcolors.ENDC
			gameplane[self.y][self.x - 1] = ' '
			gameplane[self.y][self.x - 2] = ' '
			gameplane[self.y + 1][self.x] = colours.CYAN + '/' + bcolors.ENDC
			gameplane[self.y + 1][self.x + 1] = colours.CYAN + '\\' + bcolors.ENDC
			gameplane[self.y + 1][self.x - 2] = ' '
			gameplane[self.y + 1][self.x - 1] = ' '
		elif gameplane[self.y + 1][self.x + 2] == colours.GREEN + 'R' + bcolors.ENDC:
			#Set Frame
			startFrame = self.x - 50
			if startFrame < 0:
				startFrame = 0
			elif startFrame > gameLength - 100:
				startFrame = gameLength - 100	

			#Set Enemy
			gameplane[self.y + 1][self.x] = colours.GREEN + 'R' + bcolors.ENDC
			gameplane[self.y + 1][self.x + 1] = colours.GREEN + 'R' + bcolors.ENDC
			gameplane[self.y + 1][self.x + 2] = ' '
			gameplane[self.y + 1][self.x + 3] = ' '

			board.printboard(gameplane,startFrame,self.lives,int(self.score/100),self.killed)
			if self.lives > 1:
				self.reduceLife(gameplane,gameLength)
			else:
				self.lives = 0	
				gaming.quitgame(int(self.score/100),self.killed)	
				
	def up(self,gameplane):
		if gameplane[self.y - 1][self.x] in [' ',colours.PURPLE + '*' + bcolors.ENDC] and gameplane[self.y - 1][self.x + 1] in [' ',colours.PURPLE + '*' + bcolors.ENDC]:
			#Collect coins
			if gameplane[self.y - 1][self.x] == colours.PURPLE + '*' + bcolors.ENDC:
				os.system('aplay ./Music/coin.wav&')
				self.score += 360
			if gameplane[self.y - 1][self.x + 1] == colours.PURPLE + '*' + bcolors.ENDC:
				os.system('aplay ./Music/coin.wav&')
				self.score += 360

			self.y -= 1
			gameplane[self.y][self.x] = colours.RED + '0' + bcolors.ENDC
			gameplane[self.y][self.x + 1] = colours.RED + '0' + bcolors.ENDC
			gameplane[self.y + 1][self.x] = colours.CYAN + '/' + bcolors.ENDC
			gameplane[self.y + 1][self.x + 1] = colours.CYAN + '\\' + bcolors.ENDC
			gameplane[self.y + 2][self.x] = ' '
			gameplane[self.y + 2][self.x + 1] = ' '

	def down(self,gameplane):
		if gameplane[self.y + 2][self.x] in [' ',colours.PURPLE + '*' + bcolors.ENDC] and gameplane[self.y + 2][self.x + 1] in [' ',colours.PURPLE + '*' + bcolors.ENDC]:
			#Collect coins
			if gameplane[self.y + 2][self.x] == colours.PURPLE + '*' + bcolors.ENDC:
				os.system('aplay ./Music/coin.wav&')
				self.score += 360
			if gameplane[self.y + 2][self.x + 1] == colours.PURPLE + '*' + bcolors.ENDC:
				os.system('aplay ./Music/coin.wav&')
				self.score += 360

			self.y += 1	
			gameplane[self.y][self.x] = colours.RED + '0' + bcolors.ENDC
			gameplane[self.y][self.x + 1] = colours.RED + '0' + bcolors.ENDC
			gameplane[self.y - 1][self.x] = ' '
			gameplane[self.y - 1][self.x + 1] = ' '
			gameplane[self.y + 1][self.x] = colours.CYAN + '/' + bcolors.ENDC
			gameplane[self.y + 1][self.x + 1] = colours.CYAN + '\\' + bcolors.ENDC

	def reduceLife(self,gameplane,gameLength):
		self.lives -= 1
		os.system("killall aplay")
		os.system("aplay ./Music/death.wav&")
		#printboard
		for i in range(3):
			#Set Frame
			startFrame = self.x - 50
			if startFrame < 0:
				startFrame = 0
			elif startFrame > gameLength - 100:
				startFrame = gameLength - 100	
			board.printboard(gameplane,startFrame,self.lives,int(self.score/100),self.killed)
			print("Mario died. Respawning in ... " + str(3 - i))
			sleep(1)
		os.system("aplay ./Music/main_theme.wav&")



		gameplane[self.y][self.x] = ' '		
		gameplane[self.y][self.x + 1] = ' '	
		if self.y == 25:		
			gameplane[self.y + 1][self.x] = ' '		
			gameplane[self.y + 1][self.x + 1] = ' '
		self.x = 2
		self.y = 24
		gameplane[self.y][self.x] = colours.RED + '0' + bcolors.ENDC		
		gameplane[self.y][self.x + 1] = colours.RED + '0' + bcolors.ENDC		
		gameplane[self.y + 1][self.x] = colours.CYAN + '/' + bcolors.ENDC		
		gameplane[self.y + 1][self.x + 1] = colours.CYAN + '\\' + bcolors.ENDC

		



