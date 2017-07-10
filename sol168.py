class Solution(object):
	def convertToTitle(self, n):
		return self.convertToTitle((n-1)/26)+chr((n-1)%26+ord('A')) if n!=0 else ""


sol =Solution()


print sol.convertToTitle(26)


