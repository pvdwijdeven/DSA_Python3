# Function to return non-repeated elements in the array.
def print_not_repeated(arr):
    dict = {}
    for i in arr:
        dict[i] = 0
    # storing the frequency of each element.
    for i in arr:
        dict[i] += 1
    res = []
    # iterating over the array elements.
    for i in arr:
        # if frequency of current element is 1,
        # then we increment the counter.
        if dict[i] == 1:
            res.append(i)
    # returning the count of non-repeated elements.
    return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 1, 1, 2, 3]
    print(print_not_repeated(arr=arr))
