def big_andsecbig(a):
    length=len(a)
    big=secondbig=a[0]
    for i in range(1,length):
        if a[i]>big:
            secondbig=big
            big=a[i]
        elif a[i]>secondbig:
            secondbig=a[i]
    print("largest number:",big)
    print("second largest number:",secondbig)
a=eval(input("enter list:"))
big_andsecbig(a)
