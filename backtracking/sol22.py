






class Solution(object):

	def __init__(self):
		self.res=[]
	#Backtrack way

	def gen(self,lT):

		yield (lT[0]+'(',lT[1]+1,lT[2])
		yield (lT[0]+')',lT[1],lT[2]+1)

	def reject(self,lT,n):

		if lT[2] > lT[1] or (lT[1]+lT[2])>(n*2) or lT[1] >n :
			return True
		return False

	def accept(self,lT,n):
		if (lT[1]+lT[2])==(n*2) and lT[1]==lT[2]:
			return True
		return False


	def BK(self,lT,n):
		if self.reject(lT,n):
			return 

		if self.accept(lT,n):
			self.res.append(lT[0])


		for sl in self.gen(lT):
			self.BK(sl,n)


	def generator(self,left,right,s,n):
		if(right == n):
			self.res.append(s)
		
		if( left < n): 
			self.generator(left+1,right,s+'(',n)
		
		if (right <left):     
			self.generator(left,right+1,s+')',n)
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		
		self.BK(('',0,0),n)
		#self.generator(0,0,'',n)
		return self.res

sol = Solution()

print sol.generateParenthesis(3)
