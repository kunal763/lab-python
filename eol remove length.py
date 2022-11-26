#program to display the size of a file after removing eol characters leading and tracing white spaces
myfile=open(r'E:\story.txt',"r")
str=" "
s=r=0
while str:
    str=myfile.readline()
    s=s+len(str)
    r=r+len(str.strip())
print("The size before removing eol characters",s)
print("The size after removing eol characters",r)
