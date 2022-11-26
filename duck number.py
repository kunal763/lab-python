#waf to input a number and check wheather it is a duck number or not
def duck(n):
    f=0
    while n>0:
        d=n%10
        if d==0:
            f=f+1
        n=n//10
    if f>=1:
        print("Duck number!!!!🦆")
    else:
        print("not a duck number")
a=int(input("enter a number:"))
duck(a)
