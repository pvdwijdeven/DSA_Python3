# Counting Sort for numbers
def counting_sort(arr) -> list[int]:
    min_arr = min(arr)
    k = max(arr) - min(arr) + 1
    output = [0] * len(arr)
    count = [0] * k
    for x in arr:
        count[x - min_arr] += 1
    for i in range(1, k):
        count[i] += count[i - 1]
    for x in reversed(arr):
        output[count[x - min_arr] - 1] = x
        count[x - min_arr] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]
    return arr


# Counting Sort for strings
def counting_sort_string(arr) -> str:
    output = [" "] * len(arr)
    count = {}
    for x in arr:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    key_list = sorted(count.keys())
    prev = 0
    for i in key_list:
        count[i] += prev
        prev = count[i]
    for x in reversed(arr):
        output[count[x] - 1] = x
        count[x] -= 1
    return "".join(output)


if __name__ == "__main__":
    arr = [-1, 10, 2, 1, 1, 1]
    print(counting_sort(arr=arr))
    s = "edsab"
    print(counting_sort_string(arr=s))
