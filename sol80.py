class Solution(object):
	def removeDuplicates(self, nums):
		
		repeatFlag = False
		currentV= None
		for idx,n in enumerate(nums[:]):
			if currentV is None:
				currentV = n

			elif repeatFlag == False and n != currentV:
				currentV = n

			elif repeatFlag == False and n == currentV:
				repeatFlag = True

			elif repeatFlag == True and n != currentV:
				repeatFlag = False
				currentV = n
			else:
				pass
			
		return len(nums)



sol = Solution()

print sol.removeDuplicates([1,1,1,1,2,2,2,4,4,4,4,4,55,55,55])