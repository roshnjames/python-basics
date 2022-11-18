def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return(f)


num=int(input("Enter a number to find factorial"))
factorial=fact(num)
print("Factorial is ",factorial)


