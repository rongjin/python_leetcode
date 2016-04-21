class Stack(object):
	def __init__(self):
		self.mystack = []
		self.mystack2 = []

	def push(self,x):
		self.mystack.append(x)

	def pop(self):
		if self.empty()==1:
			return None
		else:
			while(len(self.mystack)>1):
				self.mystack2.append(self.mystack.pop(0))
			result = self.mystack.pop(0)
			while(len(self.mystack2)>0):
				self.mystack.append(self.mystack2.pop(0))
			return result

	def top(self):
		if self.empty()==1:
			return None
		return self.mystack[len(self.mystack)-1]
	def empty(self):
		return len(self.mystack)==0

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print s.pop()
s.push(4)
print s.pop()
print s.pop()
print s.pop()



