#waf to create a file for entering some data into newline without using write() function
myfile=open(r"E:\student.dat","w")
L=[ ]
for i in range(5):
    a=input("Enter name:")
    L.append(a+'\n')
myfile.writelines(L)
myfile.close()
