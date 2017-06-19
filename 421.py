





# use Dict to build Tries is more straight forward.

'''
def searchTri(self,l):

	ptr= self.tri

	for c in l:
			
		if c not in ptr.keys():
					return False
		ptr=ptr[c]

	return True
'''


key points:

	1. build tries for problem.
	2. use dictionary to build tries (good solution)
	3. traverse the tries for number!




class Solution(object):
	

	def __init__(self):
		self.tri={}

	def buildTrie(self,binStrs):
		for s in binStrs:
			ptr=self.tri
			for c in s:
				if c not in ptr.keys():
					ptr[c]={}
				ptr=ptr[c]

	def findLengthXOR(self,strs):
		base=2**31
		nLen=0
		ptr=self.tri
		for c in strs:

			if c=='1':
				rc='0'
			else:
				rc='1'
			if rc in ptr.keys():
				nLen+=base
				ptr=ptr[rc]
			elif c in ptr.keys():
				ptr=ptr[c]
			else:
				return nLen

			base/=2
		return nLen

	def findMaximumXOR(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		binStrs= map(bin,nums)
		binStrs= [ v[2:].zfill(32) for v in binStrs]
		self.buildTrie(binStrs)

		maxV=0
		for s in binStrs:
			maxV=max(maxV,self.findLengthXOR(s))
		return maxV

sol =Solution()

ary= [3, 10, 5, 25, 2, 8]

print sol.findMaximumXOR(ary)
