



Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.





key points:

	1. 這題需要再重新縮減









class Solution(object):


	def inBound(self,p):

		if (0<=p[0] and p[0]<self.bH) and (0<=p[1] and p[1]<self.bW):
			return True
		return False

	def setDigit(self,mPos):


		self.digitBoard[mPos[0]][mPos[1]]=-1

		adjPos=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
		adjPos=[ [mPos[0]+p[0],mPos[1]+p[1]] for p in adjPos]

		for p in adjPos:
			if self.inBound(p) and self.digitBoard[p[0]][p[1]] !=-1:
				self.digitBoard[p[0]][p[1]]+=1


	def DFS(self,cP):

		

		if self.inBound(cP) and self.cTlb[cP[0]][cP[1]] =='W':

			self.cTlb[cP[0]][cP[1]]='G'			
			if self.digitBoard[cP[0]][cP[1]] >=1:
				self.ansBoard[cP[0]][cP[1]]=str(self.digitBoard[cP[0]][cP[1]])
			
			elif self.digitBoard[cP[0]][cP[1]]==0:
				self.ansBoard[cP[0]][cP[1]]='B'
				adjPos=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
				adjPos=[ [cP[0]+p[0],cP[1]+p[1]] for p in adjPos]

				for p in adjPos:
					self.DFS(p)
			
			elif self.digitBoard[cP[0]][cP[1]]==-1:
				self.ansBoard[cP[0]][cP[1]]='X'


			self.cTlb[cP[0]][cP[1]]='B'









	def updateBoard(self, board, click):
		"""
		:type board: List[List[str]]
		:type click: List[int]
		:rtype: List[List[str]]
		"""

		if board==[] or board==[""]:
			return board

		self.bW=len(board[0])
		self.bH=len(board)
		self.ansBoard=[[board[y][x] for x in range(self.bW)] for y in range(self.bH)]
		self.digitBoard= [[0  for x in range(self.bW)] for y in range(self.bH)]
		self.cTlb= [['W' for x in range(self.bW)] for y in range(self.bH)]
		minePos= [ [y,x]  for x in range(self.bW) for y in range(self.bH) if board[y][x]=='M']

		

		for p in minePos:
			self.ansBoard[p[0]][p[1]]='M'
			self.setDigit(p)
			
	
		self.DFS(click)

		out=[]
		for r in self.ansBoard:
			out.append("".join(r))

		return out









sol = Solution()



mat=["EEEEE","EEMEE","EEMEE","EEEEE"]
mat2=["EEE","EEM","EEE"]
mat3=["B1E1B","B1M1B","B111B","BBBBB"]

click=[1,2]
for r in sol.updateBoard(mat3,click):
	print r