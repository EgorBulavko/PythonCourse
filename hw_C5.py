n=int(input())
k=int(input())
A = [1,1]
i=2
while i!=n:
    b = k*A[i-2] + A[i-1]
    A.append(b)
    i+=1
print(A[-1])
