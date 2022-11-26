#wap to print the hcf of the  given number
def  hcf(a,b):
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            h=i
    print("hcf=",h)
a=int(input("enter  number:"))
b=int(input("enter  number:"))
hcf(a,b)
