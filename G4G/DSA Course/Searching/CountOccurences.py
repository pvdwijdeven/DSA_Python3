def left_index(arr, x) -> int:
  left = 0
  right = len(arr) - 1
  while left <= right:
      mid = (left + right) // 2
      if arr[mid] > x:
          right = mid - 1
      elif arr[mid] < x:
          left = mid + 1
      else:
          if mid == 0 or arr[mid - 1] != arr[mid]:
              return mid
          else:
              right = mid - 1
  return -1


def right_index(arr, x) -> int:
  left = 0
  right = len(arr) - 1
  while left <= right:
      mid = (left + right) // 2
      if arr[mid] < x:
          left = mid + 1
      elif arr[mid] > x:
          right = mid - 1
      else:
          if mid == len(arr) - 1 or arr[mid] != arr[mid + 1]:
              return mid
          else:
              left = mid + 1
  return -1


def count_occurences(arr, x) -> int:
  first = left_index(arr=arr, x=x)
  if first == -1:
      return 0
  else:
      return right_index(arr=arr, x=x) - first + 1


if __name__ == "__main__":
  arr = [10, 20, 20, 20, 30, 30]

  print(10, count_occurences(arr=arr, x=10))
  print(20, count_occurences(arr=arr, x=20))
  print(30, count_occurences(arr=arr, x=30))
  print(25, count_occurences(arr=arr, x=25))
