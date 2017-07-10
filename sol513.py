513. Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

key points:

	two queue BFS (should remember the structure)
	












# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):




	def findBottomLeftValue(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""

		if len(root) ==1:
			return root.val

		qCurrent =[]
		qNext=[]


		qCurrent.append(root)
		while len(qCurrent) !=0:
			for n in qCurrent:

				if n.left is not None:
					qNext.append(n.left)
				if n.right is not None:
					qNext.append(n.right)


			if qNext ==[]:
				return qCurrent[0].val
			else:
				qCurrent=qNext[:]
				qNext=[]

sol = Solution()


root=TreeNode(2)
a = TreeNode(1)
b= TreeNode(3)
root.left =a
root.right=b


print sol.findBottomLeftValue(root)
