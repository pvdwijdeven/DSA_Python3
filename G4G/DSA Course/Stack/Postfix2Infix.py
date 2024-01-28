"""
Algorithm 
Scan all symbols one by one from left to right in the given postfix expression .
If the reading symbol is an operand , push it into the stack .
If the reading symbol is an operator , then 
    a. Pop two expression from the stack , operand1 and operand2 , which is operand for the current operator 
    b. Push “(“ + operand2 + operator + operand1 + “)” into the stack
If there is no symbol left then stop the process . Top of the stack will have the required infix expression .
"""


class Solution:
    def postToInfix(self, postfix):
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


sol = Solution()
exp1 = "abcd^e-fgh*+^*+i-"
res1 = sol.postToInfix(exp1)
sol1 = "((a+(b*(((c^d)-e)^(f+(g*h)))))-i)"
print(res1)
print(res1 == sol1)
exp2 = "ABC+*D/"
res2 = sol.postToInfix(exp2)
sol2 = "((A*(B+C))/D)"
print(res2)
print(res2 == sol2)
