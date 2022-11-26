def angle(a,b,c):
    if a>b and a>c:
        print("the largest angle is",a)
    if b>c and b>a:
        print("the largestangle is ",b)
    if c>a and c>b:
        print("the laragest angle is",c)
x=int(input("enter an angle:"))
y=int(input("enter an angle:"))
z=int(input("enter an angle:"))
t=angle(x,y,z)
print("the largest angle is ",t)

