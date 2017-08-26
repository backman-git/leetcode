class Solution(object):
	def maxArea(self, height):

		
		ptrH,ptrT = 0, len(height)-1

		res=0
		while ptrH < ptrT:
			res = max(min(height[ptrH],height[ptrT])*(ptrT-ptrH),res)

			if height[ptrH] < height[ptrT]:
				ptrH+=1
			else:
				ptrT-=1

		return res



sol = Solution()

print sol.maxArea([2,1,1,2])
