



class Solution(object):


	def fn1(self,x,y):
		return [x[0] or y[1]    , x[1] or y[1]]


	def findOcean(self,x,y,vTlb):

		for y in range(self.h):
			for x in range(self.w):
				print self.ansMatrix[y][x],
			print ""
		print"------"
		vTlb[y][x]=True

		if self.ansMatrix[y][x] !=[None,None]:
			return self.ansMatrix[y][x]


		
		right=None
		down=None
		left=None
		up=None

		#up
		if y-1!=0 and vTlb[y-1][x] is False:
			up=self.findOcean(x,y-1,vTlb)
		#down
		if y+1!=self.h and vTlb[y+1][x] is False:
			down=self.findOcean(x,y+1,vTlb)

		#left
		if x-1 !=0 and vTlb[y][x-1] is False:
			left= self.findOcean(x-1,y,vTlb)
		#right
		if x+1 != self.w and vTlb[y][x+1] is False:
			right= self.findOcean(x+1,y,vTlb)

		print [left,up,down,right]

		self.ansMatrix[y][x]=reduce(self.fn1,[left,up,down,right])

		return self.ansMatrix[y][x]

		# Pacific,Atlantic

	def pacificAtlantic(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[List[int]]
		"""
		self.matrix = matrix
		self.w = len(matrix[0])
		self.h = len(matrix)
		self.ansMatrix=[[[None,None] for w in range(self.w)] for h in range(self.h)   ]
		#inital enviroment
	


		res=[]
		#for y in range(self.h):
		#	for x in range(self.w):
		#		if self.findOcean(x,y,None) ==[True,True]:
		#			res.append([x,y])

		#vTlb=[[False for x in range(self.w)] for y in range(self.h) ]
		#print self.findOcean(0,4,vTlb)


		for y in range(self.h):
			for x in range(self.w):
				print self.ansMatrix[y][x],
			print ""

		return res


matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]





sol = Solution()

print sol.pacificAtlantic(matrix)