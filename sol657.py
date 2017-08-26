
import collections

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        cnt=collections.Counter(moves)

        return True if (cnt['U']==cnt['D'] and cnt['L']==cnt['R'] ) else False

        


sol = Solution()

ary = "LL"
print sol.judgeCircle(ary)