




class Solution(object):
	def findPeakElement(self, nums):
		
		
		hPtr=0
		tPtr=len(nums)-1

		while hPtr < tPtr-1:

			mid = (hPtr+tPtr)/2

			if nums[mid-1] <nums[mid] and nums[mid] > nums[mid+1]:
				return mid

			elif nums[mid-1] > nums[mid]:
				tPtr=mid-1
			elif nums[mid+1] > nums[mid]:
				hPtr=mid+1

		return hPtr if nums[hPtr] > nums[tPtr] else tPtr



sol = Solution()

print sol.findPeakElement([-1])