def prefix_sum(arr) -> tuple[list[int], list[int]]:
    sum_arr = [0] * len(arr)
    weight_arr = [0] * len(arr)
    sum_arr[0] = arr[0]
    weight_arr[0] = 0
    for i in range(1, len(arr)):
        sum_arr[i] = sum_arr[i - 1] + arr[i]
        weight_arr[i] = weight_arr[i - 1] + arr[i] * i
    return sum_arr, weight_arr


def get_sum(sum_arr, left, right) -> int:
    if left == 0:
        return sum_arr[right]
    else:
        return sum_arr[right] - sum_arr[left - 1]


def get_weight_sum(sum_arr, weight_arr, left, right):
    if left == 0:
        return weight_arr[right] + sum_arr[right]
    else:
        return (
            weight_arr[right]
            - weight_arr[left - 1]
            - (left - 1) * (sum_arr[right] - sum_arr[left - 1])
        )


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    sum_arr, weight_arr = prefix_sum(arr=arr)
    print(sum_arr, weight_arr)
    print(get_sum(sum_arr=sum_arr, left=0, right=5))
    print(get_sum(sum_arr=sum_arr, left=3, right=4))
    print(get_weight_sum(sum_arr=sum_arr, weight_arr=weight_arr, left=0, right=1))
    print(get_weight_sum(sum_arr=sum_arr, weight_arr=weight_arr, left=2, right=3))
