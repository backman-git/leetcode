




Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
Subscribe to see which companies asked this question.

key points:

	next permutation is minimumValue that larger than current value.


	1.backward find no-increasing array, if didn't find one, it reach the last permutation.

	2.find minValue in suffix larger than pivot Value. 

	3. reverse suffix array.

class Solution(object):
	def nextPermutation(self, nums):
		if len(nums)<=1:
			return
		#backward find no-increasing		
		pivotIdx = None 
		lastV=None
		for idx,v in reversed(list(enumerate(nums))):
			if idx == len(nums)-1:
				lastV=nums[-1]
			else:
				if v < lastV:
					pivotIdx=idx
					break
				else:
					lastV=v

		if pivotIdx is None:
			nums.reverse()
			return 
		# find minValue in suffix larger than pivot Value 
		minVIdx=0
		for i in range(pivotIdx+1,len(nums)):
			if nums[i] > nums[pivotIdx]:
				minVIdx=i
			else:
				break

		nums[pivotIdx],nums[minVIdx] = nums[minVIdx],nums[pivotIdx]

		#reverse suffix 
		ptr1=pivotIdx+1
		ptr2=len(nums)-1
		
		while ptr1 < ptr2:
			nums[ptr1],nums[ptr2]=nums[ptr2],nums[ptr1]
			ptr1+=1
			ptr2-=1
			
		






sol = Solution()

ary=[4,3,2,1]
sol.nextPermutation(ary)

print ary