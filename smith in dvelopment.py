n=int(input("netr num:")
for i in range(1,n+1):
    if n%i==0:
      for j in range(2,i):
         if i%j!=0:
             print(i)
        
