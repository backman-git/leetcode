











class Solution(object):

	def __init__(self):
		self.fFlag=False

	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		# row check
		for y in range(9):
			checkT={}
			for x in range(9):
				
				if board[y][x] !='.' and board[y][x]  in checkT.keys():
					return False
				elif  board[y][x] !='.':
					checkT[board[y][x]]=True

		for x in range(9):
			checkT={}
			for y in range(9):
				
				if board[y][x]!='.' and board[y][x]  in checkT.keys():
					return False
				elif board[y][x] !='.':
					checkT[board[y][x]]=True

		for Y in range(3):            
			for X in range(3):
				checkT={}
				for y in range(Y*3,(Y+1)*3):
					for x in range(X*3,(X+1)*3):
						
						if board[y][x] !='.' and board[y][x]  in checkT.keys():
							return False
						elif  board[y][x] !='.':
							checkT[board[y][x]]=True
		
		
		return True





	def vaildNums(self,nStr):

		dTable={str(n):False for n in range(1,10)}
		for c in nStr:
			dTable[c]=True

		nAry=[str(n) for n in range(1,10)]		
		out=map(lambda x: '.' if dTable[x] is True else x  ,nAry)
		out= [str(n) for n in out if n!='.']
		return  out



	def reject(self,board):
		return False if self.isValidSudoku(board) else True

	def accept(self,board):
		
		if board[8][8] !='.':
			return True
		else:
			return False




	def output(self,board):
		pass


	def findDot(self,board):

		for y in range(0,9):
			for x in range(0,9):
				if board[y][x]=='.':
					return (y,x)
		
		return None
	



	def extend(self,board):



			ptr= self.findDot(board)


			


			
			if ptr is not None:
				outBoard=[ [c for c in row] for row in board ]

				for n in range(1,10):
					outBoard[ptr[0]][ptr[1]]= str(n)
					out = [ "".join(row) for row in outBoard ]
					yield out

				
		
			
		



	def BT(self,board):

		print "----------"
		for r in board:
			print r
		print "==========\n\n"
		if self.reject(board) is True:
			return


		if self.accept(board) is True:
			self.board=board
			return


		if board[8][8]=='.' :
			for b in  self.extend(board):
				if self.fFlag is False:
					self.BT(b)










	def solveSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		

		

		self.BT(board)

		for r in range(0,9):
			
			board[r]=self.board[r]
	
		return 







sol = Solution()

board = ["....4..1.",".1..5394.","...68.527","...86....","86.....93","....32...","396.27...",".7431..6.",".8..9...."]


sol.solveSudoku(board)

print board