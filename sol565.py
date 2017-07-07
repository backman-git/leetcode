

class Solution(object):
	def arrayNesting(self, nums):

		tTlb=[False for i in range(len(nums))]
		maxL=0

		for n in nums:
			if tTlb[n] is False:
				ptr=n
				pLen=0
				while tTlb[ptr] is False:
					tTlb[ptr]=True
					pLen+=1
					ptr=nums[ptr]
				maxL=max(maxL,pLen)
		return maxL



ary= [5,4,0,3,1,6,2]

sol = Solution()

print sol.arrayNesting(ary)