
'''
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.


Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].




Key Point:

	1.
		use hashTable to store the difference!
		O(n)

	2. use two pointer also can solve but need sort the array!
'''



#by hashTable
class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		
		needTlb={}
		
		for i in range(len(nums)):
	   
			if nums[i] in needTlb:
				return [needTlb[nums[i]] ,i]
			else:
				needTlb[target-nums[i]] = i
			
	
#by recursion
		
class Solution(object):

	def twoSum(self,nums,target):
		


		