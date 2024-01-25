def ispar(x):
    # code here
    stack = []
    opening = ["{", "(", "["]
    closing = ["}", ")", "]"]
    par = dict(map(lambda i, j: (i, j), closing, opening))
    for char in x:
        if char in opening:
            stack.append(char)
        if char in closing:
            if par[char] != stack.pop():
                return False
    return stack == []


x = "{[()]}"
print(ispar(x))
