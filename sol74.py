



74. Search a 2D Matrix


key points:


	1.use last column to find target possible row

	2.  search the row  (binary search)






class Solution(object):
	
	def getLastCol(self,matrix):

		return [ matrix[y][self.w-1]  for y in range(self.h)           ]

	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""

		if matrix ==[]:
			return False

		if matrix ==[[]]:
			return False

		self.w= len(matrix[0])
		self.h= len(matrix)

		lastCol = self.getLastCol(matrix)

		#find target col
		targetRow=None
		for idx,v in enumerate(lastCol):
			if v  >= target:
				targetRow=idx
				break

		if targetRow is not None:
			if target in matrix[targetRow]:
				return True
			else:
				return False
		else:
			return False




		


sol = Solution()

mat =[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print sol.searchMatrix(mat,24)

