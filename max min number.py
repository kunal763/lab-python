#wap to input 10 numbers from the user and print the max imum number and th emin number
def maxandmin(n):
    min=n
    max=0
    for i in range(1,10):
        a=int(input("enter number:)"))
        if min>a:
            min=a
        elif max<a:
            max=a
    print("smallest number=",min)
    if max<n:
        max=n
    print("largest number=",max)
b=int(input("enter number:)"))
maxandmin(b)
