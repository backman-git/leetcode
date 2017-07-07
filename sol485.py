



class Solution(object):
	def findMaxConsecutiveOnes(self, nums):
	   
		maxL=0
		cLen=0
		for n in nums:
			if n==1:
				cLen+=1
			else:
				maxL=max(maxL,cLen)
				cLen=0
		return max(maxL,cLen)



sol =Solution()

print sol.findMaxConsecutiveOnes([1,1,0,1,1,1])
