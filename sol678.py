class Solution(object):


	def checkValidString(self, s):
	   

		stackL=[]
		stackS=[]

		for idx,c in enumerate(s):
			if c =="(":
				stackL.append(idx)
			elif c ==")":

				if len(stackL)>0 :
					stackL.pop()
				elif len(stackS) >0:
					stackS.pop()
				else:
					return False
			else:
				stackS.append(idx)

		if len(stackL) >0 and len(stackL) <= len(stackS):
			while len(stackL) >0:
				lIdx=stackL.pop()
				sIdx=stackS.pop()
				if lIdx >sIdx:
					return False
			return True
		elif len(stackL) >0 and len(stackL) > len(stackS):
			return False

		else:
			return True



		

sol = Solution()
ary="((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
print sol.checkValidString(ary)