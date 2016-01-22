class Solution(object):
	def canCompleteCircuit(self,gas,cost):
		if sum(gas)<sum(cost):
			return -1
		mylist = [gas[0]-cost[0]]
		for i in range(1,len(gas)):
			mylist.append(mylist[-1]+gas[i]-cost[i])
		print mylist
		mymin = 10000
		for i in range(len(mylist)):
			if mylist[i]<mymin:
				mymin = mylist[i]
				result = i
		if result+1 == len(gas):
			return 0
		else:
			return result+1

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
s = Solution()
print s.canCompleteCircuit(gas,cost)
