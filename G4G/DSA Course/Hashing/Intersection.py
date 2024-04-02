def array_intersection(a, b, n, m):
    # return: expected length of the intersection array.
    n = len(a)
    m = len(b)
    res = 0
    hash = set()
    for x in a:
        hash.add(x)
    for x in b:
        if x in hash:
            hash.remove(x)
            res += 1
    return res


def array_union(a, b, n, m):
    # return: expected length of the intersection array.
    n = len(a)
    m = len(b)
    hash = set()
    for x in a:
        hash.add(x)
    for x in b:
        if x not in hash:
            hash.add(x)
    return len(hash)


if __name__ == "__main__":
    n = 5
    m = 3
    a = [89, 24, 75, 11, 23]
    b = [89, 2, 4]
    print(array_intersection(a, b, n, m))
    print(array_union(a, b, n, m))
