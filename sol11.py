class Solution(object):
	def fizzBuzz(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""

		if n==0:
			return []

		ans=[]

		for i in range(1,n+1):
			tmp=""

			if i%3==0:
				tmp+="Fizz"
			if i%5==0:
				tmp+="Buzz"

			if len(tmp)==0: 
				tmp=str(i)

			ans.append(tmp)

		return ans



sol = Solution()


print sol.fizzBuzz(15)