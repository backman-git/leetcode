

















class Solution(object):
	

	def extend(self,l,deep):

		
		if   deep < len(self.nList) and  ( l==[] or l[-1] <=self.nList[deep]):
			yield l[:]
			yield l[:]+[self.nList[deep]]

	

	def reject(self,l,deep):

		if  deep > len(self.nList) :
			return True
		return False


	def accept(self,l,deep):
		if len(l) >=2 and deep == len(self.nList):
			return True
		return False




	def BK(self,l,deep):


		if self.reject(l,deep):
			return

	
		if self.accept(l,deep):
			if l not in self.res:
				self.res.append(l)
			return 


		for l in self.extend(l,deep):
			self.BK(l,deep+1)




	def findSubsequences2(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		self.nList=nums
		self.res = []
		

		if nums ==[]:
			return []


		self.BK([],0)

		return self.res


	def findSubsequences(self,nums):

		if nums==[]:
			return []

		res=set()
		for n in nums:
			for t in list(res):
				if n>= t[-1]:
					res.add(t+(n,))
			res.add((n,))

		return [l for l in res if len(l)>1 ]







sol = Solution()

ary=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print sol.findSubsequences(ary)