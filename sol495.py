


class Solution(object):
	def findPoisonedDuration(self, timeSeries, duration):
		"""
		:type timeSeries: List[int]
		:type duration: int
		:rtype: int
		"""



		res=0

		for idx,v in enumerate(timeSeries):

			res+= min(timeSeries[idx+1]-v,duration) if idx != len(timeSeries)-1 else duration

		
		return res

sol= Solution()

print sol.findPoisonedDuration([1,2],2)