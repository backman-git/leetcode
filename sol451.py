


Given a string, sort it in decreasing order based on the frequency of characters.



key points:

	collection.Counter()
	Counter.most_common()	
	[ c*n  for c,n in cnt]












import collections


class Solution(object):
	def frequencySort(self, s):
		"""
		:type s: str
		:rtype: str
		"""

		cnt = collections.Counter(s).most_common()

		res="".join([ c*n  for c,n in cnt])



		return res




sol = Solution()

strs=""
print sol.frequencySort(strs)