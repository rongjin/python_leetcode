class Solution(object):
	def merge(self, nums1, m,nums2, n):
		i = m-1
		j = n-1
		k = m+n-1
		while(k>=0):
			if i<0:
				nums1[k] = nums2[j]
				j-=1
			elif j<0:
				nums1[k] = nums1[i]
				i-=1
			elif nums1[i]>=nums2[j]:
				nums1[k] = nums1[i]
				i-=1
			else:
				nums1[k] = nums2[j]
				j-=1
			k-=1

num1 = [1,3,5,7,0,0,0]
num2 =[2,4,6]
s = Solution()
s.merge(num1,4,num2,3)
print num1
