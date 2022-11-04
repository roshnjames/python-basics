dict1={}
dict2={}
n=int(input("Enter the number of elements in dictionary 1"))

for i in range(0,n):
    key=input("Enter the key")
    val=int(input("enter the value"))
    dict1[key]=val

m=int(input("Enter the number of elements in dictionary 2"))
for i in range(0,m):
    key=input("Enter the key")
    val=int(input("enter the value"))
    dict2[key]=val
print(dict1)
print(dict2)


d3={**dict1,**dict2}
for k,v in d3.items():
    if k in dict1 and k in dict2:
        d3[k]=[v,dict1[k]]
print(d3)
