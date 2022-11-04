n=int(input("Enter the year upto which you want to check"))
if(n<2022):
    print("please enter a future year")
else:
    for i in range(2022,n):
        if((i%400==0) or ((i%4==0) and (i%100!=0))):
            print(i," is leap year")
        else:
            print(i," is not a leap year")
