

215. Kth Largest Element in an Array



Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Show Tags
Show Similar Problems




key points:

	1. use heapq lib
	



import heapq


class Solution(object):
	def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""

	



		if nums ==[]:
			return nums

		heapq.heapify(nums)
		print nums

		for i in range(len(nums)-k+1):
			ans=heapq.heappop(nums)

		return ans



sol = Solution()

l=[2,1]
print sol.findKthLargest(l,1)