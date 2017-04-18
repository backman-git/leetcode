


7. Reverse Integer

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321


key point:

    1. string : 
        a="abc"
        a[::-1] ==> "cba" 
        a.replace("-","" )  '-' -> ''
    2.  1<<31    2^32     11111111111111111111111111111



#string manipuation
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x=str(x)
        
        
        if(x[0]=='-'):
            a=int(x.replace("-","")[::-1])*(-1)
            if a >2147483647 or a<-2147483647:     
                return 0 
            else:
                return a
            
        else :
            a=int( x[::-1])
            if a >2147483647 or a<-2147483647:     
                return 0 
            else:
                return a


#math 

class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        if n == 0:
            return 0
            
        neg = 1
        if n < 0:
            neg, n = -1, -n
        
        reverse = 0

        #一位一位移
        while n > 0:
            reverse = reverse * 10 + n % 10
            n = n / 10
        
        reverse = reverse * neg
        if reverse < -(1 << 31) or reverse > (1 << 31) - 1:
            return 0
        return reverse