from collections import defaultdict


# the following function sorts the array based on frequency.
# if elements have the same frequency, the are sorted in ascending order.
def sort_by_frequency(arr, n):
	mp = defaultdict(lambda: 0)
	for i in range(n):
		mp[arr[i]] += 1
	arr.sort(key=lambda x: (-mp[x], x), reverse=False)
	return arr


if __name__ == "__main__":
	arr = [8, 9, 1, 2, 3, 1]
	print(sort_by_frequency(arr=arr, n=len(arr)))
