import sys
class Solution(object):

	def __init__(self):
		self.tlb={}

	def fn(self,l):
		if tuple(l) in self.tlb:
			return self.tlb[tuple(l)]
		minV=sys.maxint
		if l ==[0,0,0,0,0,0]:
			return 0
		for order in self.special:
			v= [ l[i]-order[i] for i in range(6)]
			#print l,order,v
			tV=map(lambda x: True if x>=0 else False,v)
			flag=reduce(lambda x,v: x and v ,tV)
			if flag:
				value= self.tlb[tuple(l)] if tuple(l) in self.tlb else self.fn(v)+order[-1] 				
				minV=min(minV,value)
		self.tlb[tuple(l)]=minV
		return minV

	def shoppingOffers(self, price, special, needs):
		self.special=[ [order[i]  if i < len(order)-1 else 0  for i in range(6)  ]+[order[-1]] for order in special ]
		for idx,n in enumerate(needs):
			self.special.append([ 0 if i !=idx else 1  for i in range(6)]+[price[idx]])
		return self.fn([ needs[i] if i <len(needs) else 0 for i in range(6)])



sol =Solution()
print sol.shoppingOffers([10,1,1,3,8,3],[[0,5,6,5,6,0,14],[6,3,2,1,2,0,11],[3,5,3,3,6,6,12],[0,3,0,6,6,1,25],[4,5,3,2,3,2,15],[2,0,1,6,2,4,2],[4,2,4,5,5,5,22],[3,2,6,3,5,4,9],[4,6,4,6,2,5,1],[3,0,0,6,6,2,18],[1,4,2,3,4,4,1],[3,2,6,6,4,4,2],[1,1,0,5,5,2,15],[0,1,5,4,6,5,7],[3,5,2,4,0,5,20],[3,0,3,6,3,2,3],[5,4,1,6,6,1,7],[2,1,6,1,2,2,8],[0,5,4,3,4,4,4],[2,0,2,5,1,5,7],[4,6,5,0,3,4,19],[0,5,6,3,0,5,8],[0,5,0,0,3,4,15],[5,6,1,1,0,3,15],[1,2,0,3,1,5,12],[2,1,6,3,6,3,7],[4,6,3,3,4,3,3],[1,5,5,6,4,6,19],[4,1,5,3,3,5,25],[2,1,6,4,2,3,7],[0,0,6,2,6,0,7],[4,3,0,3,6,3,5],[4,1,1,6,2,6,10],[5,2,5,5,1,4,8],[4,1,1,2,6,0,20],[5,6,3,0,2,1,12],[2,4,4,4,5,5,11],[0,2,2,3,2,1,13],[3,3,2,5,4,3,24],[3,1,3,0,0,4,20],[3,5,2,3,2,6,1],[6,2,6,4,4,0,24],[6,1,0,2,4,2,18],[0,5,6,1,0,2,20],[0,6,0,1,2,0,16],[5,6,0,2,6,5,7],[3,5,0,0,6,1,25],[1,3,1,6,0,6,3],[0,6,0,0,6,0,23],[1,5,2,4,2,3,18],[1,1,6,4,6,4,4],[3,3,5,2,5,4,21],[5,1,3,5,1,3,8],[0,2,3,6,0,6,3],[3,0,6,4,6,5,23],[3,1,4,6,4,0,24],[0,3,1,5,4,2,8],[5,6,5,3,6,6,3],[6,3,3,0,3,2,8],[0,6,5,3,0,0,10],[2,6,0,3,2,1,2],[6,2,3,5,1,6,2],[5,5,2,4,2,3,7]],[3,6,1,4,5,4])
print sol.tlb