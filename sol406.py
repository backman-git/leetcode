406. Queue Reconstruction by Height




Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.




key Points:

	use tuple (0,0,0)  but it hard to change value inside
	change list instead

	有很好的解法
	vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
    auto comp = [](const pair<int, int>& p1, const pair<int, int>& p2)
                    { return p1.first > p2.first || (p1.first == p2.first && p1.second < p2.second); };
    sort(people.begin(), people.end(), comp);
    vector<pair<int, int>> res;
    for (auto& p : people) 
        res.insert(res.begin() + p.second, p);
    return res;
}




class Solution(object):
	



	def findLeftAndRest(self,pList,k):

		if len(pList) ==1:
			return pList[0],[]



		#find short and no one in front of it

		shortP=None
		rest=[]
	
		for p in pList:

			if  shortP is not None and  p[2]==0 and shortP[0]>= p[0]:
				shortP=p
			elif shortP is None and p[2] ==0:
				shortP= p



		rest = [ p for p in pList if p!=shortP]

		
		#update queue

		for p in rest:
			if p[0] <=shortP[0]:
				p[2]-=1		


		return shortP,rest




	def reconstructQueue(self, people):
		"""
		:type people: List[List[int]]
		:rtype: List[List[int]]
		"""
		
		
		if people ==[]:
			return []
		
		pList  = [ [p[0],p[1],p[1]] for p in people ]
		res =[]
		for idx in range(len(people)):
			p,rest=self.findLeftAndRest(pList,idx)
			pList=rest
			res.append(p)


		res = [ [p[0],p[1]] for p in res]

		
		return res

