#waf to input a number and check wheather it is a kaprerkar number or not
def kaprekar(a):
    sq=a*a
    n=a
    t=1
    while a>0:
        t=t*10
        a=a//10
    x=sq%t
    y=sq//t
    s=x+y #Sum of the two parts of the square
    if s==n:
        print("kaprekar number!!!!!😀")
    else:
        print("not a kaprekar number  😟")
n=int(input("enter a number : "))
kaprekar(n)
