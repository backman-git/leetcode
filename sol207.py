



207. Course Schedule



There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.



key points:
	
	1. DFS search for acyclic DAG  




class Solution(object):


	def dfs(self,root):

		self.cTlb[root]='G'
		res=True
		for cNode in self.G[root]:
			
			if self.cTlb[cNode] is 'W':
				res&=self.dfs(cNode)
			elif self.cTlb[cNode] is 'G':
				return False

		self.cTlb[root]='B'

		return res





	def canFinish(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""
		if numCourses==0 and prerequisites==[]:
			return True


		self.G= {i:[] for i in range(numCourses)}
		self.cTlb=['W' for i in range(numCourses)]
		for e in prerequisites:
			self.G[e[0]].append(e[1])

		ans=True
		for idx , v in enumerate(self.cTlb):
			if v=='W':
				ans&=self.dfs(idx)


		return ans







sol =Solution()


print sol.canFinish(8,[[4, 2], [2, 0], [0, 1], [2, 3], [3, 1], [4, 3], [6, 5], [5, 3], [5, 4], [6, 7], [7, 5] ])