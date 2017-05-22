

566. Reshape the Matrix

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.





key points:


	1. python: the variables are defined in comprehensions effects outside variables of comprehensions.  

class Solution(object):
	def matrixReshape(self, nums, r, c):
		"""
		:type nums: List[List[int]]
		:type r: int
		:type c: int
		:rtype: List[List[int]]
		"""


		if nums ==[]:
			return nums


		mRow= len(nums)
		mCol= len(nums[0])

		mElements= [nums[row][col] for row in range(mRow) for col in range(mCol) ]  
		
		if mRow*mCol != r*c:
			return nums

		res=[]
		row=[]
		for idx,v in enumerate(mElements):

			if idx % c ==0:
				row=[]
				row.append(v)
			else:
				row.append(v) 

			if idx % c ==c-1:
				res.append(row)


		return res







sol = Solution()



ary=[[1,2],[3,4]]
print sol.matrixReshape(ary,1,4)