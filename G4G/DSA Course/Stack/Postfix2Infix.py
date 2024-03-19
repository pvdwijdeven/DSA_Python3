def postfix_to_infix(postfix) -> str:
	# Code here
	operators = {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2}
	stack = []
	for char in postfix:
		if char not in operators:
			stack.append(char)
		else:
			operand1 = stack.pop()
			operand2 = stack.pop()
			stack.append("(" + operand2 + char + operand1 + ")")
	return stack[-1]


if __name__ == "__main__":
	exp1 = "abcd^e-fgh*+^*+i-"
	res1 = postfix_to_infix(postfix=exp1)
	print(res1)
	exp2 = "ABC+*D/"
	res2 = postfix_to_infix(postfix=exp2)
	print(res2)
