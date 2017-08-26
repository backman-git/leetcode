import sys
class Solution(object):


	def BFS(self,root):
		mQ=[root]

		while len(mQ)!=0:
			n=mQ.pop(0)
			self.minV=min(abs(n.val-n.left.val) if n.left is not None else sys.maxint , abs(n.val - n.right.val) if n.right is not None else sys.maxint,self.minV)
			if n.left is not None:
				mQ.append(n.left)
			if n.right is not None:
				mQ.append(n.right)

	def getMinimumDifference(self, root):
		self.minV=sys.maxint
		self.BFS(root)

		return self.minV
	   


		


sol =Solution()

