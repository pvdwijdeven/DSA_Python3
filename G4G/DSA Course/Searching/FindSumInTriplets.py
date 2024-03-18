def sum_in_pair(arr, x, i_start) -> list[tuple[int, int]]:
  res = []
  i = i_start
  j = len(arr) - 1
  while i < j:
    if arr[i] + arr[j] == x:
      res.append((i, j))
      j -= 1
    elif arr[i] + arr[j] < x:
      i += 1
    else:
      j -= 1
  return res


def sum_in_triplet(arr, x) -> list[tuple[int, int, int]]:
  res = []
  for i in range(len(arr) - 2):
    pair_res = sum_in_pair(arr=arr, x=x - arr[i], i_start=i + 1)
    if pair_res != []:
      for pair in pair_res:
        res.append((arr[i], arr[pair[0]], arr[pair[1]]))
  return res


arr = [2, 3, 5, 10, 15, 18, 20]
x = 33
print(sum_in_triplet(arr=arr, x=x))
