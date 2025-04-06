A = [10,5,2,1,7,4]
n=len(A)

for i in range(1,n):
    temp =A[i]
    j=i-1

    while j>=0 and A[j]>temp:
        A[j+1] = A[j]
        j=j-1

    A[j+1] = temp
    
print(A)