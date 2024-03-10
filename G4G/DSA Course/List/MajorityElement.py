# The following function finds the majority element
# of an arry, if any exists. A majority element in
# an array size n is an element that appears more than
# n/2 times (and hence there is at most one such element).
def get_majority_element(arr) -> tuple[bool, int]:

    def get_candidate(arr) -> int:
        cur_index = 0
        count = 1
        for i in range(len(arr)):
            if arr[cur_index] == arr[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                cur_index = i
                count = 1
        return arr[cur_index]

    candidate = get_candidate(arr=arr)
    count = 0
    for i in range(len(arr)):
        if arr[i] == candidate:
            count += 1
    return (count > len(arr) / 2), candidate


if __name__ == "__main__":
    arr1 = [8, 8, 9, 9, 9, -11, 9]
    arr2 = [3, 4, 3, 4, 3]
    arr3 = [10, -3, -4, 7, 6, 5, -4, -1]
    print(get_majority_element(arr=arr1))
    print(get_majority_element(arr=arr2))
    print(get_majority_element(arr=arr3))
