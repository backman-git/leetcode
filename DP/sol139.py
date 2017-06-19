class Solution(object):

	def __init__(self):

		self.dTlb={}



	def driver(self,s,wordDict):

		if s in self.dTlb:
			return True
		elif s in wordDict:
			self.dTlb[s]=True
			return True
		else:
			for i in range(1,len(s)):
				
				res=self.wordBreak(s[:i],wordDict) and self.wordBreak(s[i:],wordDict)
				if res== True:
					self.dTlb[s]=True
					return True
				
		return False

	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""



		print sorted(wordDict,key=lambda x: len(x) )

		


		return self.driver(s,wordDict)


		



sol =Solution()


s="leetcode"
print sol.wordBreak(s,["leet","code"])

print sol.dTlb