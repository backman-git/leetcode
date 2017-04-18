
13. Roman to Integer





key point:
	
	roman numerals:
		1.look from left.
		if numerical symbol is less than right symbol substract it!


	後記:
		終於去解決了!   20170417   消防役時期


class Solution(object):



	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		
		romanTlb={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}


		ans=0
		for idx,c in enumerate(s):
			if idx+1 <len(s) and romanTlb[c] < romanTlb[s[idx+1]]:
				ans+= -1*romanTlb[c]
			else:
				ans+=romanTlb[c]

		return ans


sol = Solution()

print  sol.romanToInt("DCXXI")


