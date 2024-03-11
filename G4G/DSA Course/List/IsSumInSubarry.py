def is_sum_in_subarray(arr, sum) -> bool:
    s, cur = 0, 0
    for i in range(len(arr)):
        cur += arr[i]
        while cur > sum:
            cur -= arr[s]
            s += 1
        if cur == sum:
            return True

    return False


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    sum = 9
    print(is_sum_in_subarray(arr=arr, sum=sum))
