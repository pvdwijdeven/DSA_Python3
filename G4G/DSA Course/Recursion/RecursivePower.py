# O(n) solution:
def recursive_power(n, p) -> int:
    """
    return value of n^p recursively;
    """
    res = n
    if p == 0:
        return 1
    if p == 1:
        return n
    res *= recursive_power(n, p - 1)
    return res


# O(logn) solution:
def power(n, p) -> int:
    modulo = 10**9 + 7
    if p == 0:
        return 1

    x = power(n=n, p=p // 2)

    if p % 2 == 0:
        return x * x % modulo
    else:
        return n * x * x % modulo


if __name__ == "__main__":
    print(recursive_power(n=9, p=9))
    print(power(n=9, p=9))
