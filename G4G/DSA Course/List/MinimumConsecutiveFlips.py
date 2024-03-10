# The following function prints the start and end
# points for flipping 1s or 0s in a binary array,
# so that the array becomes only 1s or 0s, with the
# minimum amount of flips. A row of the same values (0s or 1s)
# counts as 1 flip
def minimum_consecutive_flips(arr) -> None:
    flip = 0 if arr[0] == 1 else 1
    flipping = False
    for i in range(len(arr)):
        if not flipping and arr[i] == flip:
            flipping = True
            print(f"From {i} to", end=" ")
        if flipping and arr[i] != flip:
            print(i - 1)
            flipping = False
    if flipping:
        print(len(arr) - 1)


if __name__ == "__main__":
    arr1 = [0, 0, 0, 1, 1, 0, 0, 1, 1]
    arr2 = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1]
    arr3 = [1, 0]
    minimum_consecutive_flips(arr=arr1)
    minimum_consecutive_flips(arr=arr2)
    minimum_consecutive_flips(arr=arr3)
