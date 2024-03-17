# Function to find list of all words possible by pressing given numbers.
def words_from_phonenumber(arr) -> list[str]:
    phone = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }

    res = []

    def helper(arr, N, cur, i):
        if i == N:
            res.append(cur)
        else:
            for j in phone[arr[i]]:
                cur = cur + j
                helper(arr=arr, N=N, cur=cur, i=i + 1)
                cur = cur[:-1]

    helper(arr=arr, N=len(arr), cur="", i=0)
    return res


if __name__ == "__main__":
    arr = [2, 3, 4]
    print(words_from_phonenumber(arr=arr))
