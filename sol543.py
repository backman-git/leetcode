class Solution(object):
	def detectCapitalUse(self, word):
		"""
		:type word: str
		:rtype: bool
		"""

	   
		allCaptialF=True
		notFirstCapitalF=False

		for idx in range(len(word)):

			isupper=word[idx].isupper()

			if isupper is False:
				allCaptialF=False

			if idx!=0 and isupper is True:
				notFirstCapitalF=True



		if allCaptialF is True or notFirstCapitalF is False:
			return True

		else:
			return False








sol =Solution()

s="FlAg"
print sol.detectCapitalUse(s)