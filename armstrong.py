def armstrong(a):
    s=0
    n=a
    while a>0:
        d=a%10
        s=s+d**3
        a=a//10
    if s==n:
        print(n,"is an armstrong number")
    else:
        print(n,"is not an armstrong number")

b=int(input("enter a number : "))
armstrong(b)

        
