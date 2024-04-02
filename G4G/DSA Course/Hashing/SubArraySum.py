from collections import OrderedDict


def subarray_sum(arr, sum):
    n = len(arr)
    # using dictionary to store the sum which has appeared already.
    mp = OrderedDict({})
    curr_sum = 0
    count = 0
    # iterating over the array elements.
    for i in range(n):
        # storing prefix sum which is sum of elements till current element.
        curr_sum += arr[i]
        # checking if sum up to current element is equal to the given sum.
        if curr_sum == sum:
            # updating the counter.
            count += 1
        # if dictionary contains (curr_sum-sum) i.e. difference of current
        # and given sum, it means there is a subarray with sum of elements
        # equal to sum given.
        x = mp.get(curr_sum - sum, False)
        if x is not False:
            # adding number of times (curr_sum-sum) has
            # appeared in map to the counter.
            count += x
        # storing the prefix sum in dictionary.
        mp[curr_sum] = mp.get(curr_sum, 0) + 1
    # returning the count of subarrays.
    return count


if __name__ == "__main__":
    arr = [10, 2, -2, -20, 10]
    sum = -10
    print(subarray_sum(arr=arr, sum=sum))
