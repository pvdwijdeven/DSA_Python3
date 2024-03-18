# Function to insert elements of array in the hashTable avoiding collisions.
def separate_chaining(hashSize, arr) -> list[list[int]]:
    hash = [[] for x in range(hashSize)]
    for element in arr:
        key = element % hashSize
        hash[key].append(element)
    return hash


if __name__ == "__main__":
    hashSize = 10
    arr = [92, 4, 14, 24, 44, 91]
    print(separate_chaining(hashSize=hashSize, arr=arr))
