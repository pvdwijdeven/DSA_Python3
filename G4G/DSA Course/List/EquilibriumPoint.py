def equilibrium_point(arr) -> int:

    total_sum = sum(arr)
    leftsum = 0
    for i, num in enumerate(iterable=arr):
        total_sum -= num
        if leftsum == total_sum:
            return i
        leftsum += num
    return -1


if __name__ == "__main__":
    arr1 = [1, 2, 3, 3, 2, 1]
    arr2 = [8, 3, 3, 3, 2]
    print(equilibrium_point(arr=arr1))
    print(equilibrium_point(arr=arr2))
