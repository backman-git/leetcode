
62. Unique Paths


A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

key points


import math

class Solution(object):


	def C(self,m,n):

		'''
			(m+n)!/ (m!*n!)

		'''
		upV=1
		for v in range((m+n),m,-1 ):
			upV*=v

		downV=math.factorial(n)

		return upV/downV


	def uniquePaths(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		if m<=0 or n<=0 :
			return 0

		#C(m-1,n-1)
		if m>=n:
			return self.C(m-1,n-1)
		else:
			return self.C(n-1,m-1)





class Solution(object):
	def uniquePaths(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		
		DP_T=[ [0 for x in range(n)] for y in range(m)]






		DP_T[0][0]=1

		for x in range(0,n):
			for y in range(0,m):


				if x-1 >=0:
					DP_T[y][x]+=DP_T[y][x-1]
				if y-1 >=0:
					DP_T[y][x]+=DP_T[y-1][x]

		return DP_T[m-1][n-1]


#-----------------------------------------------------------------

obj = Solution()



print obj.uniquePaths(3,7)

















sol =Solution()

print sol.uniquePaths(7,0)