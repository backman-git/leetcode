class Solution(object):
	def findUnsortedSubarray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		# left no-decreasing sequence

		if nums==[]:
			return 0

		res = len(nums)
		upBound=0
		for ptr in range(0,len(nums)):

			if ptr == len(nums)-1:
				res-=1

			elif nums[ptr]<=nums[ptr+1]:
				res-=1
			else:
				upBound=nums[ptr+1]
				break

		
		if res==0:
			return 0

		for ptr2 in range(len(nums)-1,-1,-1):

			if ptr2 == 0:
				res-=1

			elif nums[ptr2]>upBound and nums[ptr2-1] <=nums[ptr2] :
				res=res-1
			else:
				break
		return res



sol = Solution()

print sol.findUnsortedSubarray([2,3,4,6,5,4,4,7,8,9])