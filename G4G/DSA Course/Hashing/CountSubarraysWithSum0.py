def count_subarrays_sum0(arr):

# NOTE: Dictionary in python in
# implemented as Hash Maps.
# Create an empty hash map (dictionary)
n = len(arr)
mp = {}
cur_sum = 0
count = 0

# Traverse through the given array
for i in range(0, n):
	# Add current element to sum
	cur_sum = cur_sum + arr[i]
	# To handle sum = 0 at last index
	if cur_sum == 0:
		count += 1
	# If this sum is seen before,
	if cur_sum in mp:
		count += mp[cur_sum]
	mp[cur_sum] = mp.get(cur_sum, 0) + 1

return count