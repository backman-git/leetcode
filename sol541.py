class Solution(object):
	def reverseStr(self, s, k):
		
		return ''.join(list(reversed(s[:k]))+list(s[k:2*k]))+self.reverseStr(s[2*k:],k) if len(s)!=0 else ''

		




sol = Solution()

print sol.reverseStr("abcdefg",2)