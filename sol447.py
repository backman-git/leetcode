


447. Number of Boomerangs

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).



key points:

	1. o(n**2) : hash table to store all same distance pairs.
	


	2. maybe try backtrack!!






class Solution(object):
	def numberOfBoomerangs(self, points):
		"""
		:type points: List[List[int]]
		:rtype: int
		"""

		ans=0
		for x1,y1 in points:
			dTlb={}
			for x2,y2 in points:
				dis=(x1-x2)**2 + (y1-y2)**2
				if dis not in dTlb:
					dTlb[dis]=1
				else:
					dTlb[dis]+=1

			for k,v in dTlb.items():
				ans+= v*(v-1)

		return ans








sol = Solution()


ary=[[0,0],[1,0],[2,0]]
print sol.numberOfBoomerangs(ary)