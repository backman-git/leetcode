












class Solution(object):



		

	def robLine(self, nums):
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

			self.dTlb[len(nums)]=max(nums[-1]+self.robLine(nums[:-2]) , self.robLine(nums[:-1]))

			return self.dTlb[len(nums)]



	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		if len(nums) ==0:
			return 0
		if len(nums) ==1:
			return nums[0]


		self.dTlb={}
		lV=self.robLine(nums[:-1])
		self.dTlb={}
		rV=self.robLine(nums[1:])
		
		return max(lV,rV)



sol = Solution()
ary=[10]
print sol.rob(ary)