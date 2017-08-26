

class Solution(object):


	def avg(self,x,y):
		div=0
		sumV=0

		for offsetX in range(-1,2):
			for offsetY in range(-1,2):
				if 0<= x+offsetX and x+offsetX < self.w and 0<= y+offsetY and y+offsetY <self.h:
					div+=1
					sumV+=self.M[y+offsetY][x+offsetX]

		return sumV/div

	def imageSmoother(self, M):
		"""
		:type M: List[List[int]]
		:rtype: List[List[int]]
		"""
		self.M = M
		self.h=len(ary)
		self.w=len(ary[0])

		res = [ [ self.avg(x,y) for x in range(self.w)  ] for y in range(self.h)  ]
		
		return res

sol = Solution()

ary=[[1,1,1],
	 [1,0,1],
	 [1,1,1]]
sol.imageSmoother(ary)