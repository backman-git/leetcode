



class Solution(object):


		

	def isSubsequence(self, a, b):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""

		dTlb = [[0]*(len(b)+1) for i in range(len(a)+1)]

		

		for idxA in range(len(a)):
			for idxB in range(len(b)):
				if a[idxA] == b[idxB]:
					dTlb[idxA+1][idxB+1] = dTlb[idxA][idxB]+1

				else:
					dTlb[idxA+1][idxB+1] = max(dTlb[idxA+1][idxB] , dTlb[idxA][idxB+1])
			
			
			if dTlb[idxA+1][len(b)] != idxA+1:
				return False
	
		return True

		


sol = Solution()



print sol.isSubsequence("abxc","ahbgdc")		