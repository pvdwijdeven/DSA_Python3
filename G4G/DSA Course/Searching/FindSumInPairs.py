# Find if sum is in 1 or more pairs: two Pointers Approach
def sum_in_pair(arr, x) -> list[tuple[int, int]]:
  res = []
  i = 0
  j = len(arr) - 1
  while i < j:
    if arr[i] + arr[j] == x:
      res.append((arr[i], arr[j]))
      j -= 1
    elif arr[i] + arr[j] < x:
      i += 1
    else:
      j -= 1
  return res


if __name__ == "__main__":
  arr = [0, 2, 5, 7, 10, 12, 15, 30]
  x = 17
  print(sum_in_pair(arr=arr, x=x))
