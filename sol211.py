class WordDictionary(object):
	
	def __init__(self):
		self.tri={}

	def addWord(self, word):
		ptr =self.tri
		for c in word:
			if c not in ptr.keys():
				ptr[c]={"status":False}
			ptr=ptr[c]
		ptr['status']=True

	def recurSearch(self,word,d):
		if word=="":
			return d['status']
		if word[0]=='.':
			return any(self.recurSearch(word[1:],d[k]) for k in d.keys() if k!="status")
		elif word[0] in d.keys():
			return self.recurSearch(word[1:],d[word[0]])
		else:
			return False

	def search(self, word):
		if word=="":
			return True
		return self.recurSearch(word,self.tri)
		









# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


obj = WordDictionary()
obj.addWord("backman")
obj.addWord("backmen")
print obj.search("backmen")
print obj.search("xci")