# Function to return the maximum water that can be stored
# by choosing 2 buildings and destroying the rest
def max_water_between_buildings(arr) -> int:
	max_water = 0
	left = 0
	right = len(arr) - 1
	while left < right:
		if arr[left] < arr[right]:
			max_water = max(max_water, (right - left - 1) * arr[left])
			left += 1
		elif arr[right] < arr[left]:
			max_water = max(max_water, (right - left - 1) * arr[right])
			right -= 1
		else:
			max_water = max(max_water, (right - left - 1) * arr[left])
			left += 1
			right -= 1
	return max_water


if __name__ == "__main__":
	arr = [2, 1, 3, 4, 6, 5]  # output = 8
	print(max_water_between_buildings(arr=arr))
	arr = [2, 1]  # output = 0
	print(max_water_between_buildings(arr=arr))
