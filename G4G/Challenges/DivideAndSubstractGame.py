def divAndSub(N):
    if N == 1:
        return "Arya"
    if N < 6:
        return "Jon"
    arr = [0] * (N + 1)
    i = 1
    while i < 6 and i <= N:
        arr[i] = 1
        i += 1

    i = 6
    while i <= N:
        # Whosever turn will it be we will
        # check if there is any move by
        # performing, there is a chance for
        # him to win, means if any
        # arr[condition] = 0 then he will win
        # for sure else not
        if arr[i // 2] == 0 or arr[i // 4] == 0 or arr[i // 3] == 0 or arr[i // 5] == 0:
            # Means the person doing the move can win through division
            arr[i] = 1
        elif arr[i - 2] == 0 or arr[i - 3] == 0 or arr[i - 4] == 0 or arr[i - 5] == 0:
            # Means the person doing the move can win through subtraction
            arr[i] = 1
        else:
            # Else other person will win
            arr[i] = 0
        i += 1

    # If arr[N] is 1 then Jon win else Arya win
    return "Jon" if (arr[N] == 1) else "Arya"
