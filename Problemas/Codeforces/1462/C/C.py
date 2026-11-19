m=0

def solve():
    p={1,2,3,4,5,6,7,8,9}
    f=""
    n=0
    s=0
    r=m
    while len(p):
        n=max(p)
        s+=n
        f+=str(n)
        if (r-s)==0:
            return f[::-1]
        if (r-s)<0:
            s-=n
            f=f[:-1]
        p.remove(n)
    return -1


n=int(input())
while (n:=n-1)>-1:
    m=int(input())
    print(solve())
