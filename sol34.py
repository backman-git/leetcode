






















import bisect






class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		if nums == []:
			return [-1,-1]


		lIdx=bisect.bisect_left(nums,target)
		if lIdx >= len(nums) or  nums[lIdx] != target:
			return [-1,-1]
		
		ptr=lIdx+1
		while ptr <len(nums) and nums[ptr] == target :
			ptr+=1


		rIdx=ptr


		return [lIdx,rIdx-1]

sol = Solution()

ary=[5,7,7,8,8,8,8,8,8,8,10]
print sol.searchRange(ary,8)