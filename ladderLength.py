class Solution(object):
	def check(self,word1,word2):
		if len(word1)!=len(word2):
			return False
		count = 0
		for i in range(len(word1)):
			if word1[i]!=word2[i]:
				count +=1
			if count>1:
				return False
		if count == 0:
			return False
		return True

	def ladderLength(self,beginWord, endWord,wordList):
		visited = {beginWord:1,endWord:1}
		beginset = {beginWord:1}
		endset = {endWord:1}
		while True:
			#check begin set can reach end set
			for key in beginset:
				for key2 in endset:
					if self.check(key,key2):
						return beginset[key]+endset[key2]
			if len(beginset)>len(endset):
				temp = endset
				endset = beginset
				beginset = temp
			#beginset is the smaller one
			#update beginset
			newbeginset = {}
			for word in beginset:
				for i in range(len(word)):
					for j in "abcdefghijklmnopqrstuvwxyz":
						tmp = word[:i]+j+word[i+1:]
						if tmp not in visited and tmp in wordList:
							newbeginset[tmp]=beginset[word]+1
							visited[tmp]=1
			beginset = newbeginset
			if len(beginset)==0:
				return 0
			print beginset

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
s = Solution()
print s.ladderLength(beginWord,endWord,wordList)
