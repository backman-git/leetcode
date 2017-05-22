

61. Rotate List



Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

Subscribe to see which companies asked this question.







key points:

	1. make circle

	2. rotate 








#Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None










class Solution(object):
	def rotateRight(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""

		if head is None:
			return None


		#find end and count len
		ptr1 =head
		lLen=1
		while ptr1.next is not None:
			lLen+=1
			ptr1=ptr1.next

		#make circle
		ptr1.next=head

		#find cut point

		for i in range(lLen-(k%lLen)):
			ptr1=ptr1.next

		res=ptr1.next
		ptr1.next=None

	

		return res






sol = Solution()

a1=ListNode(1)
a2=ListNode(2)
a3=ListNode(3)
a4=ListNode(4)
a5=ListNode(5)

a1.next=a2
a2.next=a3
a3.next=a4
a4.next=a5





sol.rotateRight(a1,2)
