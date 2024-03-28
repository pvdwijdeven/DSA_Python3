def spiral_traversal(matrix):
    row_end = len(matrix)
    col_end = len(matrix[0])
    row_start = 0
    col_start = 0
    res = []
    while row_start < row_end and col_start < col_end:
        for col in range(col_start, col_end):
            res.append(matrix[row_start][col])
        row_start += 1
        for row in range(row_start, row_end):
            res.append(matrix[row][col_end - 1])
        col_end -= 1
        if row_start < row_end:
            for col in range(col_end - 1, (col_start - 1), -1):
                res.append(matrix[row_end - 1][col])
            row_end -= 1
        if col_start < col_end:
            for row in range(row_end - 1, row_start - 1, -1):
                res.append(matrix[row][col_start])
            col_start += 1
    return res


if __name__ == "__main__":

    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(spiral_traversal(matrix=A))
