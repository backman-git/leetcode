

77. Combinations




Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]


key points:
	
	1. backtracking 
		1.1 if k > n/2 :
				backtrack the k:=n-k save time!! 









class Solution(object):
	



	def extend(self,l,n):

		if l==[]:
			for i in range(1,n+1):
				yield[i]
		else:
			for i in range(l[-1]+1,n+1):
				yield l+[i]




	def reject(self,l,n,nL):
		if l != [] and n-l[0]+1 < nL:
			return True
		return False

	def accept(self,l,n,nL):

		if len(l)==nL:
			return True
		return False

	def BK(self, l,n,nL):
		
		if self.reject(l,n,nL):
			return 

		#print l

		if self.accept(l,n,nL):
			self.ans.append(l)
			return

		for p in self.extend(l,n):
			self.BK(p,n,nL)

	def combine(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""

		if n==0:
			return []
		if k==0:
			return []

		self.ans=[]
		
		if k > n/2:
			self.BK([],n,n-k)

			self.ans = [  [n for n in range(1,n+1) if n not in a ] for a in self.ans                ]

		else:
			self.BK([],n,k)





		return self.ans


sol = Solution()

sol.combine(20,12)






