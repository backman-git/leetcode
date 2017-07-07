




class Solution(object):
	def maximumProduct(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		nums.sort()
		return max(nums[0]*nums[1]*nums[-1],nums[-3]*nums[-2]*nums[-1])





sol = Solution()

print sol.maximumProduct([-1,-2,-3,-4])