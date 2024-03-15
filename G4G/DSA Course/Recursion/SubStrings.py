def get_sub_strings(str) -> list[str]:
    def sub(str, cur="", ind=0) -> str:
        res = ""
        if ind == len(str):
            return cur + "_"
        res += sub(str=str, cur=cur, ind=ind + 1)
        res += sub(str=str, cur=cur + str[ind], ind=ind + 1)
        return res

    return sub(str=str).split("_")[:-1]


if __name__ == "__main__":
    print(get_sub_strings(str="ABC"))
