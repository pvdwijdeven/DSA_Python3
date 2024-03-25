# Cycle sort
def cycle_sort(arr) -> list[int]:
    for cur_pos in range(len(arr) - 1):
        cur_item = arr[cur_pos]
        pos = cur_pos
        for i in range(cur_pos + 1, len(arr)):
            if arr[i] < cur_item:
                pos = pos + 1
        if pos == cur_pos:
            continue

        while cur_item == arr[pos]:
            pos += 1
        arr[pos], cur_item = cur_item, arr[pos]

        while pos != cur_pos:
            pos = cur_pos
            for i in range(cur_pos + 1, len(arr)):
                if arr[i] < cur_item:
                    pos += 1
            while cur_item == arr[pos]:
                pos += 1
            arr[pos], cur_item = cur_item, arr[pos]
    return arr


if __name__ == "__main__":
    arr = [20, 40, 30, 10, 50]
    n = len(arr)
    print(cycle_sort(arr=arr))
