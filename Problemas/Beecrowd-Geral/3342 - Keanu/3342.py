from math import ceil
n = int(input())
n = n*n

b = n//2 if n % 2 == 0 else (n//2) + 1
p = b if n % 2 == 0 else b - 1

print(f'{b} casas brancas e {p} casas pretas')