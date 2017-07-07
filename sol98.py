


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isValidBST(self, root):

		if root is None :
			return True

		if ( root.left is None or root.left.val <= root.val  ) and ( root.right is None or root.val <= root.right.val):
			return True and self.isValidBST(root.left) and self.isValidBST(root.right)
		else:
			return False


