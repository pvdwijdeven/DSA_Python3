def stock_buy_sell(arr) -> tuple[list[list[int]], int]:
    i = 0
    res = []
    bought = -1
    profit = 0
    price = 0
    n = len(arr)
    while i < n:
        if bought > -1:
            if i == n - 1 or arr[i] > arr[i + 1]:
                profit += arr[i] - price
                res.append([bought, i])
                bought = -1
        else:
            if i < n - 1 and arr[i] < arr[i + 1]:
                bought = i
                price = arr[i]
        i += 1
    return res, profit


if __name__ == "__main__":
    arr = [100, 180, 260, 310, 40, 535, 695]
    print(stock_buy_sell(arr=arr))
