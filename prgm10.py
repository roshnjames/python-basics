n=int(input("Enter the limit of your list"))
l=[]
for i in range(0,n):
    ele=int(input("Enter a value"))
    if(ele>100):
        l.append("over")
    else:
        l.append(ele)

print("Created list is")
print(l)
