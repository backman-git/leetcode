


class Solution(object):
	def findMaxLength(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		if nums==[]:
			return 0

		maxL=0

		dTlb={0:0,1:0}

		for d in nums:
			dTlb[d]+=1

			if dTlb[0] == dTlb[1]:
				maxL=2*dTlb[0]

		return maxL






sol =Solution()



a=[0,0,1,1,0,1,0]
print sol.findMaxLength(a)