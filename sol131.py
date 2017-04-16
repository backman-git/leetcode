
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",

Return [["aa","b"],["a","a","b"]]


Key Point:
	
	1.
		字串partition 切割 ＢＦＳ


						   ---->['a','a']"b"  -----> ['a','a','b']''

			---> ['a']"ab" ---->['a','ab']''	

	  aab   ---> ['aa']"b" ---->['aa','b']''

	  		---> ["aab"]

	  		切割點

	2.
		isPalindrome: two pointer 



class Solution(object):


	def isPalindrome(self,strs):


		sPtr=0
		ePtr=len(strs)-1

		while sPtr < ePtr:



			if strs[sPtr] != strs[ePtr]:
				return False

			sPtr+=1
			ePtr-=1

		return True


	def ext(self,cutList,uncuted):
		
		if uncuted==[]:
			yield cutList[:],uncuted


		for i in range(1,len(uncuted)+1):
			yield cutList+[uncuted[:i]],uncuted[i:]

	def reject(self,cutList,uncuted):


		if cutList!=[] and self.isPalindrome(cutList[-1]) is False:
			return True
		return False
	

	def accept(self,cutList,uncuted):
		
		if uncuted=="":
			return True
		return False
		
			

	def BK(self,cutList,uncuted):


		if self.reject(cutList,uncuted):
			return 

		if self.accept(cutList,uncuted):
			self.res.append(cutList)


		for cutList,uncuted in self.ext(cutList,uncuted):
			self.BK(cutList,uncuted)	


	def partition(self, s):
		"""
		:type s: str
		:rtype: List[List[str]]
		"""
		self.res=[]
		self.BK([],s)

		return self.res

		




sol = Solution()
strs="aab"
print sol.partition(strs)



