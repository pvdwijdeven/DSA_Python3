# Merge overlapping intervals
def merge_overlappinig_intervals(arr):
    arr.sort(key=lambda x: x[0])
    res = 0
    for i in range(1, len(arr)):
        if arr[res][1] >= arr[i][0]:
            arr[res][1] = max(arr[res][1], arr[i][1])
        else:
            res = res + 1
            arr[res] = arr[i]
    return arr[: res + 1]


if __name__ == "__main__":
    arr = [[5, 10], [3, 15], [18, 30], [2, 7]]
    print(merge_overlappinig_intervals(arr=arr))
