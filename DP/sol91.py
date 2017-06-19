






class Solution(object):


	def fn(self,v):
		
		#able to decode

		if v=="":
			return False


		elif len(v)==1:
			if int(v)==0:
				return False
			else:
				return True

		elif len(v)==2:

			if v[0]=='0':
				return False
			elif 1<=int(v) and int(v)<=26:
				return True
			else:
				return False

		else:
			return False




	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		
		if s=="":
			return 0

		v=[0]*len(s)


		for idx,c in enumerate(s):

			if idx ==0:
				if self.fn(c):
					v[idx]=1


			else:

				if self.fn(s[idx]) is False and self.fn(s[idx-1:idx+1]) is False:
					return 0

			
				elif self.fn(s[idx]) is True and self.fn(s[idx-1:idx+1]) is True :
					v[idx]=v[idx-1]+1
				elif self.fn(s[idx]) is False and self.fn(s[idx-1:idx+1]) is True :
					v[idx]=v[idx-1]-1

				else:
					v[idx]=v[idx-1]
			


		return v[len(s)-1]


sol =Solution()

print sol.numDecodings("102")



