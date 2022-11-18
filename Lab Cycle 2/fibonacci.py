def fibonacci(n):
    num1=0
    num2=1
    print(num1,"\n")
    print(num2,"\n")
    num3=num1+num2
    print(num3,"\n")
    for i in range(0,n-3):
        num1=num2
        num2=num3
        num3=num1+num2
        print(num3,"\n")
        
    

n=int(input("Enter the Fibonacci series limit you want\n"))
f=fibonacci(n)
