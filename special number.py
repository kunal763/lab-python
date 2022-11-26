def check(n):
    a=n
    s=0
    while n>0:
        #mujhe lagta hai ki yahan s lene par ye galat hoga
        f=1
        d=n%10
        for i in range(1,d+1):
            f=f*i
        s=s+f
        n=n//10
    if a==s:
        print("Special Number!!!")
    else:
        print("not a special number!!!")    
num=int(input("enter anumber"))
print(check(num))
