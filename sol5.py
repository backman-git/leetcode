class Solution(object):

	def __init__(self):
		self.dpTable={}
	
	def inRange(self,num):
		if num[0]=="0":
			return False

		if 0< int( num) and int (num)<27:
			return True
		else:
			return False



	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""



		if s[0]=="0":
			return 0

		elif s=="":
			return 0

		elif len(s)==1:
			return 1


		result= self.dpTable.get(s,None)
		if result is not  None:
			return result


		result=0

		for dPtr in range(len(s)):
			
			
			

			if len(s[:dPtr]) ==0 and self.inRange(s[dPtr:])  is True:
				result+=1

			elif self.inRange(s[dPtr:]) is True:
				


				self.dpTable[s[:dPtr] ]=self.numDecodings( s[:dPtr] )
				result+=self.dpTable[s[:dPtr]]

			

			
			
	

		return result




sol = Solution()




print sol.numDecodings("101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010")
