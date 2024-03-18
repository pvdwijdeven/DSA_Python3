def first_repeated(arr) -> int:
  # arr : given array
  # n : size of the array
  dict = {}
  for element in arr:
    dict[element] = 0
  for element in arr:
    if dict[element] != 0:
      return element
    else:
      dict[element] += 1
  return -1


if __name__ == "__main__":
  arr = [1, 1, 2, 3, 1, 4, 2]
  print(first_repeated(arr=arr))
