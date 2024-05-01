from collections import deque


def get_first_N(n, digits) -> list[str]:
    q = deque()
    res: list[str] = []
    for digit in digits:
        q.append(str(object=digit))
    i = 0
    while (i + len(q)) < n:
        curr = q.popleft()
        res.append(curr)
        for digit in digits:
            q.append(curr + str(object=digit))
        i += 1
    while i < n:
        res.append(q.popleft())
        i += 1
    return res


def main() -> None:
    print(get_first_N(20, digits=[5, 6]))


if __name__ == "__main__":
    main()
