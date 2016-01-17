class Solution(object):
	def maxProfit(self,prices):
		largest = 0
		if len(prices)<=1:
			return 0
		best = [0 for i in range(len(prices))]
		best[1] = max(0,prices[1]-prices[0])
		for i in range(2,len(prices)):
			best[i] = max(0,best[i-1]+prices[i]-prices[i-1])
		for i in range(1,len(best)):
			if best[i]>largest:
				largest = best[i]
		return largest

prices = [2,1,5,0]
s = Solution()
print s.maxProfit(prices)
