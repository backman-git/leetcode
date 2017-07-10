


#trie

class tNode(object):

	def __init__(self):
		self.childs= {}
		self.isWord= False





class Trie(object):


	def __init__(self):
		self.root = tNode()



	def insert(self,word):

		ptr = self.root
		for c in word:

			child = ptr.childs.get(c,None)
			if child is None:
				 child= tNode()
				 ptr.childs[c]=child

			ptr=child
		ptr.isWord = True



	def search(self,word):

		ptr= self.root

		for c in word:
			ptr = ptr.childs.get(c,None)
			if ptr is None :
				return False
		return ptr.isWord

	def startWith(self,pre):

		ptr= self.root

		for c in pre:
			ptr = ptr.childs.get(c,None)
			if ptr is None :
				return False
		return True



tree = Trie()

tree.insert("hello")
print tree.startWith("helloo")







