a=str(input()) 
b=str(input()) 
Q=len(a) 
MuTaTiOnS=0 
for i in range(Q): 
    if a[i]==b[i]: 
        continue 
    else: 
        MuTaTiOnS+=1 
print(MuTaTiOnS)
