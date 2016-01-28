class Solution(object):
	def compute(self,num1,num2,oper):
		if oper == "+":
			return num1+num2
		elif oper == "-":
			return num1-num2
		elif oper == "*":
			return num1*num2
		else:
			if num1*num2<0 and num1%num2!=0:
				return num1/num2+1
			else:
				return num1/num2
	def evalRPN(self,tokens):
		mystack = []
		i = 0
		while(i<len(tokens)):
			if tokens[i] in ["+","-","*","/"]:
				num2 = mystack.pop()
				num1 = mystack.pop()
				num = self.compute(num1,num2,tokens[i])
				print num
				mystack.append(num)
			else:
				mystack.append(int(tokens[i]))
			i+=1
		return mystack[0]

s = Solution()
tokens = ["2","1","+","3","*"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print s.evalRPN(tokens)
