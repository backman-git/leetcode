import math
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        return int(n%2 + math.floor(math.pow(n,0.5))*2   )


sol = Solution()
print  sol.minSteps(3)