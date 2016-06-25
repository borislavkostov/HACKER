n=int(input('Enter n: '))
v=int(input('Enter v zero or one: '))
p=int(input('Enter p: '))
if v==0 :
      n=n&(~(1<<p))
else:
      n=n|(1<<p)
print(n)
