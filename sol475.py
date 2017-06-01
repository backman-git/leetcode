475. Heaters

Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.



key points:

	1.  use bSearch to quickly search near heaters 
	2. statement "in" in python operate from head to tail iteratively.
		2.1 I make a mistake to use in to check . O(nHouse*nHeater+nHeater*lg(nHeater)) ->  O(*nHouse*nHeater*lg(nHeater))




import bisect


class Solution(object):
	


	def findCloseHeaterDis(self,h):

		
		
		Idx = bisect.bisect(self.heaters,h)
		
		if Idx ==len(self.heaters):
			return h-self.heaters[Idx-1]

		if Idx == 0:
			return self.heaters[0]-h
		

		lHeaterP=self.heaters[Idx-1]
		rHeaterP=self.heaters[Idx]

		return min(h-lHeaterP,rHeaterP-h)
		

		




	def findRadius(self, houses, heaters):
		"""
		:type houses: List[int]
		:type heaters: List[int]
		:rtype: int
		"""
	  
	  	self.heaters=sorted(heaters)

		

		maxDis=0
		for h in houses:
				maxDis = max( self.findCloseHeaterDis(h),maxDis)
			
		return maxDis


sol =Solution()

houses=[1,2,3]
heaters=[2]
print sol.findRadius(houses,heaters)

