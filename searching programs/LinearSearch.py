Input=int(input("Enter a number:"))
A=[1,2,3,4,5,6,7,8,9,10]
n=len(A)
for i in range(n):
    if(Input in [A[i]]):
        print("True")