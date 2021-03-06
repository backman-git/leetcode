




Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true


key points:

	collections.Counter()

	Counter("abc")


import collections

class Solution(object):


	def canConstruct(self, ransomNote, magazine):
		

		counter=collections.Counter(magazine)

		for c in ransomNote:
			counter[c]-=1
			if counter[c]<0:
				return False
		
		return True



sol = Solution()

print sol.canConstruct("aac","aab")

