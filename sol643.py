class Solution(object):
	def findMaxAverage(self, nums, k):
		maxV = 0  
		sumV=0     
		for idx ,v in enumerate(nums):
			if idx==0:
				sumV=sum(nums[:k])
				maxV=sumV
			elif idx+k-1 <len(nums):
				sumV=sumV-nums[idx-1]+nums[idx+k-1]
				maxV =max(sumV,maxV)

		return maxV*1.0/k

sol =Solution()

print  sol.findMaxAverage([1,12,-5,-6,50,3], 3)