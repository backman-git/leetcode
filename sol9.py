

9. Palindrome Number


Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Subscribe to see which companies asked this question.



key point:



	





#math 
class Solution(object):
	
	def reverseN(self,n):

		res =0

		while n!=0:
			res = res*10+n%10
			n/=10
		return res

	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		if(x<0):
			return False

		if self.reverseN(x) == x:
			return True
		else:
			return False


#string way
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        
        return str(x)[::-1]==str(x) 
        