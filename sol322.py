

import sys



class Solution(object):


	def minExchange(self,idx,value):

		



		if value ==0:
			return 0

		if  value <0:
			return sys.maxint

		if idx<0 :
			return sys.maxint


		if (idx,value) in  self.dpTlb:
			return self.dpTlb[(idx,value)]

		else:
			#print self.dpTlb
			self.dpTlb[(idx,value)]= min(self.minExchange(idx,value-self.cList[idx])+1,self.minExchange(idx-1,value))

		return self.dpTlb[(idx,value)]








	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""

		if coins ==[]:
			return -1

		self.cList=coins

		self.dpTlb={}

		res =self.minExchange(len(self.cList)-1,amount)

		return -1 if res  == sys.maxint else res 







sol = Solution()


print sol.coinChange([3,7,405,436],8839)