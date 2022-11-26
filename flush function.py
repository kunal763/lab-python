#read the full text without using read
f=open("E:\pc.log","r")
s=" "
while s:
    s=f.readline()
    print(s,end="") 
f.close()
