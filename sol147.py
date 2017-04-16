Sort a linked list using insertion sort.




key point:


	1.	
		使用dummy Node 方便建立traverse 方法
		ptr2 = dummy
		while ptr2.next is not None and ptr2.next.val < ptr1.val
	2. # 補圖
		必要時多建指針方便指定 建立next 指針 

		a->b->c->d



# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):



	def insertionSortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""

		ptr1 = head

		dummy = ListNode(-1)

		while ptr1 is not None:



			ptr2=dummy

			#find position
			next = ptr1.next
			# 
			while ptr2.next is not None and ptr2.next.val < ptr1.val:
				ptr2=ptr2.next


			ptr1.next =ptr2.next	
			ptr2.next = ptr1
			ptr1=next			





		return dummy.next







sol =Solution()



a1 = ListNode(0)
a2 = ListNode(6)
a3 = ListNode(4)
a4 = ListNode(5)
a5 = ListNode(3)
a6 = ListNode(2)
a7 = ListNode(1)

a1.next=a2
a2.next=a3
a3.next=a4
a4.next=a5
a5.next=a6
a6.next=a7

sol.insertionSortList(a1)