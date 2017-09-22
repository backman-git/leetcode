class Solution(object):
		
	def __init__(self):
		self.visitTable=[]



	def island(self,(x,y)):

		if 0<=x and x < len(self.grid[0]) and 0<=y and y < len(self.grid) and self.grid[y][x]=="1": 
				self.grid[y][x]='0'
				dirs=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
				map(self.island,dirs)
			
				return 1
		return 0


	def numIslands(self,grid):
		
		if grid ==[]:
			return 0
		self.grid=map(list,grid)
		ans=0
		
		return sum([self.island((x,y)) for y in range(0,len(grid)) for x in range(0,len(grid[0])) ])

sol = Solution()

print sol.numIslands(["10111","10101","11101"])
		