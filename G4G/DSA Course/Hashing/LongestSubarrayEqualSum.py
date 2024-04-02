def longest_common_sum(arr1, arr2):

	# NOTE: Dictionary in python in
	# implemented as Hash Maps.
	# Create an empty hash map (dictionary)
	n = len(arr1)
	arr = [0 for i in range(n)]

	for i in range(n):
		arr[i] = arr1[i] - arr2[i]

	# Creates an empty hashMap hM
	hm = {}
	sum = 0  # Initialize sum of elements
	max_len = 0  # Initialize result

	# Traverse through the given array
	for i in range(n):

		# Add current element to sum
		sum += arr[i]

		# To handle sum=0 at last index
		if sum == 0:
			max_len = i + 1

		# If this sum is seen before,
		# then update max_len if required
		if sum in hm:
			max_len = max(max_len, i - hm[sum])
		else:  # Else put this sum in hash table
			hm[sum] = i
	return max_len


if __name__ == "__main__":
	arr1 = [0, 1, 0, 0, 0, 0]
	arr2 = [1, 0, 1, 0, 0, 1]

	print(longest_common_sum(arr1, arr2))
