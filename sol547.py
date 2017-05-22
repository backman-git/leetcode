

547. Friend Circles


There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.


key points:
	
	1. use array base to implement set operateiioon
		1.1 union implementation should assign big group to small group and vice versa.



class Solution(object):



	def union(self,a,b):

		if self.manSet[a] != self.manSet[b]:

			gMin = min(self.manSet[a],self.manSet[b])
			gMax = max(self.manSet[a],self.manSet[b])

			for idx, val in enumerate(self.manSet):
				if val == gMax:
					self.manSet[idx]=gMin


		
	def findCircleNum(self, M):
		"""
		:type M: List[List[int]]
		:rtype: int
		"""

		if M == [] or M ==[[]]:
			return 0

		nMan= len(M)

		self.manSet=[idx for idx in range(0,nMan)]

		# i < j
		for i in range(0,nMan):
			for j in range(i+1,nMan):
				if M[i][j] ==1 :
					self.union(i,j)
	


		return len(set(self.manSet[:]))








sol = Solution()


mat=[[1,0,0,1],      
	 [0,1,1,0],
	 [0,1,1,1],
	 [1,0,1,1]]


'''
0 ->3
1 ->2
2 ->1
2 ->3
3 ->0
3 ->2




'''

print sol.findCircleNum(mat)