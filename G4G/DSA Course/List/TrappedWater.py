# this function returns the amount of water that can be trapped in blocks
# the array are non-negative integers, representing the height of the blocks
def trapping_water(arr) -> int:
    n = len(arr)
    left_max = [0] * n
    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i])
    right_max = [0] * n
    right_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(arr[i], right_max[i + 1])
    water = 0
    for i in range(0, n):
        water += min(left_max[i], right_max[i]) - arr[i]
    return water


if __name__ == "__main__":
    arr1 = [3, 0, 4, 0, 2, 0, 3]
    arr2 = [6, 9, 9]
    arr3 = [7, 4, 0, 9]
    arr4 = [3, 0, 0, 2, 0, 4]
    print(trapping_water(arr=arr1))
    print(trapping_water(arr=arr2))
    print(trapping_water(arr=arr3))
    print(trapping_water(arr=arr4))
