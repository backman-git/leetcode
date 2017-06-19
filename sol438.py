


key points:

	1. use dict to build set.


import collections
class Solution(object):
	def findAnagrams(self, s, p):

		res=[]
		cnt=collections.Counter(p)
		matchN=len(p)
		for idx,c in enumerate(s):
			#front
			if idx-len(p) >=0:
				cnt[s[idx-len(p)]]+=1
				if cnt[s[idx-len(p) ]]>0:
					matchN+=1
			#find pattern       [ X]
			if cnt[c]>0:				
				matchN-=1

			cnt[c]-=1
			if matchN==0:
				res.append(idx-len(p)+1)
		return res

			





sol = Solution()



s="cbaebabacd"
p="abc"
print sol.findAnagrams(s,p)