class Solution(object):
	def arrayPairSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		nums.sort()

		res=0
		for idx,v in enumerate(nums):
			if idx%2==0:
				res+=v

		return res






sol =Solution()

ary=[1,100]
print sol.arrayPairSum(ary)