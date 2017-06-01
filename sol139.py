

139. Word Break




Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".


key points:
	
	top down 比較慢

	buttom up 比較快

	代碼比我精簡 （未研究）

buttom up 
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    # @good coding!
    def wordBreak(self, s, dict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]


top down
class Solution(object):

	def __init__(self):

		self.dTlb={}

	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""

		if s in self.dTlb:
			return self.dTlb[s]

		if s in wordDict:
			self.dTlb[s] = True
			return self.dTlb[s] 
		elif len(s)==1:
			self.dTlb[s] = False
			return self.dTlb[s] 

		res =False
		for c in range(1,len(s)):

			res =res or ( self.wordBreak(s[:c],wordDict) and self.wordBreak(s[c:],wordDict) )
			if res is True:
				break



		self.dTlb[s]=res
		return self.dTlb[s] 


sol = Solution()

s="leetcode"
dictStr=["l","e","t","c","o","d"]
print sol.wordBreak(s,dictStr)

#print sol.dTlb
