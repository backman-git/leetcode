

class Solution(object):

	def __init__(self):

		self.picW=0
		self.picH=0

	def inbound(self,x,y):

		if 0<=x and x<self.picW and 0<=y and y <self.picH:
			return True
		else:
			return False


	def lonePixel(self,pic,x,y):
		if (self.inbound(x,y+1) is False or pic[y+1][x] == "W"  ) and(self.inbound(x+1,y) is False or pic[y][x+1] == "W" ):
			return True
		else:
			return False 


	def drawW(self,pic,x,y):


		if self.inbound(x,y) is False or pic[y][x]=="W":
			return
		else:
			pic[y][x]="W"
			self.drawW(pic,x-1,y)
			self.drawW(pic,x,y+1)
			self.drawW(pic,x+1,y)
			


	def findLonelyPixel(self, picture):
		"""
		:type picture: List[List[str]]
		:rtype: int
		"""

		self.picH=len(picture)
		self.picW=len(picture[0])

		result=0
		for  y in range(self.picH):
			for x in range(self.picW):
				if picture[y][x]=="B" and self.lonePixel(picture,x,y):
					result+=1
					

				else:
					self.drawW(picture,x,y)



		return result



sol = Solution()


pic=[['W','W','B'],
	 ['W','B','W'],
	 ['B','W','W']]

'''

BWB
WBW
BWW




'''



print sol.findLonelyPixel(pic)

