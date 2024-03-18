# Function to return the name of candidate that received maximum votes.
def winner(arr) -> str:
    # return the name of the winning candidate and the votes he recieved
    dict = {}
    for name in arr:
        dict[name] = 0
    for name in arr:
        dict[name] += 1
    max = 0
    for name in arr:
        if dict[name] > max:
            max = dict[name]
    res = []
    for name in arr:
        if dict[name] == max:
            res.append(name)
    return sorted(res)[0]


if __name__ == "__main__":
    arr = [
        "john",
        "johnny",
        "jackie",
        "johnny",
        "john",
        "jackie",
        "jamie",
        "jamie",
        "john",
        "johnny",
        "jamie",
        "johnny",
        "john",
    ]
    print(winner(arr=arr))
