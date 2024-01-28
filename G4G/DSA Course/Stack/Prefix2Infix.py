"""
Read the Prefix expression in reverse order (from right to left)
If the symbol is an operand, then push it onto the Stack
If the symbol is an operator, then pop two operands from the Stack 
Create a string by concatenating the two operands and the operator between them. 
string = (operand1 + operator + operand2) 
And push the resultant string back to Stack
Repeat the above steps until the end of Prefix expression.
At the end stack will have only 1 string i.e resultant string
"""


class Solution:
    def preToInfix(self, pre_exp):
        # Code here
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


sol = Solution()

exp1 = "*-A/BC-/AKL"
res1 = sol.preToInfix(exp1)
sol1 = "((A-(B/C))*((A/K)-L))"
print(res1)
print(sol1 == res1)
