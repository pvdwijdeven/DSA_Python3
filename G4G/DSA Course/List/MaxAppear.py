# the following function shows the first value that
# occurs the most in the ranges. The ranges are defiined
# from left[i] to right[i], where the value can be max 100.
def max_appear(left, right) -> int:
    freq = [0] * 101
    for i in range(len(left)):
        freq[left[i]] += 1
        freq[right[i] + 1] -= 1
    for i in range(1, len(freq)):
        freq[i] += freq[i - 1]
    return freq.index(max(freq))


if __name__ == "__main__":
    left = [1, 2, 4]
    right = [4, 5, 7]
    print(max_appear(left=left, right=right))
