

23. Merge k Sorted Lists


[[2],[],[1] ]


key points:

	use heap!!()









import heapq


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""

		if lists ==[]:
			return []

		heap=[]

		dummyNode = ListNode(0)
		ptr=dummyNode

		for l in lists:
			if l is not None:
				heapq.heappush(heap,(l.val,l))

		while len(heap)!=0:
			val,l=heapq.heappop(heap)
			ptr.next=l
			if l.next is not None:
				heapq.heappush(heap,(l.next.val,l.next))
			ptr=ptr.next
		
		return dummyNode.next



a1 =ListNode(1)
a2 =ListNode(3)
a3 =ListNode(5)
a4 =ListNode(7)

a1.next =a2
a2.next =a3
a3.next =a4


b1 =ListNode(2)
b2 =ListNode(6)
b3 =ListNode(10)

b1.next = b2
b2.next = b3
c1 =ListNode(4)
c2 =ListNode(8)

c1.next=c2

d1=None

sol = Solution()

head=sol.mergeKLists([a1,b1,c1,d1])


while head is not None:
	print head.val,
	head=head.next
