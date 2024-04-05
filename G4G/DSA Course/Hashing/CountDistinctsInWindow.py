from collections import Counter


def count_distincts_in_window(arr, window):
	mp = Counter(arr[0:window])
	n = len(arr)
	res = []
	res.append(len(mp))
	for i in range(window, n):
		x = arr[i - k]
		mp[x] -= 1
		mp[arr[i]] += 1
		if mp[x] == 0:
			del mp[x]
		res.append(len(mp))
	return res


if __name__ == "__main__":
	arr = [10, 20, 10, 10, 30, 40]
	k = 4
	print(count_distincts_in_window(arr=arr, window=k))