def decodeHuffmanData(root, binaryString):

    res = ""
    n = len(binaryString)
    cur = root
    i = 0
    while i != n:
        if cur.data == "$":
            if binaryString[i] == "0":
                cur = cur.left
            else:
                cur = cur.right
            i += 1
        else:
            res += cur.data
            cur = root
    res += cur.data

    return res
