

300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.




key points:

	P.S. I always fall in this kind of problems!



	1. 用以結尾做DP:
		10 9 2 5 3 7 101 18
		1  1 1 1 1 1 1    1
		1  2 1 1 1 1 1    1
		1  2 1 1 1 1 1    1
		1  2 1 2 1 1 1    1
		1  2 1 2 2 1 1    1
		1  2 1 2 2 3 1    1
		1  2 1 2 2 3 4    1
		1  2 1 2 2 3 4    1

		max => 4


	2. patience sorting!!


		2	
		9	3		18
		10	5	7	101




import bisect







class Solution(object):

	#O(n**2)
	def lengthOfLIS2(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if nums==[]:
			return 0

		dis=[1]*len(nums)

		#tail
		for idx,n in enumerate(nums):
			for ptr in range(0,idx):

				if nums[ptr] < n:
					dis[idx] = max(dis[idx],dis[ptr]+1)


		return max(dis)

	#patience sorting


	def lengthOfLIS(self,nums):

		piles=[]


		for n in nums:

			if len(piles) ==0:
				piles.append([n])

			else:
			
				
				tops=[ pile[-1] for pile in piles]

				p=bisect.bisect_left(tops,n)

				if p ==len(piles):
					piles.append([n])

				else:
					piles[p].append(n)

		
		return len(piles)







		






sol =Solution()




print sol.lengthOfLIS([10,9,2,5,3,7,101,18])