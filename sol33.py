


33. Search in Rotated Sorted Array Add to List
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Subscribe to see which companies asked this question.





key points:

	1. 以midIdx 為切割點 其中一半會是遞增數列,用遞增數列來判斷target是否在裡面.

	


class Solution(object):


	#recursion


	def worker(self,s,e,target):

		if s>e:
			return -1


		if s == e:
			if self.nums[s]==target:
				return s 
			else:
				return -1

		if s==e-1:
			if self.nums[s]==target:
				return s 
			elif self.nums[e]==target:
				return e
			else:
				return -1

		midIdx= (s+e)/2


		if self.nums[midIdx] == target:
			
			return midIdx

		# find no-decreasing part   <=
		if self.nums[s] <= self.nums[midIdx-1]:
			if self.nums[s]<= target and target <= self.nums[midIdx-1]:
				return self.worker(s,midIdx-1,target)

			else:
				return self.worker(midIdx+1,e,target)

		else:
			if self.nums[midIdx+1] <= target and target <=self.nums[e]:
				return self.worker(midIdx+1,e,target)
			else:
				return self.worker(s,midIdx-1,target)




	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if nums==[]:
		    return -1
		self.nums=nums
		
		return self.worker(0,len(nums)-1,target)







sol =Solution()

ary = [2,3,4,5,6,7,8,9,1]
print sol.search(ary,6)