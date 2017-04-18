

35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

Subscribe to see which companies asked this question.



key points:
	
	1. bisect library

	2. binSearch return idx




import bisect


class Solution(object):

	def binSearch(self,nums,s,e,target):
		
		if s >= e:
			if nums[s] >= target:
				return s
			elif nums[s] < target:
				return s+1



		midIdx = (s+e)/2

		if nums[midIdx] == target:
			return midIdx
		elif nums[midIdx] > target:
			return self.binSearch(nums,s,midIdx-1,target)
		else:
			return self.binSearch(nums,midIdx+1,e,target)






	def searchInsert(self,nums,target):
		if nums ==[]:
			return None

		return self.binSearch(nums,0,len(nums)-1,target)


	def searchInsert2(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""



		pos = bisect.bisect(nums,target)

		if nums[pos-1] == target:
			return pos -1
		else:
			return pos


		






sol = Solution()


print sol.searchInsert([],0)