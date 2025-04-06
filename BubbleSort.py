A = [5,2,1,7,4,20]
n=len(A)
temp=[0]

for i in range(n-1):
    flag =0
    for j in range(n-1-i):
        if A[j]>A[j+1]:
            temp  =A[j]
            A[j]  =A[j+1]
            A[j+1]=temp
            flag=1
    
    if flag==0:
        break

print(A)