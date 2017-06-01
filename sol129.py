# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None





class Solution(object):



	def dfs(self,root,v):

		if root.left is None and root.right is None:
			self.tSum+=v*10+root.val

		if root.left is not None:
			self.dfs(root.left,v*10+root.val)

		if root.right is not None:
			self.dfs(root.right,v*10+root.val)



	def sumNumbers(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.tSum=0
		
		if root is None:
			return 0

		self.dfs(root,0)

		return self.tSum





a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)

a1.left = a2
a1.right =a3

sol = Solution()

print sol.sumNumbers(a1)

