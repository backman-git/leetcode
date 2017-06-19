

import collections




class Solution(object):
	def distributeCandies(self, candies):
	
		if candies ==[]:
			return 0

		cnt=collections.Counter(candies)
		nType=len([(t,n) for t,n in cnt.items()])
		return min(nType,len(candies)/2)






sol =Solution()

cand=[1,1,2,3]
print sol.distributeCandies(cand)