import math
n=int(input("Enter n = "))
numbers =[1]
for x in range(1,3200000):
      result=x*x
      numbers.append(result)

str1 = ''.join(str(e) for e in numbers)
print(str1[n])

