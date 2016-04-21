class Solution(object):
	def inter(self,A,B,C,D,E,F,G,H):
		if C<E:
			return 0
		if G<A:
			return 0
		if H<B:
			return 0
		if D<F:
			return 0
		w = min(C,G)-max(A,E)
		h = min(D,H)-max(B,F)
		return w*h

	def computeArea(self,A,B,C,D,E,F,G,H):
		intersect = self.inter(A,B,C,D,E,F,G,H)
		s1 = (C-A)*(D-B)
		s2 = (G-E)*(H-F)
		return s1+s2-intersect

s = Solution()
print s.computeArea(-3,0,3,4,0,-1,9,2)
print s.computeArea(0,0,0,0,-1,-1,1,1)

