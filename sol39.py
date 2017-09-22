



class Solution(object):


	def recurFn(self,target,idx,ans):

		if target ==0:
			self.res.append(ans)
			return
		if target<0 or idx <0:
			return 

		self.recurFn(target-self.candidates[idx],idx,ans+[self.candidates[idx]])
		self.recurFn(target,idx-1,ans)


	def combinationSum(self, candidates, target):
		self.candidates = sorted(candidates)

		self.res =[]

		self.recurFn(target,len(candidates)-1,[])
		
		return self.res
sol = Solution()

print sol.combinationSum([2,3,6,7],7)
