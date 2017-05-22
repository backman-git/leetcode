




class Solution(object):
	def findDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		s=1
		e=len(nums)-1
		self.nList=nums
		return self.findDuplicateMod(s,e,(s+e)/2)

		
	# mod way

	def findDuplicateMod(self,s,e,mid):



		nSmall=0
		for n in self.nList:
			if n <= mid:
				nSmall+=1

		print str(s)+"-"+str(e)
		print "mid:"+str(mid)+" n:"+str(nSmall)
		
		if  <= mid:

			if e-s ==1:
				return e

			return self.findDuplicateMod(mid+1,e, (e+mid+1)/2 )
		else:
			if e-s ==1:
				return s
			return self.findDuplicateMod(s,mid-1, (s+mid-1)/2 )



sol = Solution()


n=[1,2,3,3]
print sol.findDuplicate(n)