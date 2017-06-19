

import collections

class Solution(object):
	def leastBricks(self, wall):
		"""
		:type wall: List[List[int]]
		:rtype: int
		"""
		
		cnt=collections.Counter()


		for row in wall:
			ptr=0
			for gap in row[0:-1]:
				pos=gap+ptr
				
				cnt[pos]+=1
				ptr=pos
			
		if len( cnt.most_common(1)) ==0:
			return len(wall)

		g,c =cnt.most_common(1)[0]
		return len(wall)-c
		
		





sol = Solution()

w=[[1],[1],[1]]
print sol.leastBricks(w)