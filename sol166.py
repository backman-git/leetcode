
166. Fraction to Recurring Decimal



Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".




key points:
	
	1.  case +&+ -&- 0&n n&0 0&0 
	2. hashTlb to store repeat numerator
	3. make sure write clean code



class Solution(object):




	def noReaptPart(self,rPart,repeatPart):
		for idx,v in enumerate(rPart):
			if rPart[idx:] == repeatPart:
				return rPart[:idx]
		return rPart



	def fractionToDecimal(self, numerator, denominator):
		"""
		:type numerator: int
		:type denominator: int
		:rtype: str
		"""
		
		nagNumF=False
		nagDenF=False
	

		# case +&+ -&- 0&n n&0 0&0

		if denominator ==0:
			return None

		if numerator ==0:
			return "0"

		if numerator <0:
			nagNumF =True
			numerator*=-1

		if denominator <0:
			nagDenF = True
			denominator*=-1


		res=""
		rTlb={}

		#  "." left part
		lPart = numerator/denominator
		numerator = numerator%denominator
	
		rPart=[]
		repeatPart=[]
		repeatPoint=None
	
		while numerator !=0:
			

			numerator*=10

			#rTlb store numerator*10

			if numerator not in rTlb:
				
				quotient=numerator/denominator
				remainder=numerator%denominator
				
				rPart.append(quotient)
				rTlb[numerator]=quotient
				numerator=remainder

			else:
				if repeatPoint is None:
					#numerator*10
					repeatPoint=numerator

				elif  repeatPoint == numerator:
						break


				quotient=rTlb[numerator]
				remainder=numerator%denominator
				repeatPart.append(quotient)
				numerator=remainder
				

		if nagNumF != nagDenF :
			res+="-"
		res += ""+str(lPart)
		
		rPart= "".join([str(d) for d in rPart ])
		repeatPart = "".join([str(d) for d in repeatPart])

	
		if rPart !="":
			res+="."
			res+=self.noReaptPart(rPart,repeatPart)

		if repeatPart !="":
			res+="("
			res+=repeatPart
			res+=")"


		return res



			


	
sol=Solution()


print sol.fractionToDecimal(-1,)