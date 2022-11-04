dict1={}
n=int(input("Enter the number of elements in dictionary"))
for i in range(0,n):
    key=input("Enter the key")
    val=int(input("enter the value"))
    dict1[key]=val
temp=0
print(dict1)
sorted_dt = {key: value for key, value in sorted(dict1.items(), key=lambda item: item[1])}

print(sorted_dt)

