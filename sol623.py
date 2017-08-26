# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def addOneRow(self, root, v, d):
		if d==1:
			newNode=TreeNode(v)
			newNode.left=root
			return newNode

		self.deep=1
		queue=[]
		tmpQ=[]
		queue.append(root)
		while len(queue) !=0:
			while len(queue)!=0:
				n=queue.pop(0)
				if self.deep == d-1:
					newNode=TreeNode(v)
					newNode.left=n.left
					n.left=newNode
					newNode=TreeNode(v)
					newNode.right=n.right
					n.right=newNode
					return root
				
				if n.left is not None:
					tmpQ.append(n.left)
				if n.right is not None:
					tmpQ.append(n.right)

			self.deep+=1
			queue=tmpQ
			tmpQ=[]

		return root

		






sol =Solution()



a1=TreeNode(4)
a2=TreeNode(2)
a3=TreeNode(6)
a4=TreeNode(3)
a5=TreeNode(1)
a6=TreeNode(5)


a1.left=a2
a1.right=a3
a2.left=a4
a2.right=a5
a3.left=a6



sol.addOneRow(a1,1,1)