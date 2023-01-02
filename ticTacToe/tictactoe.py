grid = [[0,0,0],
				[0,0,0],
				[0,0,0]]
gameEnding = False
turnO = True
def GridOnScreen():
	for i in range(3):
		for j in range(3):
			print(" " + ("O" if grid[i][j] == 1 else ("X" if grid[i][j] == 2 else " " )), end = "")
			print(" |" if j<2 else "", end = "")
		print("   " + str(i+1))
		if(i < 2): print("-----------")
	print(" A   B   C")
	print("")
	print("")
	print("")
def LogicStuff():
	numX = 0
	numO = 0
	xIsWinner = False
	oIsWinner = False
	for i in range(3):
		if(grid[i][0] == 1): 
			numO += 1
		if(grid[i][0] == 2): 
			numX += 1
	if(numX == 3):
		xIsWinner = True
	elif(numO == 3):
		oIsWinner = True
	numX = 0
	numO = 0
	for i in range(3):
		if(grid[i][1] == 1):
			 numO += 1
		if(grid[i][1] == 2):
			 numX += 1
	if(numX == 3):
		xIsWinner = True
	elif(numO == 3):
		oIsWinner = True
	numX = 0
	numO = 0
	for i in range(3):
		if(grid[i][2] == 1):
			 numO += 1
		if(grid[i][2] == 2):
			 numX += 1
	if(numX == 3):
		xIsWinner = True
	elif(numO == 3):
		oIsWinner = True
	numX = 0
	numO = 0
	for i in range(3):
		if(grid[0][i] == 1):
			 numO += 1
		if(grid[0][i] == 2):
			 numX += 1
	if(numX == 3):
		xIsWinner = True
	elif(numO == 3):
		oIsWinner = True
	numX = 0
	numO = 0
	for i in range(3):
		if(grid[1][i] == 1):
			 numO += 1
		if(grid[1][i] == 2):
			 numX += 1
	if(numX == 3):
		xIsWinner = True
	elif(numO == 3):
		oIsWinner = True
	numX = 0
	numO = 0
	for i in range(3):
		if(grid[2][i] == 1):
			 numO += 1
		if(grid[2][i] == 2):
			 numX += 1
	if(numX == 3):
		xIsWinner = True
	elif(numO == 3):
		oIsWinner = True
	numX = 0
	numO = 0
	for i in range(3):
		if(grid[i][i] == 1):
			 numO += 1
		if(grid[i][i] == 2):
			 numX += 1
	if(numX == 3):
		xIsWinner = True
	elif(numO == 3):
		oIsWinner = True
	numX = 0
	numO = 0
	for i in range(3):
		if(grid[2-i][i] == 1):
			 numO += 1
		if(grid[2-i][i] == 2):
			 numX += 1
	if(numX == 3):
		xIsWinner = True
	elif(numO == 3):
		oIsWinner = True
	if(xIsWinner):
		gameDone = True
		print("X WINS yay !")
		exit()
	elif(oIsWinner):
		gameDone = True
		print("O WINS yay !")
		exit()	
	else:
		allFilled = True
		for i in range(3):
			for j in range(3):
				if(grid[i][j] == 0):
					 allFilled = False
		if(allFilled):
			gameDone = True
			print("It's a draw!!")
			exit()
  
def takeUserInput():
	inp = input("Enter the row you want ")
	while(not (inp.lower() == "1" or inp.lower() == "2" or inp.lower() == "3")):
		inp = input("Enter the row you want, 1,2, or 3 ")
	print("OK!")
	row = int(inp) - 1
	inp = input("" "Enter the coloumn you want """)
	while(not (inp.lower() == "a" or inp.lower() == "b" or inp.lower() == "c")):
		inp = input("Enter the coloumn you want, a,b, or c ")
	col = 0 if inp == "a" else (1 if inp == "b" else 2)
	grid[row][col] = 1 if turnO else 2
	print("")
	print("")
	print("")
print("Welcome to TicTacToe (another version cuz i can)")
print("")
print("Type where you want to play, enter the name of the row first, ie. 1,2,3, and then enter the name of the column, a,b,c")
print("")
print("")
GridOnScreen()
while True:
	if(turnO):
		print("It's O's Turn!")
	else:
		print("It's X's Turn!")
	takeUserInput()
	turnO = not turnO
	GridOnScreen()
	LogicStuff()




