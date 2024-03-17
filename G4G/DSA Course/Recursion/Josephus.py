def josephus(n, k) -> int:

    if n == 1:
        return 1
    else:

        # The position returned by
        # josephus(n - 1, k) is adjusted
        # because the recursive call
        # josephus(n - 1, k) considers
        # the original position
        # k%n + 1 as position 1
        res = (josephus(n=n - 1, k=k) + k - 1) % n + 1
        return res


# Driver Program to test above function

if __name__ == "__main__":
    n = 14
    k = 2

    print("The chosen place is ", josephus(n=n, k=k))
