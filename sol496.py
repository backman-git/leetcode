class Solution(object):
	def nextGreaterElement(self, findNums, nums):
		"""
		:type findNums: List[int]
		:type nums: List[int]
		:rtype: List[int]
		"""

		stack=[]

		nextTlb={}

		for n in nums:
			if len(stack)==0:
				stack.append(n)

			else:
				if stack[-1] < n:
					while(len(stack)!=0 and stack[-1]<n):
						nextTlb[stack.pop()]=n
					stack.append(n)
				else:
					stack.append(n)

		res=[]
		for v in findNums:
			if v in nextTlb:
				res.append(nextTlb[v])
			else:
				res.append(-1)

		return res



sol =Solution()

a1=[4,1,2]
a2=[4,3,2,6,5,4,3,7,1,9]
print sol.nextGreaterElement(a1,a2)

