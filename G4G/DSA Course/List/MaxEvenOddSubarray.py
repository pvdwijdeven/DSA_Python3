def max_even_odd(arr) -> int:
    n = len(arr)
    res = 0
    cur = 1
    is_even = [arr[0] % 2 == 0]
    for i in range(1, n):
        is_even.append(arr[i] % 2 == 0)
        if is_even[i] != is_even[i - 1]:
            cur += 1
        else:
            res = max(res, cur)
            cur = 1
    res = max(res, cur)
    return res


if __name__ == "__main__":
    arr1 = [10, 12, 14, 7, 8]
    arr2 = [4, 6]
    print(max_even_odd(arr=arr1))
    print(max_even_odd(arr=arr2))
