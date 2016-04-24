class Queue(object):
	def __init__(self):
		self.stack = []
		self.stack2 = []
	
	def push(self,x):
		self.stack.append(x)

	def pop(self):
		if self.empty():
			return None
		while(len(self.stack)>1):
			self.stack2.append(self.stack.pop())
		cur = self.stack.pop()
		while(len(self.stack2)>0):
			self.stack.append(self.stack2.pop())
		return cur

	def peek(self):
		if self.empty():
			return None
		while(len(self.stack)>1):
			self.stack2.append(self.stack.pop())
		cur = self.stack.pop()
		self.stack.append(cur)
		while(len(self.stack2)>0):
			self.stack.append(self.stack2.pop())
		return cur

	def empty(self):
		return len(self.stack)==0

q = Queue()
q.push(1)
q.push(2)
print q.pop()
print q.peek()


