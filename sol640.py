class Solution(object):
	def solveEquation(self, equation):
		"""
		:type equation: str
		:rtype: str
		"""

		xC=0
		v=0

		side=False

		for idx,c in enumerate (equation):

			if c=="=":
				side=True

			if c =='x':
				#find value
				nStr=""
				nPtr=idx-1

				if nPtr>=0 and  equation[nPtr].isdigit():
					while nPtr>=0 and equation[nPtr].isdigit():
						nStr+=equation[nPtr]
						nPtr-=1 

						

						xC+=int("".join(reversed(nStr)))
				else:
					xC+=1

			if c=="-" or c=="+":
				nPtr=idx+1
				while nPtr<len(equation) and equation[nPtr].isdigit():
					nStr+=equation[nPtr]
					nPtr-=1 
					n=int(nStr)
				v = n if c=="+" else -1*n

		print xC,v


sol=Solution()

sol.solveEquation("x+5-3+x=6+x-2")
				