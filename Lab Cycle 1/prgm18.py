l1=[]
l2=[]
l3=[]
n=int(input("Enter the number of elements for color list 1 "))
m=int(input("Enter the number of elements for color list 2 "))
print("for color list 1")
for i in range(0,n):
    ele=input("enter the color ")
    l1.append(ele)
print("for color list 2")
for i in range(0,m):
    ele1=input("enter the color ")
    l2.append(ele1)
print("Colors that are unique for color list 1")
l3=[x for x in l1 if x not in l2]
print(l3)
