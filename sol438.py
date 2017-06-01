class Solution(object):


	def isAnagrams(self,s):
		
		hTlb={}

		for c in self.anagrams:
			if c in hTlb:
				hTlb[c]+=1
			else:
				hTlb[c]=1
		


		for c in s:
			if c not in hTlb or  hTlb[c] == 0:
				return False
			else:
				hTlb[c]-=1
		return True


	def findAnagrams(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: List[int]
		"""
		self.anagrams=p
		self.lAnagrams=len(p)


		# find first
		fIdx=None
		for idx in range(len(s)-self.lAnagrams+1):
			if self.isAnagrams(s[idx:idx+self.lAnagrams-1]):
				fIdx=idx
				break

		if fIdx is None:
			return []


		hTlb={c:0 for c in p}
		res=[fIdx]

		ptrS=fIdx+1
		ptrE=ptrS+self.lAnagrams-1

		while ptrE < len(s):
			if s[ptrS-1] in hTlb:
				hTlb[s[ptrS-1]]+=1

			if s[ptrE] in hTlb:
				hTlb[s[ptrE]]-=1
				ansF=True
				print "case2: "
				print ptrS,ptrE
				print hTlb
				for k,val in  hTlb.items():
					if val != 0:
						ansF=False
						break
				if ansF is True:
					res.append(ptrS)
				ptrE+=1
				ptrS+=1

			else:
				print "case 3"
				print ptrS,ptrE
				ptrS=ptrE+1
				hTlb={}

				for c in self.anagrams:
					if c in hTlb:
						hTlb[c]+=1
					else:
						hTlb[c]=1
				
				ptrE=ptrS+self.lAnagrams-1
				



			




		return res



sol = Solution()



s="abcxabc"
p="abc"
print sol.findAnagrams(s,p)