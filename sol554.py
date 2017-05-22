

import collections

class Solution(object):


	def findGaps(self,row):

		gap=0
		gapList=[]
		for b in row:
			gap+=b
			if gap!= self.width:
				gapList.append(gap)

		return gapList


	def leastBricks(self, wall):
		"""
		:type wall: List[List[int]]
		:rtype: int
		"""
		#find width:
		self.width=sum(wall[0])
		self.row=len(wall)

		gaps=[]

		for r in wall:
			gaps.append(self.findGaps(r))

		
		cnt=collections.Counter()
		for g in gaps:
			cnt+=collections.Counter(g)

		mostGap= cnt.most_common(1)

		if mostGap ==[]:
			return self.row
		else:
			return self.row - mostGap[0][1]





sol = Solution()

w=[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
w1=[[6],[6],[6]]
print sol.leastBricks(w1)