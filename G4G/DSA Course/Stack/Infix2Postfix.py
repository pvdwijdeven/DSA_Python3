# Function to convert an infix expression to a postfix expression.
def infix_to_postfix(exp) -> str | None:
	res = []
	stack = []
	operators = {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2}
	for char in exp:
		if char not in operators and char not in ["(", ")"]:
			res.append(char)
		elif char == "(":
			stack.append(char)
		elif char == ")":
			while True:
				popped = stack.pop()
				if popped == "(":
					break
				res.append(popped)
		else:
			while (len(stack) > 0 and stack[-1] != "("
			       and operators[stack[-1]] >= operators[char]):
				res.append(stack.pop())
			stack.append(char)
	while len(stack) > 0:
		res.append(stack.pop())
		return "".join(res)


if __name__ == "__main__":
	exp1 = "a+b*(c^d-e)^(f+g*h)-i"
	res1 = infix_to_postfix(exp=exp1)
	print(res1)
	exp2 = "A*(B+C)/D"
	res2 = infix_to_postfix(exp=exp2)
	print(res2)
