class Solution(object):
	def groupAnagrams(self,strs):
		mylist = []
		mydict = {}
		for i in strs:
			word = ''.join(sorted(i))
			if mylist == []:
				mydict[word]= len(mylist)
				mylist.append([i])
			else:
				if word in mydict:
					mylist[mydict[word]].append(i)
				else:
					mydict[word] = len(mylist)
					mylist.append([i])
		result = []
		for i in mylist:
			result.append(sorted(i))
		for i in result:
			print i
		return result

s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
s.groupAnagrams(strs)

