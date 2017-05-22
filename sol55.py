












class Solution(object):



	
	def canJumpGreedy(self,nums):

		maxP=0
		for idx ,v  in enumerate(nums):
			if v !=0:
				maxP=max(maxP,idx+v)
			else:
				if maxP <= idx and idx != len(nums)-1:
					return False
		return True


	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if nums ==[]:
			return False
		if nums ==[0]:
			return True

		return self.canJumpGreedy(nums)





sol =Solution()

l=[3,2,1,0,4]
print sol.canJump(l)