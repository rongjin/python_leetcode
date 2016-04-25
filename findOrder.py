import time
class Solution(object):
	def dfs(self,i,visited,mydict,order):
		print "dfs",i
		if i in visited and visited[i]==0:
			return 0
		if i not in visited:
			visited[i] = 0
			if i in mydict:
				for j in mydict[i]:
					result = self.dfs(j,visited,mydict,order)
					if result == 0:
						return 0
			order.append(i)
			print order
			visited[i] = 1
		return 1

	def findOrder(self,numCourses,prerequisites):
		visited = {}
		mydict = {}
		for pair in prerequisites:
			print pair
			if pair[0] not in mydict:
				mydict[pair[0]] = [pair[1]]
			else:
				mydict[pair[0]].append(pair[1])
		print mydict
		order = []
		for i in range(numCourses):
			if i not in mydict:
				order.append(i)
				visited[i] = 1
		for i in range(numCourses):
			if i not in visited:
				result = self.dfs(i,visited,mydict,order)
				if result == 0:
					return []
		return order


s = Solution()
numCourses = 3
prerequisites = [[0,1],[0,2],[1,2]]
start_time = time.time()
print s.findOrder(numCourses,prerequisites)
print time.time()-start_time
