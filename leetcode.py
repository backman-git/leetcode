


def gcd(a,b):

	if a < b:
		return gcd(b,a)
	elif b==1:
		return 1
	elif b ==0:
		return 0
	else:
		return gcd(b,a%b)



def isDivider(n,d):

	if d==0:
		return True
	if n==0:
		return False
	

	if d ==1:
		return True
	elif n%d==0:
		return True
	else:
		return False





class Solution(object):
	def canMeasureWater(self, x, y, z):
		"""
		:type x: int
		:type y: int
		:type z: int
		:rtype: bool
		"""

		if x ==0 and y==0 and z==0:
			return True
		elif x==0 and y==0 and z!=0:
			return False

		print gcd(x,y)

		return isDivider(z,gcd(x,y))

sol = Solution()

print sol.canMeasureWater(1,0,0)


