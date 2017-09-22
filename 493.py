



class Solution(object):
    def reversePairs(self, nums):


    	return self.reversePairsRecurrsion(nums[:-1],nums[-1])

		
    def reversePairsRecurrsion(self,nums,target):

    	if len(nums)==0:
    		return 0

    	res=0
    	for n in nums:
    		if  n >2*target:
    			res+=1
    	return res + self.reversePairsRecurrsion(nums[:-1],nums[-1])




        
sol = Solution()

print sol.reversePairs([1,3,2,3,1])