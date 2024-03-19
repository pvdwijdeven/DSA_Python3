def preToInfix(pre_exp) -> str:
	operators = {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2}
	stack = []
	for char in pre_exp[::-1]:
		if char not in operators:
			stack.append(char)
		else:
			operand1 = stack.pop()
			operand2 = stack.pop()
			stack.append("(" + operand1 + char + operand2 + ")")
	return stack[-1]


if __name__ == "__main__":
	exp1 = "*-A/BC-/AKL"
	res1 = preToInfix(pre_exp=exp1)
	print(res1)
