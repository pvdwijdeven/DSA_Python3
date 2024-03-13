# the following function shows the first missing positive value
def smallest_missing_number(arr) -> int:
    # first move all number < 1 to the left
    j = 0
    for i in range(len(arr)):
        if arr[i] < 1:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    arr_pos = arr[j:]
    n_pos = len(arr_pos)
    # now mark index of integers found with negative number
    for i in range(n_pos):
        if abs(arr_pos[i]) <= n_pos:
            arr_pos[abs(arr_pos[i]) - 1] = abs(arr_pos[abs(arr_pos[i]) - 1]) * -1
    for i in range(0, n_pos):
        if arr_pos[i] >= 1:
            return i + 1
    return n_pos + 1


if __name__ == "__main__":
    arr0 = [0, -10, 1, 3, -20]
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [-5, 1, 3, -20, -50]
    print(smallest_missing_number(arr=arr0))
    print(smallest_missing_number(arr=arr1))
    print(smallest_missing_number(arr=arr2))
