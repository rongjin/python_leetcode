class Solution(object):
	def compareVersion(self,version1,version2):
		vlist1 = version1.split(".")
		vlist2 = version2.split(".")
		print vlist1
		print vlist2
		i = 0;
		j = 0;
		while(i<len(vlist1) or j<len(vlist2)):
			if(i>=len(vlist1)):
				v1 = 0
				v2 = int(vlist2[j])
			elif(j>=len(vlist2)):
				v2 = 0
				v1 = int(vlist1[i])
			else:
				v1 = int(vlist1[i])
				v2 = int(vlist2[j])
			if v1<v2:
				return -1
			elif v1>v2:
				return 1
			else:
				i+=1
				j+=1
		return 0

s = Solution()
version1 = "0.1.1"
version2 = "0.1"
print s.compareVersion(version1,version2)
