a = int(input())
b = int(input())
c = int(input())
D = b**2 - 4*a*c
if D<0:
    print('Корней нет')
else:
    print((-b+D**0.5)/(2*a), (-b-D**0.5)/(2*a))
