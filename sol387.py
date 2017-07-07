

import collections

class Solution(object):
	def firstUniqChar(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		
		cnt=collections.Counter(s)
		for idx,c in enumerate(s):
			if cnt[c]==1:
				return idx
		return -1


sol =Solution()


print sol.firstUniqChar("leetcode")


