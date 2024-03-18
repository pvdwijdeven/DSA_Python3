def reverse_array(arr, n) -> list[int]:
    for x in range(n // 2):
        arr[x], arr[n - x - 1] = arr[n - x - 1], arr[x]
    return arr


if __name__ == "__main__":
    print(reverse_array(arr=[1, 1, 2, 2, 3], n=5))
