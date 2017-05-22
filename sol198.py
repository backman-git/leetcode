
class Solution(object):
	
	def __init__(self):

		self.dTlb={}


	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		


		if len(nums) ==0:
			return 0

		elif len(nums)==1:

			if 1 in self.dTlb:
				return self.dTlb[1]
			self.dTlb[1]=nums[0]
			return self.dTlb[1]

		elif len(nums)==2:

			if 2 in self.dTlb:
				return self.dTlb[2]

			self.dTlb[2]=max(nums[0],nums[1])

			return self.dTlb[2]
		else:

			if len(nums) in self.dTlb:
				return self.dTlb[len(nums)]

			self.dTlb[len(nums)]=max(nums[-1]+self.rob(nums[:-2]) , self.rob(nums[:-1]))

			return self.dTlb[len(nums)]            



sol = Solution()
ary=[2,3,4,5,6]
print sol.rob(ary)