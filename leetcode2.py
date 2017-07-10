


def LLen(head):
	ptr=head
	count=0

	while ptr.next !=None:
		ptr=ptr.next	
		count+=1
	return count+1

def findEnd(head):

	ptr=head

	while ptr.next !=None:
		ptr=ptr.next	
	
	return ptr	



def makeCircle(head):
	
	end=findEnd(head)
	end.next=head
	return head 



# Definition for singly-linked list.
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


		print LLen(head)

		# make circle
		head=makeCircle(head)
		






		


L=None
for i in range(1,6):
	x = ListNode(str(i))
	x.next=L
	L=x


ptr= L
while ptr.next != None:
	print ptr.val+"->",
	ptr=ptr.next
print ptr.val


sol = Solution()
sol.rotateRight(L,2)




