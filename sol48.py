




class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        self.dim=len(matrix)

        #transpose
        for i in range(self.dim):
        	for j in range(i,self.dim):
        		matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for r in matrix:
        	r.reverse()


sol =Solution()





mat =[[1,2,3,4],
	  [5,6,7,8],
	  [9,10,11,12],
	  [13,14,15,16]]

sol.rotate(mat)
for r in mat:
	print r
