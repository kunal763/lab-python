#waf to input a number add even and odd digit
def eveoddsum(n):
    evensum=oddsum=0
    while n>0:
        d=n%10
        if d%2==0:
            evensum=evensum+d
            n=n//10
        elif d%2!=0:
            oddsum=oddsum+d
            n=n//10
    print("Sum of evendigits=",evensum)
    print("Sum of odd digits=",oddsum)
a=int(input("enter a number : "))
eveoddsum(a)
