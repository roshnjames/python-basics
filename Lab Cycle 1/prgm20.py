l1=[]
l2=[]
n=int(input("Enter the number of elements"))
for i in range(0,n):
    ele=int(input("enter the number "))
    l1.append(ele)
print("After removing even numbers")
l2=[x for x in l1 if x%2!=0]
print(l2)
