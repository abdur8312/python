def LinearSearch(List,b):
    n=len(List)
    for i in range(n):
        if(b == List[i]):
            return List[i]
List=[1,2,3,4,5,6,7,8,9,10]
b=4 #int(input("Enter a number to search in the list:"))
a=LinearSearch(List,b)
print(a)