l1=[]
n=int(input("enter the number bof elements"))
for i in range(0,n):
    ele=input("enter the name")
    l1.append(ele)

print(l1)
count=0
for i in range(0,n):
    w=l1[i]
    l=len(w)
    for j in range(0,l):
        x=w[j]
        if((x=='a') or (x=='A')):
            count+=1

print("Count of a is ",count)
