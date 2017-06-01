import collections

import sys

class Solution(object):

	def __init__(self):
		self.dTlb={}

	def findMaxForm(self, strs, m, n):


		return self.findMaxFormDriver(sorted(strs),m,n)



	def findMaxFormDriver(self, strs, m, n):
		"""
		:type strs: List[str]
		:type m: int
		:type n: int
		:rtype: int
		"""
		if m <0 or n <0 or len(strs)==0:
			return 0


		if (tuple(strs),m,n) in self.dTlb:
				return self.dTlb[(tuple(strs),m,n)]



		if len(strs)==1:
			cnt=collections.Counter(strs[0])

			if m >= cnt['0'] and n >= cnt['1']:
				self.dTlb[(tuple(strs),m,n)]=1
				return 1
			else:
				return 0


		

		res=0

		for i in range(len(strs)):
			l=strs[:]
			l.pop(i)
			cnt=collections.Counter(strs[i])
			
			if m >= cnt['0'] and n>=cnt['1'] :
				if (tuple(l),m-cnt['0'],n-cnt['1']) not in self.dTlb:
					self.dTlb[(tuple(l),m-cnt['0'],n-cnt['1'])]=self.findMaxFormDriver(l,m-cnt['0'],n-cnt['1'])+1
				
				res=max(res,self.dTlb[(tuple(l),m-cnt['0'],n-cnt['1'])])

		self.dTlb[(tuple(strs),m,n)]=res

		#print self.dTlb
		return self.dTlb[(tuple(strs),m,n)]

sol =Solution()

ary=["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]

print sol.findMaxForm((ary),9,80)
