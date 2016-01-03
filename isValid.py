class Solution(object):
	def isValid(self,s):
		mystack = []
		i = 0;
		while(i<len(s)):
			print i,mystack
			if s[i] in "([{":
				mystack.append(s[i])
				i+=1
			else:
				if mystack == []:
					return False
				else:
					top = mystack.pop()
					if ((top=="(" and s[i]==")")or
						(top=="[" and s[i]=="]")or
						(top=="{" and s[i]=="}")):
						i+=1
					else:
						return False
		print mystack
		if mystack==[]:
			return True
		else:
			return False

s = Solution()
mystr = "()[]{}"
print s.isValid(mystr)
