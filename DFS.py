






mat = [[0 for i in range(8)] for j in range(8)]


sList=['y','x','z','w','s','v','t','u']




mat[0][1]=1
mat[1][2]=1
mat[2][0]=1
mat[3][1]=1
mat[2][3]=1
mat[4][2]=1
mat[4][3]=1
mat[5][3]=1
mat[5][4]=1
mat[6][5]=1
mat[7][5]=1
mat[6][7]=1
mat[7][6]=1

for r in mat:
	print r



class Solution:

	def __init__(self):

		pass


	def dfs(self,root):

		self.cTlb[root]='G'

		self.tTlb[root]=(self.time,None)
		self.time+=1

		connextNode = [ idx for idx,v in enumerate(self.mat[root]) if v==1 ]


		for n in connextNode:
			if self.cTlb[n] is 'W':
				self.eList.append((root,n,'T'))
				self.dfs(n)
			elif self.cTlb[n] is 'G':
				self.eList.append((root,n,'B'))
			elif self.cTlb[n] is 'B':

				self.eList.append((root,n,'C'))


		self.cTlb[root]='B'
		self.tTlb[root]=(self.tTlb[root][0],self.time)
		self.time+=1






	def classifyEdge(self,mat,sList):


		self.mat = mat
		self.sList=sList
		self.cTlb=['W' for i in range(len(mat))]
		self.tTlb=[None for i in range(len(mat))]
		self.time=1
		self.eList=[]
		self.dfs(4)
		self.dfs(6)

		print self.tTlb
		print self.cTlb

		cEList=[ (t[0],t[1])  for t in self.eList if t[2]=='C']




		print cEList


		#forward edge
		fElist=[]
		for t in cEList:
			sNode=t[0]
			eNode=t[1]
			if self.tTlb[sNode][0]< self.tTlb[eNode][0] and self.tTlb[eNode][1] < self.tTlb[sNode][1]:
				fElist.append((sNode,eNode))

		print fElist
		print self.eList

		print [[t[0],t[1]] for t in self.eList  ]





sol =Solution()

sol.classifyEdge(mat,sList)






