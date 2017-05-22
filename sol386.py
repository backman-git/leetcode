


class Solution(object):



	# TLE
	def lexicographicalOrder(self,a,b):

		if a==b:
			return 0

		sA=str(a)
		sB=str(b)

		for idx,c in enumerate(sA):
			if idx < len(sB) and  sA[idx] != sB[idx]:
				if str(sA) < str(sB):
					return -1
				else:
					return 1

			elif idx >=len(sB):
				return 1

		return -1


	def dLen(self,n):

		d=1

		while n>=10:
			n/=10
			d+=1
		return d

	def dYield(self,n):

		dL=self.dLen(n)

		lastV=0
		for i in range(dL-1,-1,-1):
			v=n/(10**i)
			yield v-lastV*10
			lastV=v

		yield -1


	#TLE
	def lexicographicalOrder2(self,a,b):

		if a==b:
			return 0


		gA=self.dYield(a)
		gB=self.dYield(b)
		
		while  True:
			
			dA=gA.next()
			dB=gB.next()	
			


			if dA == -1 or dB == -1:
				if dA == -1:
					return -1
				elif dB ==-1:
					return 1
				else:
					return 0

			if dA > dB:
				return 1
			elif dA < dB:
				return -1



		


	def lexicalOrderOLD(self, n):
		"""
		:type n: int
		:rtype: List[int]
		"""
		
		res =[d for d in range(1,n+1)]

		res=sorted(res,cmp=self.lexicographicalOrder)

		
		return res


	def fn(self,d,maxV):

		self.res.append(d)

		if d*10<=maxV:
			self.fn(d*10,maxV)
		if d<maxV and d%10 <9:
			self.fn(d+1,maxV)


	def lexicalOrder(self,n):

		self.res=[]

		self.fn(1,n)

		return self.res


sol =Solution()


print  sol.lexicalOrder(5656)

