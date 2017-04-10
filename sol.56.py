




Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].


main point:
	
	sorted(,key)




#Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def merge(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[Interval]
		"""

		intervals=sorted(intervals,key=lambda x: x.start)

		res=[]
		for interval in intervals:

			if len(res) ==0 or res[-1].end <interval.start:
				res.append(interval)
			else: 
				res[-1].end = max(res[-1].end,interval.end)

		return res

sol = Solution()

a= Interval(2,6)
b= Interval(1,3)

l=[a,b]

for i in sol.merge(l):
	print i.start,i.end