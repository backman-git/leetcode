
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def partition(self, head, x):
		"""
		:type head: ListNode
		:type x: int
		:rtype: ListNode
		"""
		
		ptr=head

		bPtr=ListNode(0)
		bHPtr=bPtr
		sPtr=ListNode(0)
		sHPtr=sPtr

		while ptr is not None:
			
			if ptr.val >= x:
				bPtr.next=ptr
				bPtr=bPtr.next
			else:
				sPtr.next=ptr
				sPtr=sPtr.next

			ptr=ptr.next

		bPtr.next=None

		sPtr.next=bHPtr.next


		return sHPtr.next 		




a=ListNode(1)
b=ListNode(4)
c=ListNode(3)
d=ListNode(2)
e=ListNode(5)
f=ListNode(2)

a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
f.next=None


sol = Solution()
p=sol.partition(a,3)

while p is not None:
	print p.val
	p=p.next






