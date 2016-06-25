v=int(input('Enter v: '))
p=int(input('Enter p: '))
i=1
mask=i<<p
isOne=v&mask!=0
print(isOne)
