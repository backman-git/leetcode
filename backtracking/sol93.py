



class Solution(object):
	




	def BK(self,idxs):


		
		if self.reject(idxs):
			return 

		if self.accept(idxs):
			print idxs

		for subStrs in self.gen(idxs):
			self.BK(subStrs)


	def reject(self,idxs):

		if len(idxs)==3 and idxs[-1] < self.sLen-4:
			return True
		else:
			return False


	def accept(self,idxs):

		if len(idxs)==3:
			return True
		return False






	def gen(self,idxs):

		if len(idxs)==3:
			return 

		yield idxs+[ idxs[-1]+1 if len(idxs)!=0 else 0]
		yield idxs+[ idxs[-1]+2 if len(idxs)!=0 else 1]
		yield idxs+[ idxs[-1]+3 if len(idxs)!=0 else 2]

		
 


	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		self.sLen=len(s)

		self.BK([])
		
		


sol = Solution()

strs="25525511135"
sol.restoreIpAddresses(strs)


