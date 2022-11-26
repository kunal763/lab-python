def listh(L):
    n=len(L)
    for i in range(0,n):# loop ko n bar chalana hai kyunki max to max list ko n bar sort karna pad sakta hai
        for j in range(0,n-i-1):
            if L[j]>L[j+1]:
                t=L[j]
                L[j]=L[j+1]
                L[j+1]=t
    print(L)
l=eval(input("enter list:"))
listh(l)
