def getByIndex(arr,n,idx):
    # return required ans
    if idx > n-1: 
        return -1
    return arr[idx]

def insertAtEnd(arr,sizeOfArray,element):
    ##Your code here
    arr.append(element)
    return arr

def insertAtIndex(arr, sizeOfArray, index, element):
    #Your code here
    arr.insert(index,element)
    return arr

def updateArray(arr,n,idx,element):
    #code here
    arr[idx] = element
    
    
def deleteFromArray(arr,n,idx):
    #code here
    del arr[idx]
    arr.append(0)
    return arr


def median(A,N):
    ##Your code here
    A.sort()
    if N % 2 == 0:
        return (A[(N//2) - 1] + A[(N//2)])//2
    else:
        return A[((N-1)//2)]
    
    #If median is fraction then convert the median to integer and return
    
#Function to find mean of the array elements.   
def mean(A,N):
    ##Your code here
    return sum(A)//N

print(mean([1,1,1,1,1,1],6))
print(median([1,1,1,1,1,1],6))