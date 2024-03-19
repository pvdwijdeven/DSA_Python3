def floorSqrt(x) -> int:
    if x == 0 or x == 1:
        return x
    start = 0
    end = x // 2
    res = 0
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            start = mid + 1
            res = mid
        else:
            end = mid - 1
    return res


if __name__ == "__main__":
    for i in range(10):
        print(i, floorSqrt(x=i))
    print(floorSqrt(x=100000000))
    print(floorSqrt(x=225))
    print(floorSqrt(x=224))
    print(floorSqrt(x=226))
