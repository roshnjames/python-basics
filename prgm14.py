a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if(a>b):
    if(a>c):
        print("largest is ",a)
    else:
        print("largest is ",c)
elif(b>c):
    print("largest is ",b)
elif(c>b):
    print("largest is ",c)
else:
    print("same values entered")
