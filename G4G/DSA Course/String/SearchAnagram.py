# Anagram Search

CHAR = 256


def are_same(ct, cp) -> bool:
    for i in range(CHAR):
        if ct[i] != cp[i]:
            return False
    return True


def search_anagram(txt, pat) -> int:
    n = len(txt)
    m = len(pat)
    ct = [0] * CHAR
    cp = [0] * CHAR
    for i in range(m):
        ct[ord(txt[i])] += 1
        cp[ord(pat[i])] += 1
    for i in range(m, n):
        if are_same(ct, cp):
            return i - m
        ct[ord(txt[i])] += 1
        ct[ord(txt[i - m])] -= 1
    return -1


if __name__ == "__main__":
    txt = "geeksforgeeks"
    pat = "frog"
    print(search_anagram(txt=txt, pat=pat))
