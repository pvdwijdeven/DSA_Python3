def is_zero_sum(array) -> bool:
    pre_sum = 0
    h = set()
    for i in range(len(array)):
        pre_sum += array[i]
        if pre_sum == 0 or pre_sum in h:
            return True
        h.add(pre_sum)
    return False


if __name__ == "__main__":
    A = [4, 3, -2, 1, 1]
    print(is_zero_sum(array=A))
