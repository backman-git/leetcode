


class Solution(object):

	def isPure(self,n):

		for c in n:
			if c in ["+","-","*"]:
				return False
		return True

	def compute(self,(lo,op,ro)):

		if op=="+":
			return int(lo)+int(ro)
		elif op=="-":
			return int(lo)-int(ro)
		else:
			return int(lo)*int(ro)
		

	def diffWaysToCompute(self, input):
		"""
		:type input: str
		:rtype: List[int]
		"""
	
		if self.isPure(input):
			return [int(input)]
		else:
			res=[]
			for idx,c in enumerate(input):
				if c in ["+","-","*"]:
					lo= input[:idx]
					ro= input[idx+1:]
					lVs=self.diffWaysToCompute(lo)
					rVs=self.diffWaysToCompute(ro)
					vPairs=[(lv,c,rv) for lv in lVs for rv in rVs]
					res.extend([self.compute(vP) for vP in vPairs])
			return res


sol =Solution()


ary="2"
print sol.diffWaysToCompute(ary)