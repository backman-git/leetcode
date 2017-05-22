





class Solution(object):
	
	def next_permutation(self,l):

		if len(l)<=1:
			return l

		pIdx=None
		#find no-increasing suffix
		for idx in range(len(l)-2,-1,-1):
			if l[idx] < l[idx+1]:
				pIdx=idx
				break

		if pIdx is None:
			return 

		cIdx=None
		#find minValue larger than pivot Value
		for idx in range(pIdx+1,len(l)):
			if  l[idx]>l[pIdx]:
				cIdx=idx
			else:
				break

		l[cIdx],l[pIdx]=l[pIdx],l[cIdx]

		ptr1=pIdx+1
		ptr2=len(l)-1

		while ptr1<ptr2:
			
			l[ptr1],l[ptr2]=l[ptr2],l[ptr1]
			ptr1+=1
			ptr2-=1

		return l






	def getPermutation(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: str
		"""
		pList=[n for n in range(1,n+1)]

		for i in range(1,k):
			pList=self.next_permutation(pList)


		pList=map(lambda x: str(x),pList)

		return "".join(pList)


sol =Solution()

print sol.getPermutation(9,273815)