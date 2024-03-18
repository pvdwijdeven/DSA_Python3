# Function to return the count of non-repeated elements in the array.
def count_non_repeated(arr) -> int:
    dict = {}
    for i in arr:
        dict[i] = 0
    # storing the frequency of each element.
    for i in arr:
        dict[i] += 1
    counter = 0
    # iterating over the array elements.
    for i in arr:
        # if frequency of current element is 1,
        # then we increment the counter.
        if dict[i] == 1:
            counter += 1
    # returning the count of non-repeated elements.
    return counter


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 1, 1, 2, 3]
    print(count_non_repeated(arr=arr))
