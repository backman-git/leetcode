

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.



key points:


	hash Table 






class Solution(object):
	def findWords(self, words):
		"""
		:type words: List[str]
		:rtype: List[str]
		"""

		if words == []:
			return []



		self.keyTable={"q":1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,'p':1,
				  "a":2,'s':2,'d':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,
				  'z':3,'x':3,'c':3,'v':3,'b':3,'n':3,'m':3}


		res=[]
		for word in words:

			if self.check(word.lower()) is True:
				res.append(word)
		return res


	def check(self,word):

		row=self.keyTable[word[0]]
		for c in word:
			if self.keyTable[c] != row:
				return False
		return True

