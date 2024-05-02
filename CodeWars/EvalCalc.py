import codewars_test as test

def precedence(op):

    if op == "+" or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2
    return 0

    # Function to perform arithmetic
    # operations.


def applyOp(a, b, op):

    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b

    # Function that returns value of
    # expression after evaluation.


def calc(expression):
    expression = expression.replace("+ -(", "+ {")
    expression = expression.replace("- -(", "- {")
    expression = expression.replace("/ -(", "/ {")
    expression = expression.replace("* -(", "* {")
    expression = expression.replace(" -(", " - (")
    expression = expression.replace("(-(", "({")
    if len(expression)>1:
        if expression[:2] == "-(":
            expression = "{" + expression[2:]

    # stack to store integer values.
    values = []

    # stack to store operators.
    ops = []
    i = 0
    prev_token = True
    while i < len(expression):

        minus: bool = False
        if expression[i] == "-" and i < len(expression) - 1:
            if expression[i + 1].isdigit() and prev_token:
                minus = True
                i += 1

        # Current token is a whitespace,
        # skip it.
        if expression[i] == " ":
            i += 1
            continue

        # Current token is an opening
        # brace, push it to 'ops'
        elif expression[i] == "(" or expression[i] == "{":
            ops.append(expression[i])
            prev_token = True
        # Current token is a number, push
        # it to stack for numbers.
        elif expression[i].isdigit():
            val = 0
            prev_token = False
            # There may be more than one
            # digits in the number.
            while i < len(expression) and expression[i].isdigit():

                val = (val * 10) + int(expression[i])
                i += 1
            if minus:
                val *= -1
            values.append(val)
            minus = False

            # right now the i points to
            # the character next to the digit,
            # since the for loop also increases
            # the i, we would skip one
            #  token position; we need to
            # decrease the value of i by 1 to
            # correct the offset.
            i -= 1

        # Closing brace encountered,
        # solve entire brace.
        elif expression[i] == ")":
            prev_token = False
            while len(ops) != 0 and ops[-1] != "(" and ops[-1] != "{":

                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(applyOp(val1, val2, op))

            # pop opening brace.
            tmp =ops.pop()
            if tmp == "{":
                values[-1] *= -1

        # Current token is an operator.
        else:
            prev_token = True
            # While top of 'ops' has same or
            # greater precedence to current
            # token, which is an operator.
            # Apply operator on top of 'ops'
            # to top two elements in values stack.
            while len(ops) != 0 and precedence(ops[-1]) >= precedence(
                expression[i]
            ):

                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(applyOp(val1, val2, op))

            # Push current token to 'ops'.
            ops.append(expression[i])

        i += 1

    # Entire expression has been parsed
    # at this point, apply remaining ops
    # to remaining values.
    while len(ops) != 0:

        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()

        values.append(applyOp(val1, val2, op))

    # Top of 'values' contains result,
    # return it.
    return values[-1]

@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        cases = (
            ("-(50) + (-79 / -31 / -(52)) / (-34 / (((-(24 / -12)))) / -80)",-50.230623266676396),
            ("1 + 1", 2),
            ("8/16", 0.5),
            ("3 -(-1)", 4),
            ("2 + -2", 0),
            ("10- 2- -5", 13),
            ("(((10)))", 10),
            ("3 * 5", 15),
            ("-7 * -(6 / 3)", 14)
        )

        for x, y in cases:
            test.assert_equals(calc(x), y)