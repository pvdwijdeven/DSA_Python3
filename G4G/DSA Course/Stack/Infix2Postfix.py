""""
can all the symbols one by one from left to right in the given Infix Expression.
If the reading symbol is an operand, then immediately append it to the Postfix Expression.
If the reading symbol is left parenthesis ‘( ‘, then Push it onto the Stack.
If the reading symbol is right parenthesis ‘)’, then Pop all the contents of the stack until the respective left parenthesis is popped and append each popped symbol to Postfix Expression.
If the reading symbol is an operator (+, –, *, /), then Push it onto the Stack. However, first, pop the operators which are already on the stack that have higher or equal precedence than the current operator and append them to the postfix. If an open parenthesis is there on top of the stack then push the operator into the stack.
If the input is over, pop all the remaining symbols from the stack and append them to the postfix.

"""


class Solution:
    # Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        # code here
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
                while (
                    len(stack) > 0
                    and stack[-1] != "("
                    and operators[stack[-1]] >= operators[char]
                ):
                    res.append(stack.pop())
                stack.append(char)
        while len(stack) > 0:
            res.append(stack.pop())

        return "".join(res)


sol = Solution()

exp1 = "a+b*(c^d-e)^(f+g*h)-i"
exp2 = "A*(B+C)/D"

res1 = sol.InfixtoPostfix(exp1)
print(res1)
sol1 = "abcd^e-fgh*+^*+i-"
print(res1 == sol1)
res2 = sol.InfixtoPostfix(exp2)
print(res2)
sol2 = "ABC+*D/"
print(res2 == sol2)
