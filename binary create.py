import pickle
list =[]
n=int(input("how much student data you want ot enter"))
while n>0:
    roll = input("Enter student Roll No:")
    sname  = input("Enter student Name :")
    student = {"roll":roll,"name":sname}
    list.append(student)
    n=n-1

file = open("student.dat","wb")
pickle.dump(list,file)
file.close()
