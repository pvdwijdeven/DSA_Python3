def count_ones(arr) -> int:
	low = 0
	high = len(arr)-1

	while low <= high:
		mid = low + (high-low)//2
		if (mid == len(arr)-1 and arr[mid]==1) or (arr[mid]==1 and (mid==0 or arr[mid+1]!=1)):
			return mid+1
		elif arr[mid]<1:
			high = mid-1
		else:
			low = mid+1
	return 0


if __name__ == "__main__":
	arr = [1,1,1,1,1,1,1,1,1]
	print(count_ones(arr=arr))
