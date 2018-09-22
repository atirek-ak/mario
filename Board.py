import os

class GameBoard():
	def __init__(self):
		pass

	def printboard(self,gameplane,startFrame,mariolives,score,killed):
		os.system("clear")
		print("Lives = " + str(mariolives))
		print("Score = " + str(score))
		print("Enemies killed = " + str(killed))
		print()
		for i in range(0,1):
			for j in range(0,100):
				print("_",end='')
			print()
		for i in range(28):
			for j in range(startFrame , startFrame + 100):
				if j == startFrame or j == startFrame + 99:
					print('|',end='')
				else:
					print(gameplane[i][j],end='')
			print()


class bcolors:
    BLUE = "\033[1;36m"
    BROWN = "\033[0;33m"
    GREEN = "\033[92m"
    ORANGE = "\033[1;31m"
    PURPLE = "\033[1;35m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RED = "\033[31m"
    YELLOW = "\033[1;33m"
    GRAY = "\033[1;30m"
    CYAN = "\033[0;34m"