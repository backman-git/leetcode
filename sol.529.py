



class Solution(object):
	
	def __init__(self):

		self.board=[]

	def clickAction(x,y):


		if self.board[y][x] =="M":
			self.board[y][x]="X"
			return True
		else:





	def updateBoard(self, board, click):
		"""
		:type board: List[List[str]]
		:type click: List[int]
		:rtype: List[List[str]]
		"""
		self.board=board




	
		




sol =Solution()





board=[ ['E','E','E','E','E'],
		['E','E','M','E','E'],
		['E','E','E','E','E'],
		['E','E','E','E','E']]

click=[3,0]

sol.updateBoard(board,click)
