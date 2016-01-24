class UndirectedGraphNode(object):
	def __init__(self,x):
		self.label = x
		self.neighbors = []

class Solution(object):
	def cloneGraph(self, node):
		if node == None:
			return None
		myqueue = []
		visited = {}
		newnode = UndirectedGraphNode(node.label)
		visited[node] = newnode
		myqueue.append(node)
		while(myqueue!=[]):
			top = myqueue.pop(0)
			print top.label
			for neighbor in top.neighbors:
				print "n",neighbor.label
				if neighbor not in visited:
					p = UndirectedGraphNode(neighbor.label)
					myqueue.append(neighbor)
					visited[neighbor]=p
				visited[top].neighbors.append(visited[neighbor])
		print "^"*10
		for i in visited:
			print i.label
			for j in i.neighbors:
				print j.label,
			print
		return newnode

s = Solution()
mylist = []
for i in range(3):
	mylist.append(UndirectedGraphNode(i+1))
mylist[0].neighbors.append(mylist[1])
mylist[0].neighbors.append(mylist[2])
mylist[1].neighbors.append(mylist[0])
mylist[1].neighbors.append(mylist[2])
mylist[2].neighbors.append(mylist[2])
s.cloneGraph(mylist[0])


