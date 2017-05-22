

from collections import deque
class Solution(object):


	def vaildPos(self,p):

		if (0<=p[0] and p[0]<self.w) and (0<=p[1] and p[1]<self.h):
			return True
		return False 




	def findDis(self,x,y):

		if self.cTlb[y][x] is 'W':


		

			if self.mat[y][x] == 0:
				self.cTlb[y][x]='B'
				self.dTlb[y][x]=0
				return 0



			else:
				self.cTlb[y][x]='G'
				res=self.w
				cPoints=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
				cPoints=filter(self.vaildPos,cPoints)
				
				for p in cPoints  :
					
					if self.cTlb[p[1]][p[0]] is 'W':
						res=min(self.findDis(p[0],p[1])+1,res)
					elif self.cTlb[p[1]][p[0]] is 'B':
						res=min(self.dTlb[p[1]][p[0]]+1,res)
					

				

				self.dTlb[y][x]=res
				self.cTlb[y][x]='B'


		elif self.cTlb[y][x] is 'B':
			res=self.dTlb[y][x]


		return res



	def updateMatrix(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[List[int]]
		"""

		if matrix ==[] or matrix ==[[]]:
			return []


		self.mat=matrix
		self.w= len(matrix[0])
		self.h= len(matrix)
		
		self.dTlb= [[0 for r in range(self.w)] for c in range(self.h)]
		self.cTlb=[['W' for r in range(self.w)] for c in range(self.h)]


		
		for r in range(self.h):
			for c in range(self.w):
				if self.mat[r][c] ==0:
					self.cTlb[r][c]='B'
					self.dTlb[r][c]=0
		


		list1=[(c,r) for c in range(self.w) for r in range(self.h) if self.mat[r][c]!=0 ]

		for p in list1:
			self.findDis(p[0],p[1])

					
		for c in self.cTlb:
			print c
		



		return self.dTlb




		




sol = Solution()



mat=[[1, 1, 1, 1, 1, 1, 0, 1, 1, 1], 
 [1, 1, 0, 0, 0, 0, 0, 1, 1, 1], 
 [0, 1, 0, 1, 1, 1, 1, 0, 0, 0], 
 [1, 1, 1, 0, 0, 1, 1, 0, 1, 1], 
 [1, 0, 1, 1, 1, 0, 1, 1, 1, 1], 
 [1, 1, 0, 0, 1, 0, 1, 1, 1, 1], 
 [1, 0, 1, 0, 0, 0, 1, 1, 0, 1], 
 [1, 1, 0, 1, 1, 1, 1, 0, 0, 1], 
 [1, 1, 1, 1, 0, 0, 0, 1, 1, 0], 
 [1, 1, 1, 0, 1, 1, 0, 1, 1, 1]]

for r in sol.updateMatrix(mat):
	print r