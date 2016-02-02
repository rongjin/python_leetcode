class LRUCache(object):
	def __init__(self,capacity):
		self.mydict = {}
		self.myorder = []
		self.capacity = capacity

	def get(self,key):
		if key in self.mydict:
			self.myorder.remove(key)
			self.myorder.append(key)
			return self.mydict[key]
		else:
			return -1
	
	def set(self, key,value):
		if key in self.mydict:
			self.myorder.remove(key)
		if self.capacity == len(self.myorder):
			top = self.myorder.pop(0)
			del self.mydict[top]
		self.myorder.append(key)
		self.mydict[key] = value

s = LRUCache(2)
s.set(1,1)
s.set(2,2)
print s.myorder,s.mydict
s.set(3,3)
print s.myorder,s.mydict
s.set(1,1)
print s.myorder,s.mydict

