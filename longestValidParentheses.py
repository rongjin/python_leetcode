class Solution(object):
	def longestValidParentheses(self,s):
		mylist = []
		myqueue = []
		for i in range(len(s)):
			if s[i]=='(':
				myqueue.append(i)
				mylist.append(0)
			elif len(myqueue)==0:
				mylist.append(0)
			else:
				top = myqueue.pop()
				mylist[top] = 1
				mylist.append(1)
			print mylist,myqueue
		for i in range(1,len(mylist)):
			if mylist[i] == 1 and mylist[i-1]!=0:
				mylist[i] += mylist[i-1]
		print mylist
		longest = 0
		for i in mylist:
			if i>longest:
				longest = i
		return longest
s = Solution()
mystr = "(((()(()))))"
mystr = ")()())"
print s.longestValidParentheses(mystr)

