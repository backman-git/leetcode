


53. Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.


key points:

	1. fn(ary)= max( fn(ary[:mid]),fn(ary[mid+1:]) , cn(mid) )
		cn: crossSum:


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
