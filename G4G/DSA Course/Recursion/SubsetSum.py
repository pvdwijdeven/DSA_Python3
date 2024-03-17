def get_sub_sum(arr, sum) -> int:
    def sub(arr, sum, cur=0, ind=0) -> int:
        res = 0
        if ind == len(arr):
            if cur == sum:
                return 1
            else:
                return 0
        res += sub(arr=arr, sum=sum, cur=cur, ind=ind + 1)
        res += sub(arr=arr, sum=sum, cur=cur + arr[ind], ind=ind + 1)
        return res

    return sub(arr=arr, sum=sum)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    sum = 3
    print(get_sub_sum(arr=arr, sum=sum))
    arr = [10, 5, 2, 3, 6, 8]
    sum = 8
    print(get_sub_sum(arr=arr, sum=sum))
