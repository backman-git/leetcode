class Solution(object):
	def distributeCandies(self, candies):
		cSet = set(candies)
		return min(len(cSet),len(candies)/2)




sol =Solution()

cand=[1,1,2,3]
print sol.distributeCandies(cand)