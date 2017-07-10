






class Solution(object):


	def grayCode(self, n):

		res=[]

		nRange= 1<<n
		for i in range(nRange):
			res.append((i>>1)^i)
		return res


sol = Solution()

print sol.genGrayCode(4)