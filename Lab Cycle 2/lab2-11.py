def factors(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    return(l)


n=int(input("Enter an integer to get factors "))
l1=[]
l1=factors(n)
print("the factors are ",l1)
    
