def matrix_boundary_traversal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    res = []
    for col in range(cols):
        res.append(matrix[0][col])
    for row in range(1, rows):
        res.append(matrix[row][cols - 1])
    for col in range(cols - 2, -1, -1):
        res.append(matrix[rows - 1][col])
    for row in range(rows - 2, 0, -1):
        res.append(matrix[row][0])
    return res


if __name__ == "__main__":
    mat = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
    print(matrix_boundary_traversal(matrix=mat))
