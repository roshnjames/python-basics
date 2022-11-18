print("firsl list")
n1=int(input("enter the length of first list"))
lst1=[]
lst2=[]
ele=0
sum1=0
sum2=0
flag=0
for i in range(0,n1):
    ele=int(input("enter an element"))
    lst1.append(ele)

print("second list")
n2=int(input("enter the length of second list"))
lst2=[]
for i in range(0,n2):
    ele=int(input("enter an element"))
    lst2.append(ele)

print("first list")
for i in range(0,n1):
    print(lst1[i])

print("second list")
for i in range(0,n2):
    print(lst2[i])

if(len(lst1)==len(lst2)):
    print("Both the lists are of same length")
else:
    print("Lists have different length")


for i in range(0,n1):
    sum1+=lst1[i]
for i in range(0,n1):
    sum2+=lst2[i]

if(sum1==sum2):
    print("Sum is same")
else:
    print("sum is different")

if(n1>n2):
    l=n1
    s=n2
else:
    l=n2
    s=n1


for i in range(0,l):
    for j in range(0,s):
        if(lst1[i]==lst2[j]):
            flag=1
            break

if(flag==1):
    print("Same element occurs")
else:
    print("No same element")



    
