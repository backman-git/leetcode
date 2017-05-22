

























import collections

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	


	def DFS(self,root):

		if root is None:
			return 

		else:
			self.s[root.val]+=1
			self.DFS(root.left)
			self.DFS(root.right)
			return 


	def findMode(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		self.s=collections.Counter()

		if root is None:
			return []


		self.DFS(root)

		maxC=self.s.most_common(1)[0][1]


		

		return [v for v in self.s if self.s[v] ==maxC  ]




a1= TreeNode(2)
a2= TreeNode(2)
a3= TreeNode(2)
a4= TreeNode(2)
a5= TreeNode(5)


a3.left=a2
a3.right=a4

a2.left=a1
a4.right=a5



sol=Solution()

print sol.findMode(a3)











