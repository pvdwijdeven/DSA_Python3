def palindrome(str):
    if len(str) <= 1:
        return True
    if str[0] == str[-1]:
        return palindrome(str[1:-1])
    else:
        return False


if __name__ == "__main__":
    print(palindrome("partersetrap"))
