




class Solution(object):

	def __init__(self):

		self.romanTlb={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

	def findCloseSymbol(self,num):

		num=abs(num)

		minDiff =num
		ans='I'
		for key,val in self.romanTlb.items():
			diff = num-val
			if abs(diff) < abs(minDiff) and diff>=0:
				minDiff= diff
				ans=key
			elif abs(diff) < abs(minDiff) and abs(diff) < self.romanTlb[ans]:
				minDiff=diff
				ans=key



		return ans



	def buildRoman(self,n,strs):

		if n ==0:
			return n,strs

		cSymbol=self.findCloseSymbol(n)


		
	
		if n >0 :
			n-=self.romanTlb[cSymbol]
			strs=strs+cSymbol
		else:
			n+=self.romanTlb[cSymbol]
			strs=strs+cSymbol
		print n,strs
		return self.buildRoman(n,strs)





	def intToRoman(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		if num ==0:
			return ""
		n,outStr =self.buildRoman(num,"")

		return outStr


		
		


sol = Solution()

print sol.intToRoman(39)