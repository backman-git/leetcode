class Solution(object):
	def minimumTotal(self, triangle):
		
		if len(triangle)==0:
			return 0
		res = [0]*len(triangle)
		for l in reversed(triangle[1:len(triangle)]):
			res = [ l[i]+res[i] for i in range(len(l))]
			res = [ min(res[i-1],res[i]) for i in range(1,len(l)) ]if len(l)>2 else [res[0]+triangle[0][0]]  

		return res[0]


	   


sol =Solution()

print sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])