from sys import stdin
pwds = list(map(lambda x: int(''.join(x)), map(lambda x: x.split(), stdin.readlines())))
for i in pwds:
    print(f'{i:04d}')