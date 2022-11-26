def searchelement(a):
    length=len(a)
    element=int(input("enter element to be search for:"))
    for i in range(0,length):
        if element==a[i]:
            print(element,"found at index:",i)
            break
    else:
            print(element,"not found at any index:")
        
a=eval(input("enter list:"))
searchelement(a)
