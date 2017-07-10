
















# backtracking! slow~~~~~
class Solution(object):
	
	def reject(self,l):
		if len(l)>3:
			return True 
		return False

	def accept(self,l):
		if len(l)==3 and l[0]+l[1]>l[2]:
			return True
		return False


	def BK(self,l,source):

		if self.reject(l):
			return 

		if self.accept(l):
			self.res.append(l)

		for p,s in self.gen(l,source):
			self.BK(p,s)

	def gen(self,l,source):
		if source !=[] and len(l)<3:
			yield l+[source[0]] , source[1:]
			yield l , source[1:]

	def triangleNumber2(self,nums):

		self.res=[]
		nums.sort()
		self.BK([],nums)
		return len(self.res)

	#=============================================

	#base on two sum
	def triangleNumber(self,nums):

		nums.sort(reverse=True)
		self.res=0
		for idx,v in enumerate(nums):

			ptrL=idx+1
			ptrR=len(nums)-1

			while ptrL<ptrR:

				if nums[ptrL]+nums[ptrR] > v:
					self.res+=ptrR-ptrL					
					ptrL+=1
				else:
					ptrR-=1

		return self.res











sol = Solution()

print sol.triangleNumber([2,2,3,4])