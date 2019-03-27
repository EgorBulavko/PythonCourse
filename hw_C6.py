A = input()
B = input()
b=len(B)
a=len(A)
for i in range(a-b):
    j=1
    k=i
    M=''
    while j!=b+1:
        M+=A[k]
        j+=1
        k+=1
    if M==B:
        print(i+1, end=' ')
    else:
        continue
