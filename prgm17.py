n=int(input("enter an integer"))
sum=0
l=int(input("enter the limit upto you want the serial sum of"))
for i in range(0,l):
    for j in range(0,i):
        sum=sum+(n*j)
