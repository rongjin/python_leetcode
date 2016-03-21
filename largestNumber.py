class Solution:
	def cmp(self,num1,num2):
		l1 = int(str(num1)+str(num2))
		l2 = int(str(num2)+str(num1))
		if l1>l2:
			return 1
		elif l1<l2:
			return -1
		else:
			return 0
		
	def merge(self,num1,num2):
		result = []
		l1 = 0
		l2 = 0
		while(l1<len(num1) or l2<len(num2)):
			if l1==len(num1):
				result.append(num2[l2])
				l2 += 1
			elif l2==len(num2):
				result.append(num1[l1])
				l1 += 1
			else:
				if self.cmp(num1[l1],num2[l2])>=0:
					result.append(num1[l1])
					l1+=1
				else:
					result.append(num2[l2])
					l2+=1
		return result

	def sort(self,nums):
		if len(nums)==1:
			return nums
		elif len(nums)==2:
			if self.cmp(nums[0],nums[1])>=1:
				return [nums[0],nums[1]]
			else:
				return [nums[1],nums[0]]
		else:
			mid = len(nums)/2
			l1 = self.sort(nums[:mid])
			l2 = self.sort(nums[mid:])
			l3 = self.merge(l1,l2)
			return l3
	def largestNumber(self,nums):
		nums = self.sort(nums)
		result = ""
		for i in nums:
			result += str(i)
		return result

s = Solution()
nums = [3,30,34,5,9]
print s.largestNumber(nums)
