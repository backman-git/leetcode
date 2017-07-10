



class TicTacToe:

	def __init__(self):

		self.currentBoard=[[" "," "," "] for x in range(3)]
		

	def draw(self):

		print "_____"

		for y in range(3):
			for x in range(3):
				print self.currentBoard[y][x],
			print ""
		print "-----\n\n"
	
	def setSig(self,sig,move,board):
		board[move[1]][move[0]]=sig
	

	def isWin(self,sig,board):
		#          sig should change to player

		#check row
		for r in range(3):
			if sig==board[r][0] and board[r][0] == board[r][1] and board[r][1] == board[r][2]:
				return True


		#check col
		
		for c in range(3):
			if sig==board[0][c] and board[0][c] == board[1][c] and board[1][c] == board[2][c]:
				return True
		#check dig

		#lu dr
		if sig==board[0][0] and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
			return True

		if sig==board[0][2] and board[0][2] == board[1][1] and board[1][1] == board[0][2]:
			return True



		return False


	def score(self,player,move,board):

		self.setSig(player,move,board)

		rival="X"
		if player=="X":
			rival="O"
		value=0

		if self.isWin(player,board) is True:
			value=10
		elif self.isWin(rival,board) is True:
			value=-10
		else:
			
			if len(self.ableMove(board))==0:
				value= 0
			else:
				value= -1

		self.setSig(" ",move,board)

		return value






	def ableMove(self,board):

		return [(x,y) for x in range(3) for y in range(3) if board[y][x]==" "]



	def bestMove(self,player,board):

		MVTable={}

		for move in self.ableMove(board):
			value = self.score(player,move,board)
			if value !=-1:
				MVTable[move]=value

			else:
				self.setSig(player,move,board)

				rival="X"
				if player == "X":
					rival="O"

				
				MVTable[move]=-1*self.score(rival,self.bestMove(rival,board),board)

				self.setSig(" ",move,board)



		maxV=-20
		bestM=None
		for move in MVTable.keys():

			if maxV <= MVTable[move]:
				maxV=MVTable[move]
				bestM=move

		print MVTable
		return bestM







ttt= TicTacToe()





ttt.setSig("X",(0,0),ttt.currentBoard)
ttt.setSig("O",(1,1),ttt.currentBoard)
ttt.setSig("X",(0,1), ttt.currentBoard)

'''
ttt.setSig("O",(0,2),ttt.currentBoard)
ttt.setSig("O",(1,2),ttt.currentBoard)
ttt.setSig("O",(2,2),ttt.currentBoard)
'''



while len(ttt.ableMove(ttt.currentBoard)) !=0:


	ttt.draw()
	inValue,move=input(">>")
	ttt.setSig(inValue,move,ttt.currentBoard)
	ttt.draw()

	rival="X"
	if inValue =="X":
		rival="O"

	print ttt.score(rival,ttt.bestMove(rival,ttt.currentBoard),ttt.currentBoard)
	ttt.setSig(rival,ttt.bestMove(rival,ttt.currentBoard),ttt.currentBoard)
	



