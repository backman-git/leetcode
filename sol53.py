



class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		cV=[0]*len(nums)

		maxV=0

		for idx,v in  enumerate(nums):

			if idx==0:
				cV[idx]=v
				maxV=v
			else:
				cV[idx]=max(nums[idx-1],cV[idx-1])+nums[idx]
				maxV=max(v,cV[idx],maxV)

		return maxV








sol =Solution()

ary=[-2,1,-3,4,-1,2,1,-5,4]
print sol.maxSubArray(ary)
