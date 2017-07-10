






class Solution(object):

	#buttom-up
	def VF2(self):

		for idx in range(1,len(self.itemList)+1):
			for w in range(1,(self.w+1)):

				if self.itemList[idx-1][1] > w:
					self.dTb[idx][w] = self.dTb[idx-1][w]
				else:
					self.dTb[idx][w] = max( self.dTb[idx-1][w], self.dTb[idx-1][w-self.itemList[idx-1][1]]+ self.itemList[idx-1][0])

		return self.dTb[3][4]

	# top-down
	def VF(self,idx,w):

		if w==0:
			return 0
		if w <0:
			return -self.tValue
		if idx ==0:
			return 0
		
		if self.dTb[idx][w] !=0:
			return self.dTb[idx][w]
 
		self.dTb[idx][w]= max( self.VF(idx-1,w) , self.VF(idx-1,w-self.itemList[idx-1][1]) + self.itemList[idx-1][0] )

		return self.dTb[idx][w]

	def findMaxV(self,itemList,weight):
		
		self.w=weight
		self.itemList=itemList
		self.tValue= sum([v for v,w in itemList])
		self.dTb= [ [0]*(self.w+1) for i in range(len(self.itemList)+1) ]
		self.pTb=[False for i,v in enumerate(self.itemList)]
		

		#res = self.VF(len(itemList),self.w)
		res = self.VF2()
		print self.dTb
		return res










itemList= [(1,1),(4,3),(3,2)]


sol = Solution()

print sol.findMaxV(itemList,4)