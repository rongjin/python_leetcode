class Solution(object):
	def canFinish(self,numCourses,prerequisites):
		if len(prerequisites)==0:
			return True
		readies = {}
		visited = {}
		table = [[0 for i in range(numCourses)] for j in range(numCourses)]
		for i in range(numCourses):
			readies[i]=0
		for pair in prerequisites:
			pre = pair[1]
			ready = pair[0]
			if table[pre][ready]==0:
				readies[ready]+=1
			table[pre][ready] = 1
		print readies
		queue = []
		for i in range(numCourses):
			if readies[i]==0:
				queue.append(i)
		print queue
		while(queue):
			top = queue.pop(0)
			visited[top]=1
			for j in range(numCourses):
				if table[top][j]!=0:
					readies[j]-=1
					if readies[j]==0:
						queue.append(j)
			print queue
		if len(visited)==numCourses:
			return True
		else:
			return False


s = Solution()
numCourses = 2
prerequisites =[[1,0]]
print s.canFinish(numCourses,prerequisites)
