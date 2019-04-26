def killer(b):
    cd=0
    for i in range(1,b+1):
        if b%i==0:
            cd+=1
    return cd

def simple_num_gen(a):
    cur = 1
    for i in range(1,a+1):
        if killer(i)==2:
            yield i

for curr in simple_num_gen(int(input())):
    print(curr, end=' ')
