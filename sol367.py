




class Solution(object):


	def bSearch(self,s,e,t):

		

		if s>e:
			return False

		if s ==e :
			if s*s== t:
				return True
			else:
				return False

		mid = (s+e)/2
		
		sV=mid*mid

	

		if sV == t:
			return True
		elif sV <t:
			return self.bSearch(mid+1,e,t)
		else:
			return self.bSearch(s,mid-1,t)





	def isPerfectSquare(self, num):
		"""
		:type num: int
		:rtype: bool
		"""

		if num==0:
			return True
		if num==1:
			return True



		self.num=num

		return self.bSearch(1,num/2,num)




sol = Solution()

for n in xrange(1,50):
	print n,sol.isPerfectSquare(n)