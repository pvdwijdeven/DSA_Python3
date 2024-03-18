# The following function returns the medium of 2 sorted arrays
def median_2_sorted_arrays(arr1, arr2) -> int | float | None:
  # Assumption both arr1 and arr1 cannot be empty
  n1 = len(arr1)
  n2 = len(arr2)
  if n1 > n2:
    return median_2_sorted_arrays(arr1=arr2,
                                  arr2=arr1)  # Swapping to make arr1 smaller
  start = 0
  end = n1
  real_mid_in_merged_array = (n1 + n2 + 1) // 2
  while start <= end:
    mid = (start + end) // 2
    pos1 = mid
    pos2 = real_mid_in_merged_array - mid
    # checking overflow of indices
    left1 = arr1[pos1 - 1] if (pos1 > 0) else float("-inf")
    left2 = arr2[pos2 - 1] if (pos2 > 0) else float("-inf")
    right1 = arr1[pos1] if (pos1 < n1) else float("inf")
    right2 = arr2[pos2] if (pos2 < n2) else float("inf")
    # if correct partition is done
    if left1 <= right2 and left2 <= right1:
      if (n2 + n1) % 2 == 0:
        return (max(left1, left2) + min(right1, right2)) / 2.0
      return max(left1, left2)
    elif left1 > right2:
      end = mid - 1
    else:
      start = mid + 1


# Driver code
arr1 = [-5, 3, 6, 12, 15, 17, 20, 25]
arr2 = [-12, -10, -6, -3, 4, 10]
print(median_2_sorted_arrays(arr1=arr1, arr2=arr2))
