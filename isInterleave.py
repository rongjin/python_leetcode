class Solution(object):
	def isInterleave(self,s1,s2,s3):
		if s1 == "":
			if s2=="" and s3=="":
				return True
			else:
				return False
		elif len(s3)!=len(s1)+len(s2):
			return False
		list1 = [[-1,-1]]
		for i in range(len(s3)):
			list2 = []
			for cur in list1:
				if cur[0]+1<len(s1) and s3[i]==s1[cur[0]+1]:
					add = [cur[0]+1,cur[1]]
					if add not in list2:
						list2.append(add)
				if cur[1]+1<len(s2) and s3[i]==s2[cur[1]+1]:
					add = [cur[0],cur[1]+1]
					if add not in list2:
						list2.append(add)
			if list2 == []:
				return False
			else:
				list1 = list2
		return True

s = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s3 = "aadbbaccc"
print s.isInterleave(s1,s2,s3)
