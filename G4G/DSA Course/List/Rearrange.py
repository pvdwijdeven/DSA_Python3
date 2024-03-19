# Function to rearrange an array so that arr[i]
# becomes arr[arr[i]] with O(1) extra space
def rearrange(arr) -> list[int]:
    arr = arr[:]
    n = len(arr)
    for i in range(0, n):
        arr[i] += (arr[arr[i]] % n) * n
    for i in range(0, n):
        arr[i] = arr[i] // n
    return arr


if __name__ == "__main__":
    arr1 = [0, 1]
    arr2 = [4, 0, 2, 1, 3]
    arr3 = [1, 4, 7, 6, 2, 0, 3, 5]
    print(rearrange(arr=arr1))
    print(rearrange(arr=arr2))
    print(rearrange(arr=arr3))
    print(arr3)
