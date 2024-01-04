def maximumElement(arr,n):
    #return required result
    ans = 0
    for x in arr:
        if x > ans:
            ans = x
    return ans



def minimumElement(arr,n):
    #return required result
    
    ans = 10**7
    for x in arr:
        if x < ans:
            ans = x
    return ans
    
print(maximumElement([5,4,2,1],4))
print(maximumElement([8],1))
print(minimumElement([5,4,2,1],4))
print(minimumElement([8],1))