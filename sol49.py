



Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]


key points:

	1.善用 for k,v in dTlb.items()：
	2. sorted(“cba”) 回傳['a','b','c']

class Solution(object):
	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""


		dTlb={}


		for s in strs:
			sortStr=''.join(sorted(s))
			if  sortStr in dTlb:
				dTlb[sortStr].append(s)
			else:
				dTlb[sortStr]=[s]

		res=[]

		for k,v in dTlb.items():
			res.append(v)

		return res



sol =Solution()


ary = ["eat", "tea", "tan", "ate", "nat", "bat"]
print sol.groupAnagrams(ary)