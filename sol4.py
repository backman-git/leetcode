





class Solution(object):
	def readBinaryWatch(self, num):
		"""
		:type num: int
		:rtype: List[str]
		"""
		
		result =[]
		for digits in range(1024):
			
			if bin(digits).count("1") == num:
				h,m=digits>>6,digits&0x3f
				

				if h <12 and m <60:
					result.append("%d:%02d"%(h,m))

		return result





sol =Solution()

print sol.readBinaryWatch(1)