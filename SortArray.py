a= [10,5,15,4,6,20,9]
temp=0

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j] :
             temp= a[i]
             a[i]   = a[j] 
             a[j]   = temp
            
            
print(a)
            