def nCr(n,r):
    #code here
    # nCr = (n-1)C(r-1) + (n-1)Cr
    if n==r or r==0:
        return 1
    return nCr(n-1,r-1) + nCr(n-1,r)

print(nCr(5,2))