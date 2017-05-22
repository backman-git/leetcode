
437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000



key points:

	1. because only need to answer the numbers of path.  No need to record the path.






# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None



class Solution(object):

	def pathValue(self,root,target):

		if root is None:
			return []
		lList=[  v+root.val    for v in self.pathValue(root.left,target)]
		rList=[  v+root.val    for v in self.pathValue(root.right,target)]
		res=lList+rList+[root.val]
		cList = [True for n in res if n==target]
		self.ans+=len(cList)

		return res 
			



	def pathSum(self, root, t):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: int
		"""
		self.ans=0

		l=self.pathValue(root,t)

		return self.ans






a1=TreeNode(10)
a2=TreeNode(5)
a3=TreeNode(-3)
a4=TreeNode(3)
a5=TreeNode(2)
a6=TreeNode(11)
a7=TreeNode(3)
a8=TreeNode(-2)
a9=TreeNode(1)



a1.left=a2
a1.right=a3

a2.left=a4
a2.right=a5

a3.right=a6

a4.left=a7
a4.right=a8

a5.right=a9


sol=Solution()

print sol.pathSum(a1,8)