Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST 
is changed to the original key plus sum of all keys greater than the original key in BST.


key points:

	1. reverse inorder 



class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	
	def inorder(self,root):

		if root == None :
			return
		self.inorder(root.right)
		print root.val
		self.inorder(root.left)


	def convertBST(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""

		self.inorder(root)



