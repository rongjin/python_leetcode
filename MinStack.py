class MinStack(object):
	def __init__(self):
		self.stack = []
		self.mymin = float('Inf')
	
	def push(self,x):
		self.stack.append(x)
		if x<self.mymin:
			self.mymin = x

	def pop(self):
		top = self.stack.pop()
		if top == self.mymin:
			self.mymin = float('Inf')
			for i in self.mystack:
				if i<self.mymin:
					self.mymin = i

	def top(self):
		return self.stack[-1]

	def getMin(self):
		return self.mymin
