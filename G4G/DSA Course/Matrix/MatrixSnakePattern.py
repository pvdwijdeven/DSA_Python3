def matrix_snake_pattern(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    res = []
    for row in range(rows):
        if row % 2 == 0:
            for col in range(cols):
                res.append(matrix[row][col])
        else:
            for col in range(cols - 1, -1, -1):
                res.append(matrix[row][col])
    return res


if __name__ == "__main__":
    mat = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
    print(matrix_snake_pattern(matrix=mat))
