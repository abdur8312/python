def BinarySearch(List,key):
    n=len(List)
    l=0
    h=n-1
    while(l <= h):
        mid=(l+h)//2
        if(key == List[mid]):
            return List[mid]
        elif(key < List[mid]):
            h=mid-1
        else:
            l=mid+1
    if(l > h):
        return "Number not found"
List=[3,6,8,12,14,17,25,29,31,36,42]
key=36 #int(input("Enter a number to search in the List:"))
b=BinarySearch(List,key)
print(b)
