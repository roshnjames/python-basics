str=input("enter a line of text")
l=[]
l=str.split(" ")
count=[]
co=0
temp=[]
for i in range(0,len(l)):
    w=l[i]
    
    for j in range(i,len(l)):
        if(w==l[j]):
            if(w not in temp):
                co+=1
    if(co!=0):
        count.append(co)
    if(w not in temp):
        temp.append(w)
    co=0
print("printing count of every word")
for i in range(0,len(temp)):
    print(temp[i],':',count[i])
