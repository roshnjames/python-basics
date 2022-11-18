str=input("Enter a string")
l=[]
l=list(str)
n=len(l)
l[0],l[n-1]=l[n-1],l[0]
print("After swapping")
print(l)
