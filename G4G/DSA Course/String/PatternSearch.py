from timeit import timeit


# Naive Pattern Searching
def naive_pattern_search(txt, pat) -> list[int]:
    m = len(pat)
    n = len(txt)
    res = []
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if pat[j] != txt[i + j]:
                break
            j = j + 1
        if j == m:
            res.append(i)
    return res


# Naive Pattern Searching with distinction
def distinct_naive_pattern_search(txt, pat) -> list[int]:
    m = len(pat)
    n = len(txt)
    i = 0
    j = 0
    res = []
    while i <= (n - m):
        for j in range(m):
            if pat[j] != txt[i + j]:
                break
            j += 1
        if j == m:
            res.append(i)
            i += m
        if j == 0:
            i += 1
        else:
            i += j
    return res


# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book
# d is the number of characters in the input alphabet
# pat  -> pattern
# txt  -> text
# q    -> A prime number
def rabin_karp_pattern_search(txt, pat, q):
    d = 256
    res = []
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in range(M - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(N - M + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters one by one
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
                else:
                    j += 1

            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j == M:
                res.append(i)

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q
    return res


# Python program for KMP Algorithm
def KMP_search(txt, pat):
    res = []
    M = len(pat)
    N = len(txt)
    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * M
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    compute_LPS_array(pat, M, lps)
    i = 0  # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            res.append(i - j)
            j = lps[j - 1]
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return res


def compute_LPS_array(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix
    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len - 1]
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


if __name__ == "__main__":
    txt = (
        "ABCEABFABCDEADACABCD" * 100
        + "ABCEABFABCDEADACABCDE" * 10
        + "ABCEABFABCDEADACABCD" * 100
    )
    pat = "ABCEABFABCDEADACABCDE" * 1
    # pat = "ABCD"
    timeit_number = 1000
    print(
        timeit(
            stmt="naive_pattern_search(txt=txt, pat=pat)",
            number=timeit_number,
            globals=globals(),
        )
    )
    print(
        timeit(
            stmt="distinct_naive_pattern_search(txt=txt, pat=pat)",
            number=timeit_number,
            globals=globals(),
        )
    )
    print(
        timeit(
            stmt="rabin_karp_pattern_search(txt=txt, pat=pat, q=257)",
            number=timeit_number,
            globals=globals(),
        )
    )
    print(
        timeit(
            stmt="KMP_search(txt=txt, pat=pat)",
            number=timeit_number,
            globals=globals(),
        )
    )
    print(rabin_karp_pattern_search(txt=txt, pat=pat, q=10**9 + 7))
