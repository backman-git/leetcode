# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def averageOfLevels(self, root):
		"""
		:type root: TreeNode
		:rtype: List[float]
		"""
	
		mainQ=[]
		tmpQ=[]
		res=[]
		res.append(root.val)

		mainQ.append(root)

		while len(mainQ)!=0:
			while len(mainQ)!=0:

				n=mainQ.pop(0)
				if n.left is not None:
					tmpQ.append(n.left)
				if n.right is not None:
					tmpQ.append(n.right)

			if tmpQ !=[]:
				value=sum([n.val for n in tmpQ])
				avgV= (1.0*value)/len(tmpQ)
				res.append(avgV)
			mainQ=tmpQ[:]
			tmpQ=[]
		return res


