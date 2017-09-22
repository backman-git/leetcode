

import operator


class Solution(object):


    def islandPerimeter(self, grid):

    	gridRC = grid + map(list,zip(*grid))

    	res=0
    	for r in gridRC:
    		res+=sum(map(operator.ne,[0]+r,r+[0]))

    	return res





sol =Solution()

m = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
print sol.islandPerimeter(m)







