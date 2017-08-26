


Given an input string, reverse the string word by word.

For example,Given s = "the sky is blue",
return "blue is sky the".


main point:

	python strip() and [::-1]



sol:

class Solution:

	def reverseWords(self, s):
		return " ".join(s.split()[::-1])

sol =Solution()

print sol.reverseWords("111 222 321")