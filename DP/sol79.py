








key points:

	1.Backtracking is good for enumerating !! 






class Solution(object):



	def adjs(self,x,y):
		offsets=[(1,0),(-1,0),(0,1),(0,-1)]
		res=map(lambda (oX,oY): (oX+x,oY+y),offsets )		
		res= filter(lambda ((oX,oY)): True if (0<=oX and oX<self.w and 0<=oY and oY<self.h) else False ,res    )
		return res



	def accept(self,(pStr,lX,lY),word):
		if pStr == word:
			return True
		else:
			return False

	def reject(self,(pStr,lX,lY),word):

		ptr=len(pStr)-1
		if ptr!=-1 and (pStr[ptr]!=word[ptr]  or len(pStr) == self.wLen):
			return True
		return False

	def BK(self,(pStr,lX,lY),word):
		
		if self.accept((pStr,lX,lY),word):
			return True
		if self.reject((pStr,lX,lY),word):
			return False

		res=False
		self.tTlb[lY][lX]=True		

		for (nStr,x,y) in self.gen((pStr,lX,lY)):
			#here is trick!
			res = res or self.BK((nStr,x,y),word)
		self.tTlb[lY][lX]=False
		return res


	def gen(self,(pStr,lX,lY)):
			if len(pStr) <self.wLen:
				for x,y in self.adjs(lX,lY):
					if self.tTlb[y][x] is False:
						yield (pStr+self.board[y][x],x,y)


			


	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		
		if board==[] or word =="":
			return False

		self.board=board
		self.w=len(board[0])
		self.h=len(board)
		self.wLen=len(word)
		self.tTlb= [[False for x in range(self.w)] for y in range(self.h)]

		self.res=[]

		for x in range(self.w):
			for y in range(self.h):
				if self.BK((self.board[y][x],x,y),word):
					return True

		return False
				
		









sol = Solution()

board=["aaa",
	   "abb",
	   "abb",
	   "bbb",
	   "bbb",
	   "aaa",
	   "bbb",
	   "abb",
	   "aab",
	   "aba"]
word="aabaaaabbb"



print sol.exist(board,word)


