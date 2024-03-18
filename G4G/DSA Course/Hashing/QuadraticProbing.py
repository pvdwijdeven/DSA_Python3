# using Linear Probing to handle collisions.
def quadratic_probing(hash, hashSize, arr) -> list[int]:
    size = hashSize
    hash = [-1] * hashSize
    for element in arr:
        if element in hash:
            continue
        done = False
        plus = 0
        while not done:
            pos = (element + plus**2) % hashSize
            if hash[pos] == -1:
                hash[pos] = element
                size -= 1
                done = True
                if size == 0:
                    return hash
            else:
                plus += 1
    return hash


if __name__ == "__main__":
    hash = []
    arr = [21, 10, 32, 43]
    hashSize = 11
    print(quadratic_probing(hash=hash, hashSize=hashSize, arr=arr))
