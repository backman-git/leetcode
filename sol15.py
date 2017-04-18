



15. 3Sum



Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.




key point:
	
	create two sum first!!



def twoSum(nums,target):

	s=0;
	e=len(nums)-1

	while s < e:
		tSum = nums[s]+nums[e]
		if tSum == target:
			yield [nums[s],nums[e]]
			s+=1
			e-=1
		elif tSum > target:
			e-=1
		else:
			s+=1

	yield None




class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		nums.sort()
		
		out=[]
		for i in range(0, len(nums)):
			for ans in twoSum(nums[i+1:],-nums[i]):
				if ans is not None:
					ansList=[nums[i]]+ans
					if ansList not in out :
						out.append(ansList)
				
				
		return out