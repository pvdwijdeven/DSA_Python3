def get_points(points):
    n = len(points) - 2
    res = (n * (n + 1) * (n + 2)) // 6
    return res


def count_col_triang(col_list):

    colors = set()
    points = {}
    for x in col_list:
        colors.add(x[1])
        if x[1] not in points:
            points[x[1]] = []
        points[x[1]].append(x[0])
    total_points = sum([len(x) for x in points.values()])
    res = {}
    for color in points:
        res[color] = 0
        if len(points[color]) >= 3:
            res[color] = get_points(points[color])

    total = sum(res.values())
    mx = 0
    mx_col = []
    for x in res:
        if res[x] > mx:
            mx = res[x]
            mx_col = [x]
        elif res[x] == mx:
            mx_col.append(x)
    mx_col.append(mx)
    print(([total_points, len(colors), total, mx_col]))
    return [total_points, len(colors), total, mx_col]


def fixed_tests():
    assert count_col_triang(
        col_list=[
            [[3, -4], "blue"],
            [[-7, -1], "red"],
            [[7, -6], "yellow"],
            [[2, 5], "yellow"],
            [[1, -5], "red"],
            [[-1, 4], "red"],
            [[1, 7], "red"],
            [[-3, 5], "red"],
            [[-3, -5], "blue"],
            [[4, 1], "blue"],
        ]
    ) == [10, 3, 11, ["red", 10]]

    assert count_col_triang(
        col_list=[
            [[3, -4], "blue"],
            [[-7, -1], "red"],
            [[7, -6], "yellow"],
            [[2, 5], "yellow"],
            [[1, -5], "red"],
            [[1, 1], "red"],
            [[1, 7], "red"],
            [[1, 4], "red"],
            [[-3, -5], "blue"],
            [[4, 1], "blue"],
        ]
    ) == [10, 3, 7, ["red", 6]]

    assert count_col_triang(
        col_list=[
            [[1, -2], "red"],
            [[7, -6], "yellow"],
            [[2, 5], "yellow"],
            [[1, -5], "red"],
            [[1, 1], "red"],
            [[1, 7], "red"],
            [[1, 4], "red"],
            [[-3, -5], "blue"],
            [[4, 1], "blue"],
        ]
    ) == [9, 3, 0, []]


if __name__ == "__main__":
    fixed_tests()
