# Function to find two repeated elements.
def two_repeaated(arr) -> list[int]:
    res = []
    for i in range(len(arr)):
        arr[abs(arr[i])] *= -1
        if arr[abs(arr[i])] > 0:
            res.append(abs(arr[i]))
    return res


if __name__ == "__main__":
    arr = [5, 4, 7, 2, 8, 1, 3, 9, 6, 4, 3]
    print(two_repeaated(arr=arr))
    arr = [1, 2, 2, 1]
    print(two_repeaated(arr=arr))
