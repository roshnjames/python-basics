
str=input("Enter the string")
l=[]
l=list(str)
c=l[0]
for i in range(1,len(l)):
    if(l[i]==c):
        l[i]='$'
    
print(l)
