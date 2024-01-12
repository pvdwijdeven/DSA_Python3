def binsort(A):
    N = len(A)
    l,r=0,N-1
    while l<r:
        while l<r and A[l]==0:
            l+=1
        while l<r and A[r]==1:
            r-=1
        if l<r:
            A[l],A[r]=A[r],A[l]
            l+=1
            r-=1
    return A


print(binsort([0,1,1,1,0,0,0]))