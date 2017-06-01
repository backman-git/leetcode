344. Reverse String




Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

Subscribe to see which companies asked this question.


key points:

	join function()




class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        return "".join([s[i] for i in range(len(s)-1,-1,-1)   ])