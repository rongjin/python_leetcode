class Solution(object):
	def maxProfit(self,prices):
		l = len(prices)
		if l<=1:
			return 0
		#mat = [[0 for i in range(l)] for i in range(l)]
		best = [0 for i in range(l)]
		best[1] = max(0,prices[1]-prices[0])
		for i in range(2,l):
			if prices[i]>prices[i-1]:
				best[i] = best[i-1]+prices[i]-prices[i-1]
			else:
				best[i] = best[i-1]
		print best
		largest = 0
		for i in best:
			if i>largest:
				largest = i
		return largest


prices = [1,2,3,4,0,5]
print prices
s = Solution()
print s.maxProfit(prices)
