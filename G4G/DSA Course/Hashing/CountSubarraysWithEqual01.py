def count_subarrays_equal_01(arr):

	# NOTE: Dictionary in python in
	# implemented as Hash Maps.
	# Create an empty hash map (dictionary)
	n = len(arr)
	mp = {}
	cur_sum = 0
	count = 0

	# Traverse through the given array
	for i in range(0, n):
		if arr[i] == 0:
			arr[i] = -1
		else:
			arr[i] = 1
		# Add current element to sum
		cur_sum = cur_sum + arr[i]
		# To handle sum = 0 at last index
		if cur_sum == 0:
			count += 1
		# If this sum is seen before,
		if cur_sum in mp:
			count += mp[cur_sum]
		mp[cur_sum] = mp.get(cur_sum, 0) + 1
		if arr[i] == -1:
			arr[i] = 0
		else:
			arr[i] = 1

	return count


if __name__ == "__main__":
	arr = [1, 0, 0, 1, 0, 1, 1]

	print(count_subarrays_equal_01(arr=arr))
	arr = [1, 1, 1, 1, 0]

	print(count_subarrays_equal_01(arr=arr))