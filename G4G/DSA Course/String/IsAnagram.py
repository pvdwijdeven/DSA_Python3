# Function is to check whether two strings are anagram of each other or not.
def is_anagram(s1, s2) -> bool:
    h = [0 for x in range(65, 122)]
    if len(s1) == len(s2):
        for i in range(len(s1)):
            h[ord(s1[i]) - 66] += 1
            h[ord(s2[i]) - 66] -= 1
    else:
        return False
    return all(i == 0 for i in h)


if __name__ == "__main__":
    s1 = "abzdef"
    s2 = "deaabc"
    print(is_anagram(s1=s1, s2=s2))
    s1 = "abadef"
    s2 = "deaabf"
    print(is_anagram(s1=s1, s2=s2))
