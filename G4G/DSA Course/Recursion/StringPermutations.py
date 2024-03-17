def permute(str, ans, lst):
    if len(str) == 0:
        lst.append(ans)
        return

    for i in range(len(str)):
        ch = str[i]
        left_substr = str[0:i]
        right_substr = str[i + 1 :]
        rest = left_substr + right_substr
        permute(rest, ans + ch, lst)
    return list(set(lst))


if __name__ == "__main__":
    str = "ABBA"

    print("All possible strings are : ")
    print(permute(str=str, ans="", lst=[]))
