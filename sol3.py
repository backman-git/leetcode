3. Longest Substring Without Repeating Characters Add to List
DescriptionHintsSubmissionsSolutions
Total Accepted: 279607
Total Submissions: 1161001
Difficulty: Medium
Contributor: LeetCode
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Subscribe to see which companies asked this question.




'''
	看錯題目，想法錯誤解了個更難的想法。
	其實題目很簡單，解題時務必要專心跟最好狀態，看來還需多練練。

'''



key points:


	1. hash table!





class Solution(object):



	def findRepeat(self,sIdx,cList):

		
		useTlb={}
		res=0
		for c in cList[sIdx:]:
			if c not in useTlb:
				useTlb[c]=True
				res+=1
			else:
				break

		
		return res



	def lengthOfLongestSubstring(self, s):
		
		maxV=0
		
		for idx , c in enumerate(s):
			print idx,self.findRepeat(idx,s)
			maxV = max(maxV,self.findRepeat(idx,s))



		return maxV



sol = Solution()

print sol.lengthOfLongestSubstring("pwwkew")