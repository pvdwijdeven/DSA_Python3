def get_by_index(arr, n, idx) -> int:
    if idx > n - 1:
        return -1
    return arr[idx]


def insert_at_end(arr, element) -> list[int]:
    arr.append(element)
    return arr


def insert_at_index(arr, index, element) -> list[int]:
    arr.insert(index, element)
    return arr


def update_array(arr, idx, element) -> None:
    arr[idx] = element


def delete_from_array(arr, idx) -> list[int]:
    del arr[idx]
    arr.append(0)
    return arr


def median(A, N) -> int:
    A.sort()
    if N % 2 == 0:
        return (A[(N // 2) - 1] + A[(N // 2)]) // 2
    else:
        return A[((N - 1) // 2)]
    # If median is fraction then convert the median to integer and return


# Function to find mean of the array elements.
def mean(A, N) -> int:
    return sum(A) // N


if __name__ == "__main__":
    print(mean(A=[1, 1, 1, 1, 1, 1], N=6))
    print(median(A=[1, 1, 1, 1, 1, 1], N=6))
