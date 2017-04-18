



Write a function to find the longest common prefix string amongst an array of strings.


key point :

	1. function(*[arg1,arg2,arg3])   * unpack



	2. itertools izip function return iter!!













# two loop
class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		
		if len(strs) ==0:
			return ""
		
		
		
		
		res=""
		
		for i in range(len(strs[0])):
			
			c=strs[0][i]
			
			for obj in strs:
				if i >= len(obj) or obj[i] != c:
					return res
			
			res+=c
			
			
		return res
			





import itertools


# functional programming
class Solution(object):

	def isSameWord(self,t):
		
		t = list(t)

		res =  map(lambda x: True if x ==t[0] else False,t)
		res = reduce(lambda x,y: x and y, res )


		
		return res


	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		res=""
		for wTuple in  itertools.izip(*strs):
			if self.isSameWord(wTuple):
				res+=wTuple[0]
			else:
				break
		return res




sol =Solution()

strs=["112ab","212cd","312ef","412jj"]
print sol.longestCommonPrefix(strs)