class Solution(object):
	def help(self,num,den):
		result = ""
		mydict = {}
		k = 0
		while(num!=0):
			div = num*10/den,num*10%den
			if div[1]==0:
				result += str(div[0])
				return result
			else:
				print mydict,num
				if num in mydict:
					result2 = result[:mydict[num]]
					result2 += "("+result[mydict[num]:]+")"
					result = result2
					return result
				else:
					mydict[num] = k
					result += str(div[0])
					num = div[1]
			print result
			k+=1
		result += str(div[0])
		return result

	def fractionToDecimal(self,numerator,denominator):
		result = ""
		if numerator*denominator<0:
			pos = -1
		else:
			pos = 1
		num = abs(numerator)
		den = abs(denominator)
		div = num/den,num%den
		if div[1]==0:
			return str(pos*num/den)
		else:
			result=str(div[0])+"."
			result += self.help(div[1],den)
			if pos==-1:
				result = "-"+result
			return result

s = Solution()
num = -50
den = 8
print s.fractionToDecimal(num,den)
