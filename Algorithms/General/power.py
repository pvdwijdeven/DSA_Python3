import timeit

# still slower than default ** power function, most of the times....
def power(x, y):
    temp = 0
    if(y == 0):
        return 1
    temp = power(x, int(y / 2))
    if (y % 2 == 0):
        return temp * temp
    else:
        return x * temp * temp

def main():
    ans = power(5,100)
    print(ans)
    result = timeit.timeit(stmt='power(3,1234567)', globals=globals(), number=5)
    print(result)
    result = timeit.timeit(stmt='3**1234567', globals=globals(), number=5)
    print(result)

if __name__ == "__main__":
    main()