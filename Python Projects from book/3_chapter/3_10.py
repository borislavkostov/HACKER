number =int(input('Enter number'))

d=number%10
c=number/10
c=int(c)%10
b=number/100
b=int(b)%10
a=number/1000
a=int(a)%10
total=a+b+c+d
print("Total =",total)
print('{0}{1}{2}{3}'.format(d,c,b,a))
print('{0}{1}{2}{3}'.format(d,b,c,a))
print('{0}{1}{2}{3}'.format(a,c,b,d))
