class TrieNode(object):
	def __init__(self):
		self.word = False
		self.children = {}

class WordDictionary(object):
	def __init__(self):
		self.root = TrieNode()

	def addWord(self,word):
		node = self.root
		for i in word:
			if i not in node.children:
				node.children[i] = TrieNode()
			node = node.children[i]
		node.word = True
	
	def find(self,node,word):
		print word
		if len(word)==1:
			if word==".":
				for i in node.children:
					if node.children[i].word == True:
						return True
				return False
			else:
				if word in node.children and node.children[word].word==True:
					return True
				else:
					return False
		else:
			if word[0]!=".":
				if word[0] not in node.children:
					return False
				else:
					return self.find(node.children[word[0]],word[1:])
			else:
				for i in node.children:
					result = self.find(node.children[i],word[1:])
					if result == True:
						return True
				return False



	def search(self,word):
		node = self.root
		result = self.find(node,word)
		return result


wd = WordDictionary()
wd.addWord("word")
print wd.search("worda")
