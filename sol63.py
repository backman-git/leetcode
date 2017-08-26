class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		
		if obstacleGrid[0][0]==1:
			return 0
		
		for y in range(len(obstacleGrid)):
			for x in range(len(obstacleGrid[0])):

				if y ==0 and x ==0 :
					obstacleGrid[y][x]=1

				elif obstacleGrid[y][x] !=1:
					if 0<=x-1 and x-1 < len(obstacleGrid[0]):
						obstacleGrid[y][x]+=obstacleGrid[y][x-1]
					if 0<=y-1 and y-1 < len(obstacleGrid):
						obstacleGrid[y][x]+=obstacleGrid[y-1][x]
				else:
					obstacleGrid[y][x]=0
		return obstacleGrid[-1][-1]