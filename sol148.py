

import math
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	
	def printList(self,head):
		
		ptr=head.next
		while ptr!=None:
			print ptr.val
			ptr=ptr.next



	def sortList(self, head):
		
		#self.printList(head)

		dummyPtr= ListNode(-1)
		dummyPtr.next=head
		#o(n)
		nLen=0
		ptr=head
		while ptr!=None:
			nLen+=1
			ptr=ptr.next

		step =nLen

		while step/2 != 0:


			step=int(math.ceil(step/2.0))

			print str(step)+"<---"
			stepL=nLen/step

			fPtr=dummyPtr
			sPtr=dummyPtr

			# init window
			fPtr=fPtr.next
			for u in range(stepL):
				sPtr=sPtr.next



			#run
			for i in range(step):
				print fPtr.val
				print sPtr.val
				print "-----"

				for u in range(stepL):

					if fPtr.next is None or sPtr is None:
						break
					fPtr=fPtr.next
					sPtr=sPtr.next
		
			
		








sol = Solution()



a1=ListNode(1)
a2=ListNode(2)
a3=ListNode(3)
a4=ListNode(4)
a5=ListNode(5)
a6=ListNode(6)
a7=ListNode(7)
a8=ListNode(8)
a9=ListNode(9)
a10=ListNode(10)

a1.next=a2
a2.next=a3
a3.next=a4
a4.next=a5
a5.next=a6
a6.next=a7
a7.next=a8
a8.next=a9
a9.next=a10

sol.sortList(a1)