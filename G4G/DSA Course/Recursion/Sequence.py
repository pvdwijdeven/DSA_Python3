# S(n) = n+ n*(S(n-1)) and S(0) = 1


def theSequence(n):
    #code here
    if n == 0:
        return 1
    n = n + n * theSequence(n-1)
    return n



print(theSequence(2))
print(theSequence(3))
print(theSequence(10))
