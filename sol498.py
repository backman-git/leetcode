


498. Diagonal Traverse




Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.


Note:
The total number of elements of the given matrix will not exceed 10,000.
Subscribe to see which companies asked this question.




key points:


	1. 思考邊界方向跟走法




class Solution(object):
	


	def inBound(self,x,y):

		if (0<=x and x<self.mW) and (0<=y and y <self.mH):
			return True
		else:
			return False


	def findDiagonalOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""

		ptrX=0
		ptrY=0
		self.res=[]
		if matrix ==[[]] or matrix==[]:
			return []


		self.mW=len(matrix[0])
		self.mH=len(matrix)


		self.res.append(matrix[ptrY][ptrX])
		direction= False    # False RU , True LD

		for i in range((self.mW*self.mH)-1):

			if direction is False:

				if self.inBound(ptrX+1,ptrY-1):
					ptrX+=1
					ptrY-=1
				else:
					if self.inBound(ptrX+1,ptrY):
						ptrX+=1
					elif self.inBound(ptrX,ptrY+1):
						ptrY+=1
					direction=True
			else:
				if self.inBound(ptrX-1,ptrY+1):
					ptrX-=1
					ptrY+=1
				else:
					if self.inBound(ptrX,ptrY+1):
						ptrY+=1
					elif self.inBound(ptrX+1,ptrY):
						ptrX+=1
					direction=False

			self.res.append(matrix[ptrY][ptrX])

		return self.res






sol = Solution()



mat =[
	[ 1, 2, 3 ],
	[ 4, 5, 6 ],
	[ 7, 8, 9 ]]

print sol.findDiagonalOrder(mat)