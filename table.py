#program to show the table of the shown number
def table(n,g):
    for i in range(1,g+1):
        c=n*i   #calculating the product
        print(n,"X",i,"=",c)
a=int(input("Enter the number of which you want to print the table :)"))
b=int(input("Enter the number of multiples you want :"))
table(a,b)
