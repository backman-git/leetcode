import math
class Solution(object):
	
	def accept(self,l,c):
		return True if l[0]**2+l[1]**2==c else False

	def reject(self,l):
		return True if len(l)>2 else False

	def BK(self,l,c):

		if self.reject(l):
			return
		
		if len(l)==2 and self.accept(l,c):
			self.res.append(l)
			return
		
		for pL in self.gen(l,c):
			self.BK(pL,c)

	def gen(self,l,c):

		if len(l)==0:
			for i in range( int(math.sqrt(c) )+1 ):
				yield [i]
		else:
			for i in range(int(math.sqrt(c-l[0]))+1):
				yield l+[i]


	def judgeSquareSum2(self, c):
		self.res=[]
		self.BK([],c)
		return self.res



	def isSqrt(self,c):
		sC=int(math.sqrt(c))
		return True if sC**2==c else False


	def judgeSquareSum(self,c):

		for i in range( int(math.sqrt(c))+1 ):
			if math.isSqrt(c-i**2):
				return True

		return False





sol =Solution()
print sol.judgeSquareSum(6)