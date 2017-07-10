


















class Solution(object):




	def findPairs(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""

		if nums ==[]:
			return 0

		uList=[]

		for n in nums:
			if n in uList:
				pass
			else:
				uList.append(n)

		uList.sort()

		return self.countPair(uList,k)


	def countPair(self,l,k):
		count=0
		for idx in range(len(l)):
			for idx2 in range(idx+1,len(l)):
				if l[idx2]-l[idx] ==k:
					count+=1

		return count 






sol = Solution()




print sol.findPairs([1,2,3,4,5],1)