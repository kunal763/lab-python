#ask the child how many subject exam does he gave and what was the maximum marks
#and tell total %,average marks and print a message of "good" if the child has got above 70%and
def marks(a,b):
    tm=0
    for i in range(1,a+1):
        print("enter total number of subjects",i," : ")
        marks=int(input())
        tm=tm+marks    #calculating the total marks step by step
    avg=tm/a
    print("AVerage marks=",avg)
    rtm=a*b
    percent=(tm/rtm)*100
    print("Total percent=",percent,"%")
    if percent>=70:
        print("HURRRAY!!!!!!")
    else:
        print("bEtter LUCK next time :(")
c=int(input("enter total number of subjects : "))
d=int(input("What was the total marks!!!  "))
marks(c,d)
