





class Solution(object):


	def __init__(self):

		self.ans=[]

	def extend(self,subSet,level):	

		if level == len(self.nList):
			return

		yield subSet[:]
		yield subSet[:]+[self.nList[level]]



	def reject(self,subSet,level):

		if subSet in self.ans and level == len(self.nList):
			return True
		else:
			return False

	def accept(self,subSet,level):

		if level == len(self.nList):
			return True
		return False
			


	def BK(self,subSet,level):

		if self.reject(subSet,level):
			return

		if self.accept(subSet,level) :
			self.ans.append(subSet)
			return 


		for s in self.extend(subSet,level):
			self.BK(s,level+1)

		







	def subsetsWithDup(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		if nums ==  []:
			return []
		self.nList= sorted(nums)


		self.BK([],0)

		return self.ans


sol =Solution()
print sol.subsetsWithDup([4,4,4,1,4])

