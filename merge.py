class Interval(object):
	def __init__(self,s = 0,e=0):
		self.start = s
		self.end = e

class Solution(object):
	def merge(self,intervals):
		if len(intervals)<2:
			return intervals
		intervals.sort(key = lambda x:x.start)
		start1 = intervals[0].start
		end1 = intervals[0].end
		i = 1
		result = []
		while(i<len(intervals)):
			if intervals[i].end<=end1:
				i+=1
			elif intervals[i].start>end1:
				result.append(Interval(start1,end1))
				start1 = intervals[i].start
				end1 = intervals[i].end
				i+=1
			else:
				end1 = intervals[i].end
				i+=1
		result.append(Interval(start1,end1))
		return result

intervallist = [[2,6],[1,6],[8,10],[15,18]]
il = []
for i in intervallist:
	il.append(Interval(i[0],i[1]))
s = Solution()
il2 = s.merge(il)
for i in il2:
	print i.start,i.end
