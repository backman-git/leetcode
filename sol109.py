

109. Convert Sorted List to Binary Search Tree




Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.


key points :


	1. recursion define of tree.


P.S. find more fast way!!






















# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None





class Solution(object):


	def buildTree(self,l):

		

		if l is None:
			return None


		if l.next is None:
			
			return TreeNode(l.val)

		if l.next.next is None:

			root = TreeNode(l.val)
		
			root.right = self.buildTree(l.next)
			return root




		#find mid node

		ptr1=l 
		ptr2=l 

		while ptr2.next and ptr2.next.next is not None:
			ptr1=ptr1.next
			ptr2=ptr2.next.next





		#build root node
		root=TreeNode(ptr1.val)
		
		#cut list
		cPtr=l
		while cPtr.next.val != root.val:
			cPtr=cPtr.next

		cPtr.next=None
		lPtr=l 
		rPtr=ptr1.next
		ptr1.next=None

		root.left = self.buildTree(l)
		root.right= self.buildTree(rPtr)



		return root


	def sortedListToBST(self, head):
		"""
		:type head: ListNode
		:rtype: TreeNode
		"""

		return self.buildTree(head)



sol =Solution()


a1=ListNode(1)
a2=ListNode(2)
a3=ListNode(3)
a4=ListNode(4)
a5=ListNode(5)
a6=ListNode(6)
a7=ListNode(7)
a8=ListNode(8)
a9=ListNode(9)


a1.next=a2
a2.next=a3
a3.next=a4
a4.next=a5
a5.next=a6
a6.next=a7
a7.next=a8
a8.next=a9


sol.sortedListToBST(a1)
