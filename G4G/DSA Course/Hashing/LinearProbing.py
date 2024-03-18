# Function to fill the array elements into a hash table
# using Linear Probing to handle collisions.
def linear_probing(hashSize, arr):
  # Your code here
  size = hashSize
  t = [-1] * hashSize
  for element in arr:
    if element in t:
      continue
    done = False
    plus = 0
    while not done:
      pos = (element + plus) % hashSize
      if t[pos] == -1:
        t[pos] = element
        size -= 1
        done = True
        if size == 0:
          return t
      else:
        plus += 1
  return t


arr = [4, 14, 24, 44, 1, 2, 3, 1, 3, 5, 6, 3, 1]
hashSize = 10
print(linear_probing(hashSize=hashSize, arr=arr))
