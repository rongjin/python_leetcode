class Solution(object):
	def multiply(self,num1,num2):
		print num1,num2
		l1 = len(num1)
		l2 = len(num2)
		result = []
		for i in range(l1+l2):
			result.append(0)
		for i in range(l1):
			for j in range(l2):
				mul = int(num1[l1-1-i])*int(num2[l2-1-j])
				result[i+j] += mul%10
				result[i+j+1] += mul/10
				print result
		mynum = ""
		temp = 0
		num = 0
		for i in range(l1+l2):
			num = result[i]+temp
			mynum = str((num)%10)+mynum
			temp = num/10
		i = 0;
		while(i<len(mynum)-1 and mynum[i]=="0"):
			i+=1
		return mynum[i:]

num1 = "91"
num2 = "91"
s = Solution()
print s.multiply(num1,num2)
print
