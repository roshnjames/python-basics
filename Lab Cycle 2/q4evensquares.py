import math


def fourdigits(num1,num2):
    i=num1
    m=0
    k=0
    while i<=num2:
        k=i
        l = []
        while k>0:
            m=k%10
            if((m%2)!=0):
                l.append(m)
            k=int(k//10)
        
        if(len(l)==0):
            root=math.sqrt(i)
            if int(root)==math.sqrt(i):
                print(i, " is a perfect square with all digits as even")
        i=i+1





num1=int(input("Enter first integer limit"))
num2=int(input("Enter second integer limit"))


if(num1<1000) or (num2<1000):
    print("Enter four digit numbers only")
elif(num1>num2):
    print("Fist number should always be less than second number")
else:
    fourdigits(num1,num2)



            
        

            
