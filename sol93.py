




class Solution(object):

	def BT(self,sol):

		#if self.reject(sol) is True:
		#	return

		







		for ext in  self.extend(sol):
			print ext
			self.BT(ext)



	def extend(self,strs):

		if len(strs) == 3:
			return		

		for p in range(1,self.strL):
			if len(strs)==0 or strs[-1]< p:
				
				out=strs[:]
				out.append(p)
				yield out

	def genStrs(self,pL):
		
		out=self.decodeStr
		for p in pL:
			out = out[:p]+"."+out[p:]

		return out 




	def reject(self,pL):

		

		

	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		self.decodeStr=s
		self.strL= len(s)
	

		self.BT([])



	

	def valid(self,s):
		if 0<=int(s) and int(s)<=255:
			return True
		else:
			return False

	
				


sol =Solution()

s="25525511135"
sol.restoreIpAddresses(s)

pL=[3,7,11]
print sol.genStrs(pL)
print sol.reject(pL)