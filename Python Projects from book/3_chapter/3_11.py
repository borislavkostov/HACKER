n=int(input('Enter n: '))
p=int(input('Enter p: '))
i=1
mask=i<<p
if n&mask !=0:
      print("The bit in position ",p,"is = 1")
else:
      print("The bit in position ",p,"is = 0")
