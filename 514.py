
import sys

class Solution(object):

	def rotate(self,ring,step):
		if step ==0:
			return ring
		step%=len(ring)
		return ring[step:]+ring[:step]
	

	def minDis(self,idx,ring):
		return min(idx,len(ring)-idx)
	

	def findRotateStepsRecurrsion(self,ring,key):
		if len(key)==0:
			return 0

		if dTlb.get((tuple(ring),key),None) is not None:
			return dTlb[(tuple(ring),key)]

		
		res=sys.maxint
		for idx,c in enumerate(ring):
			if c == key[0]:
				res=min(res, self.minDis(idx,ring) +1 + self.findRotateStepsRecurrsion(self.rotate(ring,idx) ,key[1:]) ) 
				dTlb[(tuple(ring),tuple(key))] = res
		return res



	def findRotateSteps(self, ring, key):

		global dTlb
		dTlb={}
		return self.findRotateStepsRecurrsion(list(ring),key)


sol = Solution()


print sol.findRotateSteps("cdcd","cd")



