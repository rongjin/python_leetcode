class Solution(object):
	def simplifyPath(self,path):
		mylist = path.split("/")
		newlist = []
		newpath = "/"
		print mylist
		for i in mylist:
			if i == "." or i=="":
				continue
			elif i == "..":
				if newlist!=[]:
					newlist.pop()
			else:
				newlist.append(i)
		for i in newlist:
			newpath += i + "/"
		if newpath == "/":
			return newpath
		else:
			return newpath[:-1]


s = Solution()
path = "/a/./b/../../c/"
path = "/../"
path = "/home//foo"
print s.simplifyPath(path)
