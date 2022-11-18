def listsum(l):
    sum=0
    for i in l:
        sum=sum+i
    return sum


n=int(input("Enter the length of the list"))
l=[]
for i in range(0,n):
    ele=int(input("Enter the list element"))
    l.append(ele)
print("Entered list is ",l)
sum=listsum(l)
print("Sum is ",sum)
