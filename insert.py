class Interval(object):
	def __init__(self,s = 0,e=0):
		self.start = s
		self.end = e

class Solution(object):
	def insert(self,intervals,newInterval):
		if len(intervals)==0:
			return [newInterval]
		i = 0
		result = []
		find = 0
		cur = intervals[0]
		while(i<len(intervals)):
			if find==1:
				result.append(intervals[i])
				i+=1
			elif cur.end<newInterval.start:
				result.append(cur)
				i+=1
				if i<len(intervals):
					cur = intervals[i]
			elif newInterval.end<cur.start:
				find = 1
				result.append(newInterval)
			else:
				if cur.start>newInterval.start:
					cur.start = newInterval.start
				if cur.end>=newInterval.end:
					result.append(cur)
					find = 1
					i+=1
				else:
					cur.end = newInterval.end
					find = 1
					i += 1
					while(i<len(intervals) and intervals[i].start<=cur.end):
						i+=1
					cur.end = max(cur.end,intervals[i-1].end)
					result.append(cur)
		if find == 0:
			result.append(newInterval)
		return result
intervallist = [[1,2],[3,5],[6,7],[8,10],[12,16]]
il = []
for i in intervallist:
	il.append(Interval(i[0],i[1]))
s = Solution()
newinterval = Interval(0,0)
il2 = s.insert(il,newinterval)
print "*"*10
for i in il2:
	print i.start,i.end
