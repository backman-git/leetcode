
import sys
#shortest path problem!!
class Vertex(object):

	def __init__(self,label):
		self.d=sys.maxint
		self.p=None
		self.label=label


s=Vertex('s')
t=Vertex('t')
x=Vertex('x')
y=Vertex('y')
z=Vertex('z')
Vs={'s':s,'t':t,'x':x,'y':y,'z':z}
#edge table
#[h]->[t]
E ={ sP:{} for sP,v in Vs.items()}

'''
Bell-ford

E[s.label][t.label]=6
E[s.label][y.label]=7
E[t.label][z.label]=-4
E[t.label][t.label]=8
E[t.label][x.label]=5
E[x.label][t.label]=-2
E[y.label][x.label]=-3
E[y.label][z.label]=9
E[z.label][s.label]=2
E[z.label][x.label]=7
'''


#dijkstra
E[s.label][t.label]=10
E[s.label][y.label]=5

E[t.label][x.label]=1
E[t.label][y.label]=2

E[x.label][z.label]=4

E[y.label][t.label]=3
E[y.label][x.label]=9
E[y.label][z.label]=2

E[z.label][x.label]=6
E[z.label][s.label]=7






class Graph():

	def __init__(self,vs,es):
		self.Vs=vs
		self.Es=es

	def show(self):
		for sP,ePs in G.Es.items():
			for eP,v in ePs.items():
				print (sP,v,eP)

	def getEItems(self):
		res=[]
		for sP,ePs in G.Es.items():
			for eP,v in ePs.items():
				res.append((G.Vs[sP],v,G.Vs[eP]))

		return res

G=Graph(Vs,E)




def initSingleSorce(G,s):

	for l,v in  G.Vs.items():
		v.d=sys.maxint
		v.p=None


	G.Vs[s.label].d=0




def relax(h,t,w):

	if t.d > h.d + w:
		t.d = h.d+w
		t.p=h


# no nagative cycle!!  can have cycle and nagative edge!
#Bellman-ford   edge can be nagative
def BellManFord(G,s):

	initSingleSorce(G,s)

	for l,v in G.Vs.items():
		print (l,v.d),
	print "\n-----------" 


	for l,v in G.Vs.items():
		for item in G.getEItems():
			relax(item[0],item[2],item[1])

		


	for i in G.getEItems():

		if i[2].d > i[0].d+i[1]:
			return False

	return True


print BellManFord(G,s)
print "BellManFord"



#Dijkstra    positive edge!


import heapq



def dijkstra(G,s):
	
	initSingleSorce(G,s)



	
	q=[(v.d,v) for l,v in G.Vs.items()]

	heapq.heapify(q)
	uNode=[]
	while len(q)!=0:
		
		nV,node=heapq.heappop(q)
		uNode.append(node)
		for item in [ item for item in G.getEItems() if item[0].label == node.label  ]:
			relax(item[0],item[2],item[1])
			q=[(v.d,v) for l,v in G.Vs.items() if v not in uNode]
			heapq.heapify(q)
			

	return


print G.show()
dijkstra(G,s)
print "dijkstra"
for l,v in G.Vs.items():
	print (l,v.d),





