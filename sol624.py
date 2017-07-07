





class Solution(object):
	def maxDistance(self, arrays):
		
		ary =[(v,r) for r,ary in enumerate(arrays) for v in ary ]
		ary.sort()
		ptr1=0
		ptr2=len(ary)-1

		#l to right
		d1=0
		while ptr1 <ptr2:

			if ary[ptr2][1] != ary[ptr1][1]:
				d1=ary[ptr2][0]-ary[ptr1][0]
				break
			else:
				ptr1+=1


		# r to l
		ptr1=0
		ptr2=len(ary)-1
		d2=0
		while ptr1 <ptr2:

			if ary[ptr2][1] != ary[ptr1][1]:
				d2=ary[ptr2][0]-ary[ptr1][0]
				break
			else:
				ptr2-=1


		return d1 if d1 >d2 else d2





ary=[[-10,-9,-8,-7,-2,-1,0,1],[-4]]


sol =Solution()
print sol.maxDistance(ary)