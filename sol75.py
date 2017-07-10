








class Solution(object):

	def countingSort(self,nums):

		countAry=[0]*3
	
		#histrogram	
		for n in nums:
			countAry[n]+=1

		#accumulate
		accTotal=0
		for idx,n in  enumerate( countAry[:]):
			countAry[idx]=accTotal+n
			accTotal+=n

		for n in nums[:]:
			nums[countAry[n]-1]=n
			countAry[n]-=1
		
		
	def sortColors(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		
		self.countingSort(nums)
		
sol = Solution()

ary =[0,1,2,2,1,0,2,2,1,1,0]

sol.sortColors(ary)

print ary