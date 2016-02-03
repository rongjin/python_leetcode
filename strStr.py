class Solution(object):
	def strStr(self,haystack,needle):
		if needle == "":
			return 0
		result = -1
		for i in range(len(haystack)-len(needle)+1):
			find = 1
			for j in range(len(needle)):
				if haystack[i+j]!=needle[j]:
					find = 0
					break
			if find == 1:
				return i
		return result

haystack = "aabbbaa"
needle = "bbb"
s = Solution()
print s.strStr(haystack,needle)
