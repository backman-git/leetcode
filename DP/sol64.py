
64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Subscribe to see which companies asked this question.







class Solution(object):
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		

		for x in range(0,len(grid[0])):
			for y in range(0,len(grid)):

				if x-1>=0 and y-1>=0:
					grid[y][x]+=min(grid[y][x-1],grid[y-1][x])
				elif x-1<0 and y-1>=0:
					grid[y][x]+=grid[y-1][x]
				elif x-1>=0 and y-1<0:
					grid[y][x]+=grid[y][x-1]

		return grid [len(grid)-1][len(grid[0])-1]