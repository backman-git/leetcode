class Solution(object):

	# b in a
	def formable(self,a,b):

		a=sorted(a)
		b=sorted(b)


	
		ptr1=0
		ptr2=0

		while(ptr1 < len(a) and ptr2<len(b) ):

			if a[ptr1]==b[ptr2]:
				ptr2+=1
				ptr1+=1
			else:
				ptr1+=1


		if ptr2 == len(b):
			return True
		else:
			return False







	def findLongestWord(self, s, d):
		"""
		:type s: str
		:type d: List[str]
		:rtype: str
		"""

		if s=="":
			return ""

		if len(d)==0:
			return ""

		d=sorted(d,key=lambda x:(-len(x),x) )

		

		for subS in d:
			if self.formable(s,subS):
				return subS

		return ""





sol =Solution()
s = "abpcplea"
d = ["a","v","c","dd"]

print sol.findLongestWord(s,d)

"aewfafwafjlwajflwajflwafj"
["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]

print sol.formable("aewfafwafjlwajflwajflwafj","awefawfwaf")