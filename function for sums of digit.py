"""waf to input  anumber calc. and print the sum of the digits:"""
#58=5+8=13

def digsum(n):
    s=0
    while n>0:
        d=n%10
        s=s+d
        n=n//10
    return s
a=int(input("enter a number:"))
x=digsum(a)
print("the digit sum=",x)
