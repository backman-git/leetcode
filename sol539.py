class Solution(object):
	def findMinDifference(self, timePoints):
		minsList = map(self.mins,timePoints)
		minsList.sort()
		diffList= [ min(abs(minsList[i]-minsList[i+1]) , 24*60-abs(minsList[i]-minsList[i+1]) ) if i!=len(minsList)-1 else  min(abs(minsList[i]-minsList[0]) , 24*60-abs(minsList[i]-minsList[0]) )   for i in range(len(minsList)) ]
		print diffList
		return min(diffList)

	def mins(self,strs):
		h,m=strs.split(":")
		return int(h)*60+int(m)
		


sol = Solution()

print sol.findMinDifference(["12:34","01:02","21:43"])