def longest_subarray_sun(arr, sum):
	n = len(arr)
	my_dict = dict()
	pre_sum = 0
	res = 0

	for i in range(n):
		pre_sum += arr[i]
		if pre_sum == sum:
			res = i + 1
		if pre_sum not in my_dict:
			my_dict[pre_sum] = i
		if pre_sum in my_dict:
			res = max(res, i - my_dict[pre_sum])

	return res


if __name__ == "__main__":
	arr = [8, 3, 1, 5, -6, 6, 2, 2]
	sum = 4
	print(longest_subarray_sun(arr=arr, sum=sum))
