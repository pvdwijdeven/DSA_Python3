def is_sorted(arr) -> bool:
    reversed = arr[0] > arr[-1]
    prev = arr[0]
    for x in range(1, len(arr)):
        if reversed:
            if arr[x] > prev:
                return False
        else:
            if arr[x] < prev:
                return False
        prev = arr[x]
    return True


if __name__ == "__main__":
    print(is_sorted(arr=[1, 1, 2, 2, 3]))
    print(is_sorted(arr=[4, 2]))
