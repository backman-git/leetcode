
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

key point:
	
	1. two queue
	2. qCurrent= qNext[:] only content not pointer!
	





# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def largestValues(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if root is None:
			return []
		qCurrent=[]
		qNext=[]
		res=[]
		qCurrent.append(root)
		
		while True:
			maxCurrent=None
			while len(qCurrent) !=0:
				
				node=qCurrent.pop(0)
				
				maxCurrent = max(node.val,maxCurrent)
				if node.left is not None:
					qNext.append(node.left)
				if node.right is not None:
					qNext.append(node.right)	

			res.append(maxCurrent)
			if len(qNext) ==0:
				break
			else:
				qCurrent=qNext[:]
				qNext=[]
				

		return res





root= TreeNode(-1)
a1= TreeNode(3)
a2= TreeNode(2)

b1= TreeNode(5)
b2= TreeNode(3)
b3= TreeNode(9)

root.left=a1
root.right=a2

a1.left=b1
a1.right=b2
a2.right=b3


sol =Solution()
print sol.largestValues(root)