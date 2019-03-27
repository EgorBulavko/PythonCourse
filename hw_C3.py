A = [str(var) for var in input().split( )]
a=len(A[0])
for i in range(1,len(A)):
    if len(A[i])<len(A[i-1]):
        a=len(A[i])
print(a)
