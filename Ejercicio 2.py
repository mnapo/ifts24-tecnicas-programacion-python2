# calcular serie Fibonacci hasta el 100

n1 = 0
n2 = 1
print(n1)
print(n2)
while n2<100:
  temp = n2
  n2 += n1
  n1 = temp
  print(n2)
