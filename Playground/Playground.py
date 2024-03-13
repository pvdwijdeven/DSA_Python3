def function(n):
    if n == 0 or n == 1:
        return n
    if n % 3 != 0:
        return 0
    return function(n=n // 3)


for i in range(30):
    print(i, function(i))
