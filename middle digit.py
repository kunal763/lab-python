#wap to print middle digit of the given number
def middledigit(a):
    c=0
    k=e=a
    while a>0:
        d=a%10
        c=c+1
        a=a//10
    if c%2!=0:
        x=c//2
        m=int(k/(10**x))
        z=m%10
        print("middle digit=",z)
    else:
        n=c//2
        f=int(e/(10**n))
        f=f%10
        z=int(e/(10**(n-1)))
        z=z%10
        s=z+f
        print("sum of two middle digits=",s)
a=int(input("enter a number:"))
middledigit(a)
