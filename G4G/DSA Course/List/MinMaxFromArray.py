def max_element(arr) -> int:
    ans = 0
    for x in arr:
        if x > ans:
            ans = x
    return ans


def min_element(arr) -> int:
    ans = 10**9
    for x in arr:
        if x < ans:
            ans = x
    return ans


if __name__ == "__main__":
    print(max_element(arr=[5, 4, 2, 1]))
    print(max_element(arr=[8]))
    print(min_element(arr=[5, 4, 2, 1]))
    print(min_element(arr=[8]))
