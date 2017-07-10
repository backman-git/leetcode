class Solution(object):
	
	def __init__(self):

		self.dLen=0
		self.count=0
	def genExtension(self,sDigit):

		if len(sDigit) == self.dLen:
			return
		
		for i in range(10):
			
			yield sDigit+str(i)

	def removeLead(self,sDigit):

		for idx in range(len(sDigit)):
			if sDigit[idx] is not "0":
				return sDigit[idx:]
		return "0"

	def reject(self,sDigit):

		if len(sDigit) == self.dLen:

			sDigit= self.removeLead(sDigit)
		


			if sDigit == "0":
				return False

			bTable=[False]*10
			for d in sDigit:
				if bTable[int(d)] is False:
					bTable[int(d)] = True
				else:
					return True
		return False

	def accept(self,sDigit):

		if len(sDigit) == self.dLen:
			return True
		return False


	def BT(self,sDigit):

		if self.reject(sDigit) is True:
			return 

		if self.accept(sDigit) is True:
			self.count+=1


		
		for ext in self.genExtension(sDigit):
			self.BT(ext)

	def countNumbersWithUniqueDigits(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		self.dLen=n
		self.count=0

		self.BT("")

		return self.count



sol=Solution()

for i in range(1,7):
	print sol.countNumbersWithUniqueDigits(i)
