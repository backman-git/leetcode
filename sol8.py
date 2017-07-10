


class Solution(object):

	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""

		if nums == []:
			return []

		nums=sorted(nums)
		
		ans=[]
		for i in range( pow(2,len(nums))) :

			item =[]
			bValue=bin(i)[2:].zfill(len(nums))

			for j in range(len(nums)):
				if bValue[j]  =='1':
					item.append(nums[j])


			ans.append(item)	

		return ans



sol =Solution()
nums=[1,2,3]
print sol.subsets(nums)