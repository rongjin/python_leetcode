import time
class Solution(object):
	def dfs(self,i,visited,mydict):
		#print "dfs",i
		if i in visited and visited[i]==0:
			return 0
		if i not in visited:
			visited[i] = 0
			if i in mydict:
				for j in mydict[i]:
					result = self.dfs(j,visited,mydict)
					if result == 0:
						return 0
			visited[i] = 1
		return 1

	def canFinish(self,numCourses,prerequisites):
		visited = {}
		mydict = {}
		for pair in prerequisites:
			if pair[0] not in mydict:
				mydict[pair[0]] = [pair[1]]
			else:
				mydict[pair[0]].append(pair[1])
		for i in range(numCourses):
			if i not in mydict:
				visited[i] = 1
		for i in range(numCourses):
			if i not in visited:
				result = self.dfs(i,visited,mydict)
				if result == 0:
					return False
		return True


s = Solution()
numCourses = 2
prerequisites = [[0,1],[1,0]]
start_time = time.time()
print s.canFinish(numCourses,prerequisites)
print time.time()-start_time
