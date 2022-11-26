#wap to input n numbers from the user and print the factorial of odd numbers.
def oddfactorial(n):
    for i in range(1,n+1):
        f=1
        k=1
        print("enter number",i,":")
        a=int(input())
        
        if a%2!=0:    #checking odd number
           
            for j in range(1,a+1):      #finding the factorial
                f=f*j
            print("Factorial of odd number=",f)#k is a counter which will count odd  number
            f=1
       
a=int(input("how many numbers you want to enter:)"))
oddfactorial(a)
