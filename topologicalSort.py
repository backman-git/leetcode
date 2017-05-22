







mat=[[0 for i in range(10)] for j in range(10)]



mat[1][2]=1
mat[1][8]=1
mat[2][3]=1
mat[3][6]=1
mat[4][3]=1
mat[4][5]=1
mat[5][6]=1
mat[7][8]=1



















class tSort():







	def dfs(self,node):
		if self.tList[node] is not None:
			return

		self.tList[node]=(self.time,None)
		self.time+=1

		connectNodes=[idx for idx,v in enumerate(self.mat[node]) if v ==1  ]
		for n in connectNodes:
			if self.tList[n] is None:
				self.dfs(n)

		self.tList[node]=(self.tList[node][0],self.time)
		self.time+=1

		if self.tList[node][0] is not None and self.tList[node][1] is not None:
			self.sList.append(self.itemList[node])




	def topologicalSort(self,mat):

		self.tList = [None for i in range(10)]
		self.itemList= [None,"undershorts","pants","belt","shirt","tie","jacket","socks","shoes","watch"]

		self.time=1
		self.mat=mat
		self.sList=[]
		# start from 1
	
		self.dfs(4)
		self.dfs(9)
		self.dfs(1)

		self.sList.reverse()

		print self.sList

tSort= tSort()

tSort.topologicalSort(mat)
