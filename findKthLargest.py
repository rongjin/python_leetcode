import heapq
class Solution(object):
	def findKthLargest(self, nums, k):
		minheap = []
		for i in nums:
			if(len(minheap)<k):
				heapq.heappush(minheap,i)
			else:
				if i> minheap[0]:
					heapq.heappop(minheap)
					heapq.heappush(minheap,i)
		return minheap[0]

s = Solution()
nums = [3,2,1,5,6,4]
print s.findKthLargest(nums,3)
