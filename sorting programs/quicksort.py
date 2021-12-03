def partition(A,l,h):
    pivot=A[l]
    start=l
    end=h
    while(start < end):
        while(A[start] <= pivot):
            start += 1
            if(start > end):
                break
        while(A[end] > pivot):
            end -= 1
        if(start < end):
            A[start],A[end]=A[end],A[start]
    A[l],A[end]=A[end],A[l]
    return end

def Quicksort(A,l,h):
    if(l < h):
        correct_position=partition(A,l,h)
        Quicksort(A,l,correct_position-1)
        Quicksort(A,correct_position+1,h)

A=[7,6,10,5,9,2,1,15,7]#[4,2,7,3,1,6]
n=len(A)
Quicksort(A, 0, n-1)
print(A)

#[7,6,10,5,9,2,1,15,7]