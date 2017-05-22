








l =[1,2,3,4,5]



def parent(i):
	return i/2

def left(i):
	return 2*i
def right(i):
	return 2*i+1

def heapify(l,i):

	lIdx = left(i)
	rIdx = right(i)

	

	largestIdx = i
	maxV=0
	if lIdx <= len(l)-1 and l[lIdx] > l[i] :
		largestIdx=lIdx
	if rIdx <= len(l)-1 and l[rIdx] > l[largestIdx] :
		largestIdx=rIdx
	if largestIdx != i:
		tmp =l[i]
		l[i]=l[largestIdx]
		l[largestIdx]=tmp
		print l
		heapify(l,largestIdx)




def buildMaxHeap(l):

	#idx start from 1

	l.insert(0,None)
	lastIdx = len(l)-1
	for idx in range(parent(lastIdx),0,-1): 
		heapify(l,idx)


def extractMax(l):

	if len(l) ==2:
		res =l[1]
		l.pop()

		return res


	maxV=l[1]
	lastV=l.pop()
	l[1]=lastV

	heapify(l,1)

	return maxV


def heapSort(l):

	res = []

	while len(l)!=1:
		res.append(extractMax(l))


	return res




#buildMaxHeap(l)

#print heapSort(l)


#  lib heapq
l2 =[4,5,6,3,2,1,8,7,9]
import heapq

heapq.heapify(l2)

def heapSort2(l):

	heap=[]

	for obj in l:
		heapq.heappush(heap,obj)


	return [heapq.heappop(heap) for i in range(len(l))]

print heapSort2(l2)











