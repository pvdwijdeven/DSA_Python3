# Function to merge three sorted arrays into a single array.
def merge_3_sorted(A, B, C) -> list[int]:
    arr = []
    i, ia, ib, ic = 0, 0, 0, 0
    la, lb, lc = len(A), len(B), len(C)
    while ia + ib + ic <= la + lb + lc - 1:
        if ia < la:
            aa = A[ia]
        else:
            aa = float("inf")
        if ib < lb:
            bb = B[ib]
        else:
            bb = float("inf")
        if ic < lc:
            cc = C[ic]
        else:
            cc = float("inf")
        if aa <= bb and aa <= cc:
            ia += 1
            arr.append(aa)
        elif bb <= aa and bb <= cc:
            ib += 1
            arr.append(bb)
        elif cc <= aa and cc <= bb:
            ic += 1
            arr.append(cc)
    return arr


if __name__ == "__main__":
    A = [1, 2, 3, 4]
    B = [1, 2, 3, 4, 5]
    C = [1, 2, 3, 4, 5, 6]
    res = merge_3_sorted(A=A, B=B, C=C)
    print(res)
    A = [1, 2]
    B = [2, 3, 4]
    C = [4, 5, 6, 7]
    res = merge_3_sorted(A=A, B=B, C=C)
    print(res)
