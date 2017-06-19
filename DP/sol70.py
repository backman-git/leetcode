
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Subscribe to see which companies asked this question.






class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        ways=[1,2];
        
        for i in range(2,n):
            ways.append(ways[i-1]+ways[i-2])
         
        return ways[n-1]
        