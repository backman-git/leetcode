


328. Odd Even Linked List



Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...

Credits:
Special thanks to @DjangoUnchained for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.




key points:

	
	1. use two pointers (odd,even)





# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def oddEvenList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		
		if head is None or  head.next is None:
			return head
		
		


		odd=head
		even=head.next

		oddPtr=head
		evenPtr=head.next



		idx=1
		while ( idx ==1 and oddPtr.next.next is not None) or ( idx==0 and evenPtr.next.next is not None):

			if idx ==1:

				oddPtr.next=oddPtr.next.next
				oddPtr=oddPtr.next

				idx=0
			else:
				evenPtr.next=evenPtr.next.next
				evenPtr=evenPtr.next
				idx=1
		
		
		oddPtr.next=even

		evenPtr.next=None

		
		

		
		
			
			
		return odd
				
				


sol = Solution()

a1=ListNode(1)
a2=ListNode(2)
a3=ListNode(3)
a4=ListNode(4)
a5=ListNode(5)
a6=ListNode(6)
a7=ListNode(7)
a8=ListNode(8)
a1.next=a2
a2.next=a3
a3.next=a4
a4.next=a5
a5.next=a6
a6.next=a7
a7.next=a8

		  

sol.oddEvenList(a1)
				
				