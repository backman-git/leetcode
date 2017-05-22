















436. Find Right Interval

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.




key points:

	1. sorted function can sorted tuple!
	2. bisect can search tuple!
	3. 多使用bisect 避免造輪!






# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
	   self.start = s
	   self.end = e

import bisect




class Solution(object):
   

	def findRightInterval(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[int]
		"""
	

		invls= sorted( [ (v.start,idx)  for idx,v in enumerate(intervals)])

		res=[]
		for i in intervals:
			
			idx=bisect.bisect_right(invls,(i.end,))
			
			if idx >= len(invls):
				res.append(-1)
			else:
				res.append(invls[idx][1])

		return res



		
sol =Solution()


a = Interval(3,4)
b = Interval(2,3)
c = Interval(1,2)

ary = [a,b,c]


print sol.findRightInterval(ary)


