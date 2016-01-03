class Solution(object):
	def getPermutation(self,n,k):
		if n==1 and k==1:
			return "1"
		result = ""
		mylist = [1,2,3,4,5,6,7,8,9]
		k-=1
		total = 1
		for i in range(n-1):
			total *= (i+1)
		for i in range(n):
			if i == n-2:
				result += str(mylist[k])
				del mylist[k]
			elif i == n-1:
				result += str(mylist[0])
			else:
				cur = k/total
				result += str(mylist[cur])
				del mylist[cur]
				k -= cur*total
				total/= (n-1-i)
		return result

s = Solution()
print s.getPermutation(2,2)


